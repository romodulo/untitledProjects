import os
import shutil

from pprint import pprint

printLines = os.listdir("../development")
# pprint(printLines) #prints files in dir specified

for elem in printLines:
    # shutil.copy(f"../development/{elem}", f"../build/")
    if os.path.isfile(f"../development/{elem}"):
        if elem != '.gitignore' and elem != 'shelf_d':
            with open(f"../development/{elem}", "r") as file:
                print(f"{elem}")
                elements = file.readlines()
                # print(elements)
            if len(elements)>0:
                if "#!" not in elements[0][:2]:
                    #copy the elem
                    shutil.copy(f"../development/{elem}", f"../build/")
                    print("None")
                else:
                    # with open(f"../build/{elem}", "w") as inner_file:
                    #     pass
                        # inner_file.write
                    new_elements = elements[3:]
                    with open(f"../build/{elem}", "w") as fileOpen:
                        for element in new_elements:
                            fileOpen.write(element)
                    print("exists.")
            else:
                shutil.copy(f"../development/{elem}", f"../build/")
                print("blank_file") #file is blank
            print(" ")
        else:
            shutil.copy(f"../development/{elem}", f"../build/")
            print(f"{elem}")
            print("not a text based file.")
            print(" ")
    else:
        continue
