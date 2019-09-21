import os
import shutil
import sys
import hashlib
import mmh3
import time

file = sys.argv[1]


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

t1 = time.time()
print( mmh3.hash(file) )
t2 = time.time()
print("mmh3 using: ",t2-t1)


print( md5(file) )
print( len(md5(file)) )
t3 = time.time()
print("md5 using: ",t3-t2)

print((t3-t2)/(t2-t1))

