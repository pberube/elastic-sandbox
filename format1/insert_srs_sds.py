import re
import requests
from constants import filename, pattern_sds, pattern_srs

textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()


# find all matches for SRS
matches = re.findall(pattern_srs, filetext)
# remove duplicates from matches and get ordered list
srs = list(dict.fromkeys(matches))

# find all matches for SDS
matches = re.findall(pattern_sds, filetext)
# remove duplicates from matches and get ordered list
sds = list(dict.fromkeys(matches))

def url(id):
    return 'http://localhost:30000/api/v1/elastic/' + str(id)

def req_data(title, prefix):
    return {
        "title": title,
        "description": "string",
        "type": "string",
        "prefix": prefix
        }
h = {'Content-Type': 'application/json', 'accept': 'application/json'}

id = 0
for i, s in enumerate(srs):
    requests.post(url(id), json=req_data(s[6:], 'srs'), headers=h)
    id = id + 1

for i, s in enumerate(sds):
    requests.post(url(id), json=req_data(s[6:], 'sds'), headers=h)
    id = id + 1
