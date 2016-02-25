# Add key/value pair to existing JSON after specific line
import json

# Read in the JSON
with open('file.json') as json_file:
    json_decoded = json.load(json_file)

# Go through each top-level object in the JSON file
for entry in json_decoded:
    # Add key/value
    entry['type'] = 'normal'

# Write new file with added key/value
with open('file-new.json', 'w') as json_file:
    json.dump(json_decoded, json_file, indent=4, sort_keys=True)
