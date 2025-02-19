from pprint import pprint
import shelve
import json

s_file = shelve.open('shelf_d')
pprint(list(s_file.keys()))
input_var = input("type-anything-here: ")
opened_file = s_file[input_var]
print(type(opened_file))
print(opened_file)
print(json.dumps(opened_file))

s_file.close()

#note-from-the-documentation:
#d=shelve.open(filename, writeback=True)
#will allow:
#d['xx'].append(data) as expected. 