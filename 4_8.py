import binarytree

def findSum(head, s, q):
	# recursive definition
	if head is None:
		return None
	temp = 0
	q.append(head.key)
	# check if current buffer adds to sum
	for i in range(len(q)-1, -1, -1):
		temp += q[i]
		if temp == s: 
			printBuffer(q, i)

	c1 = q[:]
	c2 = q[:]

	findSum(head.left, s, c1)
	findSum(head.right, s, c2)

def printBuffer(q, level):
	for i in range(level, len(q), 1):
		print str(q[i]) + " "
	print ""

temp1 = binarytree.Node(4)
temp2 = binarytree.Node(6)
temp3 = binarytree.Node(7)
temp4 = binarytree.Node(10)
temp5 = binarytree.Node(2)

temp5.left = temp3
temp5.right = temp4
temp3.left = temp1
temp3.right = temp2
T = binarytree.BinaryTree(temp5)

#a = [1,2,3,4,5]
q = []
#T = binarytree.BinaryTree(insertkeylist = a)
T.printTree()
print ""

findSum(T.head, 13, q)
		
