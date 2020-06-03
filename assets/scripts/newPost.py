import shutil
import os
import sys
from datetime import datetime


now = datetime.now()

customName = now.strftime("%Y-%m-%d-")

customName += sys.argv[1]+".md"

src = os.getcwd()+"/template.md"

des = os.getcwd()+"/athenKing.github.io/_posts/"+customName

shutil.copy(src,des)

with open(des,'r') as file:
	data = file.readlines()

data[3]="date: "+now.strftime("%Y-%m-%d %H:%M:%S +0800\n")
data[2]="title: "+sys.argv[1]+"\n"

with open(des, 'w') as file:
    file.writelines( data )
