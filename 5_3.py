def getBit(n, j):
	return (n >> j) & 1

def setBit(n, j, b):
	if b:
		return n | (1 << j)
	else:
		#set jth bit to true
		ret = (n >> j+1) << (j+1)
		right = (1 << j) - 1
		mask = ret | right

		return (n & mask)
		

def getPrevious(n):
	#find first occurence of 0
	x = n
	i = 0
	while getBit(n, i):
		i += 1

	#find next 1
	countzeros = 0
	while not getBit(n, i):
		i += 1
		countzeros += 1

	print i, countzeros

	#set ith position equal to 0 and and set position directly to right to 1
	x = setBit(x, i, 0)
	x = setBit(x, i-1, 1)

	for k in range(i-2, countzeros-1, -1):
		x = setBit(x, k, 1)
	
	for k in range(countzeros-1, -1, -1):
		x = setBit(x, k, 0)

	return x

def getNext(n):
	x = n
	#find first occurence of 1
	i = 0
	while not getBit(n, i):
		i += 1

	countones = 0
	j = i
	#find first zero after found 1
	while getBit(n, j):
		j += 1
		countones += 1

	#set jth bit equal to 0
	#set j+1th bit equal to 1
	x = setBit(x, j, 0)
	x = setBit(x, j+1, 1)
	
	#move 1s all the way to the right
	for k in range(j-1, countones-1, -1):
		x = setBit(x, k, 0)
	
	for k in range(countones-1, -1, -1):
		x = setBit(x, k, 1)

	return x




n = 5 #binary = 101
print getPrevious(n) # = 3 (11)
print getNext(n) # = 6 (110)


n = 1 << 10
n += 1

m = 1 << 10
m += 2

print getPrevious(m)
print n
