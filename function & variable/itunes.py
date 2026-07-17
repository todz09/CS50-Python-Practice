import json                     # for better formatting of the output
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=3&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent=1))        
'''
print(json.dumps(response.json(), indent=1))  # for better formatting of the output (understandable)
print(response.json())  # for normal formatting of the output (not understandable)
'''

o = response.json()

for result in o['results']:
    print(result['trackName'])