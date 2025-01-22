#openFile-1:
openFile = open(".gitignore", "r")
m = openFile.read()

#openFile-2:
outFile = open("new.txt", "w")
nueList  = []
nue_m = m.split("\n")
print('nue_m type', "|", type(nue_m)) #nue_m type | <class 'list'>
for index, i in enumerate(nue_m):
    print(index, "|", i)
#process:
nue_m_sorted = sorted(nue_m, key=str.lower)
for index, i in enumerate(nue_m_sorted):
    print(index, "|", i)
#check if 
if nue_m_sorted[0] == "*.pyc":
    savedRemoved = nue_m_sorted.pop(0)
    print("popped!", savedRemoved)
    nue_m_sorted.append(savedRemoved)
nue_m_joined = "\n".join(nue_m_sorted)
outFile.write(nue_m_joined)
#reProcess:
for index, i in enumerate(nue_m_sorted):
    print(index, "|", i)
#close files:
outFile.close()
openFile.close()