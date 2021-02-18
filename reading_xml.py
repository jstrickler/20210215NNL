import lxml.etree as ET

doc = ET.parse('people.xml')
print(doc)

root = doc.getroot()
print(root)
for person in root.findall('person'):
    print(person.findtext('first_name'), person.findtext('last_name'))
print("-" * 60)

# find(tag)
# findall(tag)
# findtext(tag)

doc = ET.parse('people.xml')
for person in doc.findall('.//person'):
    print(person.findtext('first_name'), person.findtext('last_name'))

