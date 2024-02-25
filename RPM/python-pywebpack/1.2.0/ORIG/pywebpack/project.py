# -*- coding: utf-8 -*-
#
# This file is part of PyWebpack
# Copyright (C) 2017-2020 CERN.
# Copyright (C) 2020 Cottage Labs LLP.
#
# PyWebpack is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""API for creating and building Webpack projects."""

from __future__ import absolute_import, print_function

import json
import shutil
from os import makedirs
from os.path import dirname, exists, join

from pynpm import NPMPackage, YarnPackage

from .helpers import cached, check_exit, merge_deps
from .storage import FileStorage


class WebpackProject(object):
    """API for building an existing Webpack project."""

    def __init__(self, path):
        """Initialize instance."""
        self._npmpkg = None
        self._path = path

    @property
    def project_path(self):
        """Get the project path."""
        return dirname(self.npmpkg.package_json_path)

    @property
    def path(self):
        """Path property."""
        return self._path

    @property
    @cached
    def npmpkg(self):
        """Get API to NPM package."""
        return NPMPackage(self.path)

    @check_exit
    def install(self, *args):
        """Install project."""
        return self.npmpkg.install(*args)

    def run(self, script_name, *args):
        """Run an NPM script."""
        scripts = self.npmpkg.package_json.get('scripts', {}).keys()
        if script_name not in scripts:
            raise RuntimeError('Invalid NPM script.')
        return self.npmpkg.run_script(script_name, *args)

    @check_exit
    def build(self, *args):
        """Run build script."""
        return self.run('build', *args)

    def buildall(self):
        """Build project from scratch."""
        self.install()
        self.build()


class WebpackTemplateProject(WebpackProject):
    """API for creating and building a webpack project based on a template.

    Copies all files from a project template folder into a destination path
    and optionally writes a user provided config in JSON into the destination
    path as well.
    """

    def __init__(self, working_dir, project_template_dir, config=None,
                 config_path=None, storage_cls=None):
        """Initialize templated folder.

        :param working_dir: Path where config and assets files will be copied.
        :param project_template_dir: absolute path to the project folder.
        :param config: Dictionary used to create the `config.json` file
            generated by pywebpack. It adds extra configuration at build time.
        :param config_path: Path in `working_dir` where `config.json` will
            be written.
        :param storage_cls: Storage class.
        """
        self._project_template_dir = project_template_dir
        self._storage_cls = storage_cls or FileStorage
        self._config = config
        self._config_path = config_path or 'config.json'
        super(WebpackTemplateProject, self).__init__(working_dir)

    @property
    def config(self):
        """Get configuration dictionary."""
        if self._config is None:
            return None
        config = self._config() if callable(self._config) else self._config
        return config

    @property
    def config_path(self):
        """Get configuration path."""
        return join(self.project_path, self._config_path)

    @property
    def storage_cls(self):
        """Storage class property."""
        return self._storage_cls

    def create(self, force=None, skip=None):
        """Create webpack project from a template."""
        self.storage_cls(self._project_template_dir, self.project_path).run(
            force=force, skip=skip)

        # Write config if not empty
        config = self.config
        config_path = self.config_path
        if config:
            # Create config path directory if it does not exists.
            if not exists(dirname(config_path)):
                makedirs(dirname(config_path))
            # Write config.json
            with open(config_path, 'w') as fp:
                json.dump(config, fp, indent=2, sort_keys=True)

    def clean(self):
        """Clean created webpack project."""
        if exists(self.project_path):
            shutil.rmtree(self.project_path)

    def buildall(self):
        """Build project from scratch."""
        self.create()
        super(WebpackTemplateProject, self).buildall()


