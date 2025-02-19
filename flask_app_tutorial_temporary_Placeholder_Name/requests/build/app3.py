import requests
from pprint import pprint
import json
import os

rawValue = {'userKey': 'userValue'}
json_Value = json.dumps(rawValue)
print('json_Value:', json_Value)
url = requests.post("https://httpbin.org/post", json=rawValue, headers={'User-Agent':'webscraper: v1.0.0'})
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
fileObject.write(url.text)
fileObject.close()

if url.status_code:
    pprint({'url.status_code:': url.status_code})
if url.text:
    print(url.text)
    # print("\n")
if url.json():
    pprint(url.json())
#initialize:
url_variable = url.json()
pprint(dir(url_variable))
pprint(dict(url_variable.items()))
