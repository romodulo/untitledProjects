#modifies shelf_d <shelf file> and response_shelf
#<shelf file>

import json
import shelve
from pprint import pprint

with shelve.open("shelf_d") as shelfItem:
    user_data = shelfItem['user_data']
print("type:", type(user_data))
#load up my dict& convert to json
jsonDumps = json.dumps(user_data, sort_keys=False, indent=4)
pprint(jsonDumps) #pre-lim ::print::
with open("fileJson.txt", "w") as fileJson:
    fileJson.write(jsonDumps)

with shelve.open('response_shelf') as shelfItem:
    response_data = shelfItem['response_Json']
print("type:", type(response_data))