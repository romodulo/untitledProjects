import shelve
from pprint import pprint, pformat
import json

#opens-response
with shelve.open("response_shelf") as response_shelf:
    data = response_shelf['response_Text']
    data_json = response_shelf['response_Json']
#opens-self-generated-user-data
with shelve.open("shelf_d") as shelf_d:
    user_data = shelf_d["user_data"]

# pprint(user_data) #it doesn't print
#in console as intended
#but file retains original order of dictionary serialized
display_user_data = json.dumps(user_data)
pprint(display_user_data.split(",")) #it will be better to transform json to python format and display it in python format
#load json string
load_json_string = json.loads(display_user_data)
json_python_dictionairy = load_json_string
print("json_python_dictionairy:")
pprint(json_python_dictionairy)
with open("load_json_to_python_dictionariy.txt", "w") as modifyfile:
    modifyfile.write(str(json_python_dictionairy))
with open("load_json_to_python_dictionariy.txt", "r") as modifyfile:
    all_lines = modifyfile.readlines()
    #skip-for-now
#work-with---the loaded python dictionairy sourced from a json string
keys = json_python_dictionairy.keys()
print(keys)
for i in keys:
    print("keys:", i)
#test-items:
items = json_python_dictionairy.items()
print(items)
#variables
algorithmicString = ""
keep_count_of_highest_String = 0
#
#constants
string_of_word_keys = "keys"
string_of_word_values = "values"
#
for k, v in items:
    lenOfK = len(str(k))
    lenOfV = len(str(v))
    if lenOfK > keep_count_of_highest_String:
        keep_count_of_highest_String= lenOfK
    if lenOfV > keep_count_of_highest_String:
        keep_count_of_highest_String = lenOfV
    len_string_of_word_keys = len(string_of_word_keys)
    len_string_of_word_values = len(string_of_word_values)
    if len_string_of_word_keys > keep_count_of_highest_String:
        keep_count_of_highest_String = len_string_of_word_keys
    if len_string_of_word_values > keep_count_of_highest_String:
        keep_count_of_highest_String = len_string_of_word_values
    # print("types:", type(str(k)))
    # print("types:", type(str(v)))
print("keep-count-hights", keep_count_of_highest_String)
highest_count = keep_count_of_highest_String
buffer = round(highest_count/2)
buffer = buffer - round(buffer/2)
for k, v in items:
    a = string_of_word_keys
    b = str(k)
    c = string_of_word_values
    d = str(v)
    string_join = [a.ljust(highest_count + buffer), b.ljust(highest_count + buffer), c.ljust(highest_count + buffer), d.ljust(highest_count + buffer)]
    algorithmicString = "".join([algorithmicString] + string_join + ["\n"])

with open("test_data_integer.txt", "w") as dataFile:
    dataFile.write(algorithmicString)

with open("user_data_text.txt", "w") as modifyfile:
    json.dump(user_data, modifyfile, indent=4)

#   ###continue from here ###

with open("response_json_2.txt", "w") as modifyfile:
    modifyfile.write(pformat(data_json))

with open("response_json_2.json", "w") as modifyfile:
    modifyfile.write(pformat(data_json))

# print((pformat(data_json)))