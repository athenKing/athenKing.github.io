import os
import shutil
import sys

directory = sys.argv[1]

cnt = 0
limit = 500
fileNames=[]

originalPrefix = os.getcwd() + "/" + directory + "/"
prefix = os.getcwd() + "/" + directory+"_"

for filename in os.listdir(originalPrefix):
    fileNames.append(filename)

subdirs=[]
for file in fileNames:
    subIndex = int(cnt/limit)
    cnt += 1
    finalDir = prefix+str(subIndex)

    if finalDir not in subdirs:
        print("new direcotry: ",finalDir)
        subdirs.append(finalDir)
    
    if not os.path.exists(finalDir):
        os.makedirs(finalDir)
    finalDir = finalDir + "/" + file
    shutil.move(originalPrefix+file,finalDir)

## move sub directory to original direcotry
for sub in subdirs:
    print("move direcotry: ", sub)
    shutil.move(sub,originalPrefix)
