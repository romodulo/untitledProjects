import os
import shutil

from pprint import pprint

directory_path = "ignored"
printFileNames = os.listdir(f"../{directory_path}")
pprint(printFileNames)
namesUsedInPast = [
    "build"
]
distination_of_built_files = "build_ignored"
#check if :dir: exists
if not os.path.exists(f"../{distination_of_built_files}/"):
    os.mkdir(f"../{distination_of_built_files}/")

for elem in printFileNames:
    if elem == "app.py":
        with open (f"../{directory_path}/{elem}", "r") as file:
            file_readlines = file.readlines()
        shallow_file_readlines = file_readlines[:]
        index_count = 0
        while index_count < 5:
            if file_readlines[0].startswith("#!") or file_readlines[0].startswith("#"):
                file_readlines.pop(0)
            elif file_readlines[0].isspace():
                file_readlines.pop(0)
            index_count += 1
        shutil.copy(f"../{directory_path}/{elem}", f"../{distination_of_built_files}/")
        with open (f"../{distination_of_built_files}/{elem}", "w") as file:
            for i in file_readlines:
                file.write(i)
    else:
        shutil.copy(f"../{directory_path}/{elem}", f"../{distination_of_built_files}/")

print("file_readlines:")
pprint(file_readlines)