import json

# Open the input file
with open('2024-04-14-DRE_dump.json', 'r') as input_file:
    # Load the JSON data
    data = json.load(input_file)

# Calculate the number of items per part
items_per_part = len(data) // 9

# Split the data into parts
parts = [data[i:i+items_per_part] for i in range(0, len(data), items_per_part)]

# Add the remaining items to the last part
parts[-1].extend(data[items_per_part*9:])

# Write each part to a separate file
for i, part in enumerate(parts):
    # Generate the output file name
    output_file_name = f'2024-04-14-DRE_dump_part{i+1}.json'
    
    # Write the part to the output file
    with open(output_file_name, 'w') as output_file:
        json.dump(part, output_file, indent=4)