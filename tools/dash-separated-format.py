#!/usr/bin/python3
import pathlib
import subprocess

for filename in pathlib.Path('.').glob('**/*.md'):
    # f = open(filename)
    print('file: %s' % filename)
    new_filename = str(filename).lower().replace(' ', '-')
    command = ['git', 'mv', filename, new_filename]
    print('would run: %s' % command)
    # subprocess.run(command)
