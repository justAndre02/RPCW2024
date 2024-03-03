import json

# Open the JSON file with UTF-8 encoding
with open('dataset.json', 'r', encoding='utf-8') as f:
    bd = json.load(f)

ttl = """
"""

ttl += ttl
# Write the TTL data to a file
with open('output.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

print("TTL data has been written to output.ttl")
