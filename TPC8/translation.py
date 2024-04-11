import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('biblia.xml')
root = tree.getroot()

# Open the TTL file for writing
with open('output.ttl', 'w') as f:
    # Iterate over each <person> element
    for person in root.findall('.//person'):
        person_id = person.find('id').text
        name_given = person.find('namegiven').text
        sex = person.find('sex').text

        # Write the individual's data to the TTL file
        f.write(f'###  http://rpcw.di.uminho.pt/2024/familia#{person_id}\n')
        f.write(f':{person_id} rdf:type owl:NamedIndividual , :Pessoa ;\n')

        parent_sex = None
        for parent_ref in person.findall('parent'):
            parent_id = parent_ref.get('ref')
            parent = root.find(f'.//person[id="{parent_id}"]')
            parent_sex = parent.find('sex').text

            # Check if the parent is the mother or the father based on their sex
            if parent_sex == 'F':
                f.write(f'    :temMae :{parent_id} ;\n')
            elif parent_sex == 'M':
                f.write(f'    :temPai :{parent_id} ;\n')

        f.write(f'    :id "{person_id}" ;\n')
        f.write(f'    :nome "{name_given}" ;\n')
        f.write(f'    :sexo "{sex}" .\n')