#!/usr/local/bin/fish
# This is a fish script, and can only be run in fish.

set version (python3 loadPayload.py)

python3 assets/py/dds-to-png.py -i $version/technologies/ -o $version/technologies-output
