#! /home/romel-linux/untitledProjects/.myenv_main/bin/python
# renamebackupCopy.py is aptly named because the program
# takes in a file called "routerVideoBackups" as one its
# inputs as a program. 
#

#import shutil
import shutil
import os
from pprint import pprint

#create a dirname
currentFile = "/home/romel-linux/untitledProjects/renameProject/renamebackupCopy.py"
dirName = os.path.dirname(currentFile)
print('dirName:', dirName)
baseName = os.path.basename(currentFile)
print('baseName:', baseName)
siblingFolder = "emptyString_For_Now___"
print('siblingFolder:', siblingFolder)
helperList = "ModifiedpendingString.txt"
joinedPath = os.path.join(dirName, siblingFolder, helperList)

# get current W. Dir:
currentWDir = os.getcwd()
print("currentWDir:", currentWDir)

#directory of target file:
#~/Videos/routerVideosBackup

#
#home directory:
homeDir = '/home/romel-linux/'
videosDir = 'Videos'
routerBackup = 'routerVideosBackup'

#
#join path:
newPath = os.path.join(homeDir, videosDir, routerBackup)
print("newPath:", newPath)

#
#get list of files:
newList = os.listdir(newPath)
pprint({"newList": newList})
print(len(newList))

#
#create new dicts'?

#
#check if file exists
modifiedList = os.path.join(dirName, "copyModifiedpendingString.txt")
checkIfFileExists = os.path.exists(modifiedList)
if checkIfFileExists:
    FileObject = open(modifiedList)
    FileObjectReturn = FileObject.read()
    FileObject.close()
else:
    print("s", "False")
    pass
# pprint({'FileObjectReturn': FileObjectReturn.split("\n")[:len(FileObjectReturn.split("\n"))-1]}) #this works
def process_list(a):
    listPopped = a.split("\n") #if a=FileObjectReturn
    poppedSE = listPopped.pop() #SE stands for shift end
    return listPopped
    # reverse()
def process_another_thing():
    result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]
    pprint(result[0:50])
    return result
# process_list(FileObjectReturn) #no need for this line of TEST right now. 
# process_another_thing() #do not run yet, i think.
pprint({'FileObjectReturn': process_list(FileObjectReturn)})
print(len(process_list(FileObjectReturn)))

#
#process a new list
processNL = process_list(FileObjectReturn)
pprint({"processNL:": processNL})
#
#check if list1 is equal to list2
# create an Empty New List
if len(newList) == len(processNL):
    emptyNewList = []
    eNL = emptyNewList
    #create a new dir
    if not os.path.exists(os.path.join(homeDir, videosDir, "newFolderForModifys")):
        os.makedirs(os.path.join(homeDir, videosDir, "newFolderForModifys"))
    else:
        pass
    #newlyCreatedPath path
    newlyCreatedPath = os.path.join(homeDir, videosDir, "newFolderForModifys")
    #if newlyCreatedPath has any contents: remove contents
    if len(os.listdir(newlyCreatedPath)) > 0:
        import send2trash
        for itemOfList in os.listdir(newlyCreatedPath):
            temporaryPath = os.path.join(newlyCreatedPath, itemOfList)
            send2trash.send2trash(temporaryPath)
    print("print(os.listdir(newlyCreatedPath)):", len(os.listdir(newlyCreatedPath)))
    #sort these lists:
    #only newList needs to be sorted
    newList = sorted(newList)
    for i in range(len(newList)):
        processedName = f'{newList[i].removesuffix(".mp4")} | {processNL[i]}.mp4'
        print("processedName:", processedName)
        eNL.append(processedName)
        #mv files?
        #mv {dirName}newList[i] {dirName}processedName
        #path-join for better interopability
        #moveFromFile = os.path.join(dirName, newList[i])
        #moveToFile = os.path.join(dirName, processName)
        #is the move completed?
        #steps 1-?:
        sourceDoc = os.path.join(newPath, newList[i])
        targetDoc = os.path.join(newlyCreatedPath, processedName)
        # # # crucial step:# # #
        # # #              # # #
        # # # irreversible step added and removed previous step:# # #
        shutil.move(sourceDoc, targetDoc)
# read the contents of the new folder:
#in targetDoc
newListAppended = os.listdir(newlyCreatedPath)
newListAppended.sort()
pprint({"Directory: newFolderForModifys": newListAppended})
pprint(newListAppended)

#
#all i need to do is check my files to be committed
# if there are any cache files...


def adjusting(): #deprecated_stuff
    #for reference    
    variableI = sorted(os.listdir(variableH))
    print('variableI: is listdir(variableH) #sorted')
    # print("variableI: ")  #part of pprint example
    # pprint(variableI)#sorts #successfully  #pprint example

    #i imported send2trash at one point
    # import send2trash

    #at one point I created print statements
    #to understand what paths I'm working with.
    print("path EXistS-2")

    #test open file

    #
    #successfully reviewed deprecated code.

def project_ran_successfully():
    print('project ran successfully')

project_ran_successfully()