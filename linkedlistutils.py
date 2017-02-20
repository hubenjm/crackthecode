import linkedlist

def deleteDuplicates(L):
	"""
	Parameters:
	tree : linkedlist.SinglyLinkedList

	Returns:
	None
	"""

	previous = L.head
	current = previous.next

	while current is not None:
		#initialize runner node to head of list
		#check no nodes have data equal to current.data
		runner = tree.head
		while runner != current:
			if runner.data == current.data:
				#remove current
				temp = current.next
				previous.next = temp
				current = temp
				break #all other duplicates have been removed

			runner = runner.next
		
		if runner == current:
			# no dupes were found in this case
			# so current needs to be updated
			previous = current
			current = current.next

	return None


				
