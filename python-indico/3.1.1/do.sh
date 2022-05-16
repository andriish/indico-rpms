#!/bin/bash
set -x
diff -Naur ORIG/ PATCHED/  > indico-patch.txt
