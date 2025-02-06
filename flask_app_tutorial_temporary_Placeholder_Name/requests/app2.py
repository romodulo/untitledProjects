#! /home/romel-linux/untitledProjects/flask_app_tutorial_temporary_Placeholder_Name/requests/.ve-requests/bin/python
# message:

import requests
from pprint import pprint
import json

dictioniary = {'userKey': 'userValue'}
json_Value = json.dumps(dictioniary)
url = requests.post("https://httpbin.org/post", json=json_Value)

if url.status_code:
    pprint({'url.status_code:': url.status_code})
if url.text:
    print('url.text:',url.text)
if url.json():
    pprint({'json': url.json()})