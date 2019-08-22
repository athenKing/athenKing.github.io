import os
import shutil
import sys
import hashlib

def md5(fileName):
    """Compute md5 hash of the specified file"""
    m = hashlib.md5()
    try:
        fd = open(fileName,"rb")
    except IOError:
        print ("Reading file has problem:", filename)
        return
    x = fd.read()
    fd.close()
    m.update(x)
    return m.hexdigest()

#Features:
#1.remove all the aae data
#2.check if there exists duplicate photo

directory = sys.argv[1]

remove_cnt = 0
# limit = 500
fileNames=[]
removeList=[]

hashSet = set()

originalPrefix = os.getcwd() + "/" + directory + "/"
prefix = os.getcwd() + "/" + directory+"_"


for filename in os.listdir(originalPrefix):
    if filename.endswith(".AAE") or filename.endswith(".aae") :
        removeList.append(originalPrefix+filename)
    else:
        fileNames.append(originalPrefix+filename)

for r in removeList:
    print("delete: ",r)
    os.remove(r)

for f in fileNames:
    val = md5(f)
    if val in hashSet:
        print("delete duplicate file: ",f)
        os.remove(f)
    else:
        hashSet.add(val)