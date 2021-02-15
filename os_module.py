import os   # includes os.path

def better_dir(obj):
    attributes = [a for a in dir(obj) if not a.startswith('_')]
    return sorted(attributes)

print(better_dir(os))
print("-" * 60)

print(better_dir(os.path))
