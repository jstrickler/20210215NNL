#!/usr/bin/env python
import os

path = os.getenv('PATH')
print("PATH:", path)
print("PATH separator:", os.pathsep)
paths = path.split(os.pathsep)
print("-" * 60)
for path in paths:
    print(path)
print()

for path_dir in paths:
    if os.path.exists(path_dir):
        all_files = os.listdir(path_dir)
        print("{:4d}: {}".format(len(all_files), path_dir))
    else:
        print("WARNING: {} is in PATH, but does not exist".format(path_dir))
