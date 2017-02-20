class Node():
	def __init__(self, key = None):
		self.key = key
		self.left = None
		self.right = None

class BinaryTree():
	def __init__(self, head = None, insertkeylist = None):
		self.head = head
		if insertkeylist is not None:
			for key in insertkeylist:
				self.insert(key)

		
	def insert(self, key):
		if self.head is None:
			self.head = Node(key)
		else:
			self.insertBelow(key, self.head)

	def insertBelow(self, key, currentnode):
		if key < currentnode.key:
			if currentnode.left is not None:
				self.insertBelow(key, currentnode.left)
			else:
				currentnode.left = Node(key)
		
		else:
			if currentnode.right is not None:
				self.insertBelow(key, currentnode.right)
			else:
				currentnode.right = Node(key)

	def printTree(self):
		#print out tree as list in breadth search order
		printSubtree(self.head)
		

def printSubtree(node):
	if node is not None:
		if node.left is not None:
			printSubtree(node.left)
		print(node.key)
		if node.right is not None:
			printSubtree(node.right)


	
					
