import os
from datetime import datetime

FOLDER = 'DATA'   # ../../docs/stuff
FILENAME = 'mary.txt'

file_path = os.path.join(FOLDER, FILENAME)
print("file_path: {}\n".format(file_path))
file_size = os.path.getsize(file_path)
print("file_size: {}\n".format(file_size))
abs_path = os.path.abspath(file_path)
print("abs_path: {}\n".format(abs_path))
raw_timestamp = os.path.getmtime(file_path)
print("raw_timestamp: {}\n".format(raw_timestamp))
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp: {}\n".format(timestamp))
print(os.path.isfile(file_path))
print(os.path.isdir(file_path), '\n')

start_dir = os.path.abspath('.')
for folder, subfolders, filenames in os.walk(start_dir):
    for file_name in filenames:
        if file_name == 'words.txt':
            file_path = os.path.join(folder, file_name)
            print(file_path)
print()

#   relative  just
#   path      folder
for folder, subfolders, file_names in os.walk('.'):
    if '.git' in subfolders:
        subfolders.remove('.git')
    print(folder)
    for file_name in file_names:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            print("   {:8d} {}".format(file_size, file_name))

print("-" * 60)

for folder, subfolders, file_names in os.walk('.'):
    if '.git' in subfolders:
        subfolders.remove('.git')
    print("FOLDER:", folder)
    print("SUBFOLDERS:", subfolders)
    print()


