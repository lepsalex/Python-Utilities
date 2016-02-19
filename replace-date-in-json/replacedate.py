# Search through json file to replace formatted dates with UNIX timestamps
import time
import datetime

# Read in the file
file = open('file.json', 'r')
# Create temporary file buffer to manipulate
fileData = file.read()
file.close()

# Go through the file line-by-line
for line in open('file.json'):
    # If the query string is present in the line
    if "startTime" in line:
        # Get the line and strip empty space
        lineString = line.strip()
        # Slice the line for the current date length
        timeString = lineString[14:-2]
        # Convert the current formatted time string to UNIX datestamp format
        timeStamp = time.mktime(datetime.datetime.strptime(timeString, "%Y-%m-%dT%H:%M:%S.000Z").timetuple())
        # Replace the date
        fileData = fileData.replace(timeString, str(timeStamp))

# Read in file for write this time
f = open('file-converted.json','w')
# Write filedata (buffer) to file
f.write(fileData)
f.close()
