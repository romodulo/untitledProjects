import os
import shutil

from pprint import pprint

printLines = os.listdir("../development")
pprint(printLines)

for elem in printLines:
    shutil.copy(f"../development/{elem}", f"../build/")