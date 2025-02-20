import requests
from pprint import pprint, pformat
import json
import os
import shelve

#open-a-shelf-file
shelf_d = shelve.open("shelf_d")
user_data = {
    'userString': 'abXYZ',
    'userBool': True,
    'userNumber': "0.83"
}

shelf_d["user_data"] = user_data
shelf_d.close()
#initialize:
#open-shelf-file

with shelve.open("shelf_d") as shelf_d:
    fileValue = shelf_d["user_data"]
print("fileValue:", fileValue)

#did-it_extract: 
jsonValue = json.dumps(fileValue)
print('fileValue:', jsonValue)

with open("prelim.txt", "w") as fileJson:
    fileJson.write(jsonValue)

response = requests.post("https://httpbin.org/post", json=fileValue, headers={'User-Agent':'myBotAuto: v1.0.0'})

#write to file:
fileName = "openText.py"
writeOrAppendMode = "w"
if os.path.isfile(f"./{fileName}"):
    pass
else:
    fileObject = open(fileName, "w")
    fileObject.close()
with open(fileName, writeOrAppendMode) as fileObject:
    # fileObject.write(response.json())
    fileObject.write(pformat(response.json()))



def if_run():
    print("if_run-function runs_")
    if response.status_code:
        pprint({'response.status_code:': response.status_code})
    if response.text:
        print(f"response-text:\n{response.text}")
        with open("response_text.txt", "w") as fileJson:
            fileJson.write(pformat(response.text))
        # print("\n")
        a = True
    if response.json():
        pprint(response.json())
        response_json_variable = response.json()
        b = True
    if a and b:
        with shelve.open("response_shelf") as response_shelf:
            response_shelf["response_Text"] = response.text
            response_shelf['response_Json'] = response_json_variable

if_run()
#initialize:
response_variable = response.json()
# pprint(dir(response_variable))
# pprint(dict(response_variable.items()))

with shelve.open('shelf_d') as shelveItem:
    extract_my_shelf_data = shelveItem['user_data']

print("extract_my_shelf_data:")
pprint(extract_my_shelf_data)