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
#1.Input a directory name 
#2.Output contained pdfs into a dest directory

directory = sys.argv[1]

des = "/Users/athenking/Desketop/all_pdfs/"

if not os.path.exists(des):
    os.makedirs(des)

moveList=[]

# hashSet = set()

originalPrefix = os.getcwd() + "/" + directory + "/"
# prefix = os.getcwd() + "/" + directory+"_"

for filename in os.listdir(originalPrefix):
    if filename.endswith(".pdf") or filename.endswith(".PDF") :
        moveList.append(filename)

for f in moveList:
    print("moving: ",f)
    shutil.move(originalPrefix+f,des+f)


