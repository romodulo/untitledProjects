#! /home/romel-linux/untitledProjects/.myenv_main/bin/python
#needed
import os
from pprint import pprint


#get cwd
cwd = os.getcwd()
# print(cwd)
fileToRead = cwd #does not get the path of the file to read. 

#set a filepath for this file
fileName = "/home/romel-linux/untitledProjects/renameProject/evenNumbersList/rawList.txt"
dirName = os.path.dirname(fileName)
print("dirname", dirName)
baseName = os.path.basename(fileName)
# fileName = os.path.join(DirName, BaseName)
# print(fileName)

#FileObjects:
#open and close:
FileObject = open(fileName, "r")
convertedStringToList = FileObject.read()
convertedStringToList = convertedStringToList.split("\n")
print(type(convertedStringToList))
pprint(convertedStringToList)
FileObject.close()
#variables taken from
#opening files:
#convertedStringToList
#
#variable: dirName
#os.path.join("String-1", "String-2")
fileToWriteFileName = "pendingString.txt"
fileToWrite = os.path.join(dirName, fileToWriteFileName)
if os.path.exists(fileToWrite):
    print("program-message: file exists, file being overwritten...")
else:
    print("program-message: file doesn't exist yet")
#process-New-File:
num = 3
print(f"convertedStringToList[{num}]", convertedStringToList[num])
print(5%2)
print(4%2)
#write to file:
FileObjectWrite = open(fileToWrite, "w")
count = 1
for index, i in enumerate(convertedStringToList):
    if index % 2 == 0:
        continue
    elif index % 2 != 0:
        if not count < 10:
            FileObjectWrite.write(f"{count} | {i}\n")
            count +=1
        else:
            FileObjectWrite.write(f"0{count} | {i}\n")
            count +=1
FileObjectWrite.close()

