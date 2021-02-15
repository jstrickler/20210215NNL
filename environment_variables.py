import os

# os.environ.get(...)
user_profile_dir = os.getenv('USERPROFILE')
print("user_profile_dir: {}\n".format(user_profile_dir))

wombats = os.getenv('WOMBATS')
print(wombats)

wombats = os.getenv('WOMBATS', 'marsupials')
print(wombats)

print(os.environ)  # dict of all environment variables
print()

