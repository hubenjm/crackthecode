def updateBits(N, M, i, j):
	#set all bits of N between positions i and j equal to M
	#i <= j
	ret = (1 << i) - 1 #1's in slots 0 through i-1
	ret &= N 
	#first term below creates int matching N up to j+1th position, and 0's following (i.e. clears out everything from where M needs to appear until end of number
	#second term below creates int which shifts M to start at ith position and go until jth position
	#the first | operator replaces positions j through i of the first int with the shifted version of M
	#the last | operator puts bit positions i-1 through 0 of N back into place
	return (( (N >> (j+1)) << (j+1) ) | (M << i)) | ret

def updateBits2(N, M, i, j):
	maxint = (1 << 36) - 1
	left = maxint - ((1 << j) - 1)
	right = ((1 << i) - 1)

	mask = left | right
	return (N & mask) | (M << i)

def printBits(n):
	x = n
	for j in range(n.bit_length()-1, -1, -1):
		print (n >> j) & 1,

	print ""

N = 1 << 10
M = 21
i = 2
j = 6

printBits(updateBits(N, M, i, j))
printBits(updateBits2(N, M, i, j))
