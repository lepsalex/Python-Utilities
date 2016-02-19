import time
import datetime

# Read in the file
file = open('data.json', 'r')
filedata = file.read()
file.close()

# Generate replacement array
query = [];
for line in open('data.json'):
    if "startTime" in line:
        s = line.strip()
        t = s[14:-2]
        query.append(t)

# Replace the target string
for replacement in query:
    timestamp = time.mktime(datetime.datetime.strptime(replacement, "%Y-%m-%dT%H:%M:%S.000Z").timetuple())
    filedata = filedata.replace(replacement, str(timestamp))

# Write the file out again
f = open('data.json','w')
f.write(filedata)
f.close()
