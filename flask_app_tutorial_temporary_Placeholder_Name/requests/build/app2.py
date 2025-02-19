import requests
from pprint import pprint
import json

dictioniary = {'userKey': 'userValue'}
json_Value = json.dumps(dictioniary)
print('json_Value:', json_Value)
url = requests.post("https://httpbin.org/post", json=json_Value)

if url.status_code:
    pprint({'url.status_code:': url.status_code})
if url.text:
    print(url.text)
    print("\n")
if url.json():
    pprint(url.json())