class WebpackBundleProject(WebpackTemplateProject):
    """Build webpack project from multiple bundles."""

    def __init__(self, working_dir, project_template_dir, bundles=None,
                 config=None, config_path=None, storage_cls=None,
                 package_json_source_path='package.json'):
        """Initialize templated folder.

        :param working_dir: Path where config and assets files will be copied.
        :param project_template_dir: Absolute path to the project folder.
        :param bundles: List of
            :class:`pywebpack.bundle.WebpackBundle`. This list can be
            statically defined if the bundles are known before hand, or
            dinamically generated using
            :func:`pywebpack.helpers.bundles_from_entry_point` so the bundles
            are discovered from the defined Webpack entrypoints exposed by
            other modules.
        :param config: Dictionary used to create the `config.json` file
            generated by pywebpack. It adds extra configuration at build time.
        :param config_path: Path in `working_dir` where `config.json` will
            be written.
        :param storage_cls: Storage class.
        :param package_json_source_path: Path relative to
            `project_template_dir` to the project's package.json.
        """
        self._bundles_iter = bundles or []
        self._package_json_source_path = package_json_source_path
        super(WebpackBundleProject, self).__init__(
            working_dir,
            project_template_dir=project_template_dir,
            config=config or {},
            config_path=config_path,
            storage_cls=storage_cls,
        )

    @property
    def package_json_source_path(self):
        """Full path to the source package.json."""
        return join(
            self._project_template_dir, self._package_json_source_path)

    @property
    @cached
    def package_json_source(self):
        """Read original package.json contents."""
        with open(self.package_json_source_path, 'r') as fp:
            return json.load(fp)

    @property
    @cached
    def bundles(self):
        """Get bundles."""
        return list(self._bundles_iter)

    @property
    @cached
    def entry(self):
        """Get webpack entry points."""
        entries = dict(entries=dict(), paths=dict())
        error = 'Duplicated bundle entry for `{0}:{1}` in bundle `{2}` and ' \
            '`{3}:{4}` in bundle `{5}`. Please choose another entry name.'

        for bundle in self.bundles:
            for name, filepath in bundle.entry.items():
                # check that there are no duplicated entries
                if name in entries['entries']:
                    prev_filepath, prev_bundle_path = entries['paths'][name]
                    raise RuntimeError(error.format(name, prev_filepath,
                                                    prev_bundle_path, name,
                                                    filepath, bundle.path))
                entries['paths'][name] = (filepath, bundle.path)

            entries['entries'].update(bundle.entry)
        return entries['entries']

    @property
    def config(self):
        """Inject webpack entry points from bundles."""
        config = super(WebpackBundleProject, self).config
        config.update({'entry': self.entry, 'aliases': self.aliases})
        return config

    @property
    def aliases(self):
        """Get webpack resolver aliases from bundles."""
        aliases = dict(aliases=dict(), paths=dict())
        error = 'Duplicated alias for `{0}:{1}` in bundle `{2}` and ' \
            '`{3}:{4}` in bundle `{5}`. Please choose another alias name.'

        for bundle in self.bundles:
            for alias, path in bundle.aliases.items():
                # Check that there are no duplicated aliases
                if alias in aliases['aliases']:
                    prev_path, prev_bundle_path = aliases['paths'][alias]
                    raise RuntimeError(error.format(
                        alias, prev_path, prev_bundle_path,
                        alias, path, bundle.path))
                aliases['paths'][alias] = (path, bundle.path)

            aliases['aliases'].update(bundle.aliases)
        return aliases['aliases']

    @property
    @cached
    def dependencies(self):
        """Get package.json dependencies."""
        res = {
            'dependencies': {},
            'devDependencies': {},
            'peerDependencies': {}
        }
        for b in self.bundles:
            merge_deps(res, b.dependencies)
        return res

    @property
    @cached
    def package_json(self):
        """Merge bundle dependencies into ``package.json``."""
        # Reads package.json from the project_template_dir and merges in
        # bundle dependencies. Note, that package.json is not symlinked
        # because then we risk changing the source package.json automatically.
        return merge_deps(self.package_json_source, self.dependencies)

    def collect(self, force=None):
        """Collect asset files from bundles."""
        for b in self.bundles:
            self.storage_cls(b.path, self.project_path).run(force=force)

    def create(self, force=None):
        """Create webpack project from a template.

        This command collects all asset files from the bundles.
        It generates a new package.json by merging the package.json
        dependencies of each bundle.
        """
        # Skip package.json (because we will always write a new).
        super(WebpackBundleProject, self).create(
            force=force, skip=['package.json'])
        # Collect all asset files from the bundles.
        self.collect(force=force)
        # Generate new package json (reads the package.json source and merges
        # in npm dependencies).
        package_json = self.package_json
        # Write package.json (with collected dependencies)
        with open(self.npmpkg.package_json_path, 'w') as fp:
            json.dump(package_json, fp, indent=2, sort_keys=True)