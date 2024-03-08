#!/bin/bash
set -x
diff -Naur ORIG/ PATCHED/  > python-pywebpack-patch.txt
