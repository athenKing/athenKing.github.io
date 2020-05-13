# import random

## The Flajolet Martin counting technique
import hashlib

# numCount = 1000000
numCount = 1000

hashResult=[]

fmString=[]

for i in range(128):
	fmString.append('0')


for i in range(numCount):
	m = hashlib.md5()
	m.update(str(i).encode('utf-8'))
	rho=0
	hex_ = m.hexdigest()
	for j in range(32):
		cur = hex_[31-j]
		cur = int(cur,16)
		if cur ==0:
			rho+=4
		while cur%2 ==0 and cur!=0:
			cur=cur/2
			rho+=1
		if cur%2==1:
			break
	if rho > 0:
		fmString[rho-1]='1'
	# print(hex_)##judge zero trail counting of the binary string
	# print(rho)


final=""
for v in fmString:
	final+=v

print(final)
# for i in range(genCount):


