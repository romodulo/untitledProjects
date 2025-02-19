import requests
from pprint import pprint, pformat
import json
import os
import shelve

shelf_d = shelve.open("shelf_d")
shelf_d["json"] = {'userKey': 'userValue'}
shelf_d.close()
#initialize:
shelf_d = shelve.open("shelf_d")
raw = shelf_d["json"]
shelf_d.close()
#did-it_extract: 
jsonValue = json.dumps(raw)
print('json_Value:', jsonValue)
response = requests.post("https://httpbin.org/post", json=raw, headers={'User-Agent':'webscraper: v1.0.0'})
#write to file:
fileName = "openText.py"
write = "w"
append = "a"
writeOrAppendMode = write
if os.path.isfile(f"./{fileName}"):
    pass
else:
    fileObject = open(fileName, "w")
    fileObject.close()
fileObject = open("openText.py", writeOrAppendMode)
# fileObject.write(response.json())
fileObject.write(pformat(response.json()))
fileObject.close()

def if_run():
    if response.status_code:
        pprint({'response.status_code:': response.status_code})
    if response.text:
        print(response.text)
        # print("\n")
    if response.json():
        pprint(response.json())
#initialize:
response_variable = response.json()
# pprint(dir(response_variable))
# pprint(dict(response_variable.items()))
