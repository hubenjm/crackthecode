class SinglyLinkedNode():
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data
	def setData(self, new_data):
		self.data = new_data
	def getNext(self):
		return self.next
	def setNext(self, node):
		self.next = node

class DoublyLinkedNode():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None
	def setNext(self, newnext):
		self.next = newnext
	def setPrevious(self, newprevious):
		self.previous = newprevious
	def getNext(self):
		return self.next
	def getPrevious(self):
		return self.previous
	def getData(self):
		return self.data
	def setData(self, newdata):
		self.data = newdata

class SinglyLinkedList():
	def __init__(self, head = None):
		self.head = head

	def add(self, data):
		node = SinglyLinkedNode(data)
		node.next = self.head
		self.head = node
		
	def __repr__(self):
		s = ""
		runner = self.head
		while runner is not None:
			s += str(runner.data) + ", "
			runner = runner.next

		return s[:-2]
		
	
class DoublyLinkedList():
	def __init__(self, head = None):
		self.head = head
