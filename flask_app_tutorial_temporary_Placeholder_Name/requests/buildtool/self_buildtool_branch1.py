import os
import shutil

from pprint import pprint

printLines = os.listdir("../development")
pprint(printLines)

for elem in printLines:
    if os.path.isfile(f"../development/{elem}"):
        if elem != '.gitignore' and elem != 'shelf_d':
            with open(f"../development/{elem}", "r") as file:
                print(f"{elem}")
                elements = file.readlines()
                print(elements) #prints contents of each file
                if len(elements)>0:
                    if "#!" not in elements[0][:2]:
                        print("None")
                        # shutil.copy(f"../development/{elem}", f"../build/{elem}")
                    else:
                        with open(f"../build/{elem}", "w") as inner_file:
                            pass
                            # inner_file.write
                        print("exists.")
                else:
                    pass #pass means file was blank
            print(" ")
        else:
            continue
    else:
        continue
shutil.copy(f"../development/app.py", f"../build/")