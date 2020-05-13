
import random
import math

#There is no need to generate one uniform permutation by firstly generating all the permutation
def genUniformPermu(dimension):
	total = math.factorial(dimension)
	# uni = random.randint(1,total) if using offline method, how large would the storage table to be?
	permu = [ x+1 for x in range(dimension)]

	permu1 = []

	for i in range(dimension):
		sel = random.randint(0,dimension-i-1)
		permu1.append(permu[sel])
		del permu[sel]

	return permu1

def addPermutation(p1,p2):
	result=[]
	for i in range(len(p1)):
		result.append(p1[p2[i]-1])
	return result

def reversePermutation(p):#it's being very easy to calculate a reversed permutation
	rp=[x+1 for x in range(len(p))]
	for i in range(len(p)):
		rp[p[i]-1]=i+1
	return rp


def permuList(array,p):
	permuted=array.copy()
	for i in range(len(p)):
		permuted[i]=array[p[i]-1]
	return permuted




#one step incremental

# def genFullPermu(dimension,order):
# 	ele = [x+1 for x in range(dimension)]
#using bubble sort,then one by one change the list state
# 	permuted = ele.copy()
# 	for i in range(order):#we only do one interchange
# 		mid = 
# 		ele

# It's being very fast to generate one uniform permutation

# print(genUniformPermu(10000))

#commutative property of permutation 
#two permutation \pi_1 \pi_2 results into two 

# orig = ["I","am","the","truth","and","path"]

# permu1 = genUniformPermu(len(orig))
# permu2 = genUniformPermu(len(orig))

# r1 = reversePermutation(permu1)
# r2 = reversePermutation(permu2)

# add1 = addPermutation(permu1,permu2)
# add2 = addPermutation(permu2,permu1)

# add1_r1=addPermutation(add1,r1)
# add2_r1=addPermutation(add2,r1)

# print(addPermutation(add1_r1,r2))
# print(addPermutation(add2_r1,r2))
# print("__________")

# print(permuList(orig,r1))


##this uses massive space storaging duplicate elements
##Simple implementation, but high space consumption
def iteratelyGenPermu(length):
	if length < 2:
		return [[length]]
	else:
		preFull = iteratelyGenPermu(length-1)
		full =[]
		for pre in preFull:
			for i in range(length):
				newPre = pre.copy()
				newPre.insert(i,length)
				full.append(newPre)
		return full

#iteratelyGenPermu(11)

#using lexicographic approach to achieve permutation one by one
#low space complexity,high timing complexity
def genPermuOneByOne(length,order):
	cur = [x+1 for x in range(length)]
	print(cur)

	for i in range(order):
		for j in range(length-1):
			b_index = length-2-j
			# print(b_index)
			if cur[b_index] < cur[b_index+1]:
				swap1 = cur[b_index]
				findSwap2Index=length-1
				while(cur[findSwap2Index]<swap1):
					findSwap2Index-=1
				swap2 = cur[findSwap2Index]
				temp = []
				if b_index-1 >=0:
					temp=[x for x in cur[:b_index]]
				temp.append(swap2)
				cur[findSwap2Index]=swap1
				for k in range(length-1-b_index):
					backIndex = length-1-k
					temp.append(cur[backIndex])
				cur = temp
				print(temp)
				break
	return cur

# genPermuOneByOne(10,math.factorial(10)-1)
# genPermuOneByOne(4,23)

# origi = [3,2,1]
origi = [2,3,4,1]
next_ = origi.copy()
for i in range(24):
	print(next_)
	next_ = addPermutation(next_,origi)










