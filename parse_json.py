import json

with open('DATA/presidents.json') as pres_in:
    pres_data = json.load(pres_in)  # parse json into data structure

print(type(pres_data))
entries = pres_data['presidents']
for entry in entries:
    print(entry.get("lastname"), entry.get('party'))

# pres_data = json.loads(some_string)
