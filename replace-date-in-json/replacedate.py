# Search through json file to replace formatted dates with UNIX timestamps
import json
import time
import datetime

# Read in the JSON
with open('file.json') as json_file:
    json_decoded = json.load(json_file)

# Go through each object in the JSON file
for entry in json_decoded:
    # Get current value for startTime
    timeString = entry['startTime']
    # Convert the current formatted time string to UNIX datestamp format
    timeStamp = int(time.mktime(datetime.datetime.strptime(timeString, "%Y-%m-%dT%H:%M:%S.000Z").timetuple()))
    # Replace the date
    entry['startTime'] = str(timeStamp)

# Write new file with converted time values
with open('file-converted.json', 'w') as json_file:
    json.dump(json_decoded, json_file, indent=4, sort_keys=True)
