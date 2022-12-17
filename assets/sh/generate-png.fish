#!/usr/local/bin/fish
# This is a fish script, and can only be run in fish.

set version (ls -lha | grep -P -o '(\d(\.\d)+)$')

(which python3) assets/py/dds-to-png.py -i $PW -o