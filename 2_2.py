import linkedlist

def nthtolast(L, n):
	# non-recursively
	# march first runner to nth item from head
	# if None is encountered at any point return None
	# start second runner at head once first runner reaches nth item
	# now increment both runners in tandem until first runner reaches None

	if L.head is None:
		return None

	first_runner = L.head
	for counter in range(1,n):
		counter += 1
		first_runner = first_runner.next
		if first_runner is None:
			return None
	
	second_runner = L.head
	while True:
		if first_runner.next is None:
			return second_runner.data
		
		first_runner = first_runner.next
		second_runner = second_runner.next

L = linkedlist.SinglyLinkedList()
s = [1,4,2,5,3,2,6,4,3,2,1]
for item in s:
	L.add(item)

print L

print nthtolast(L, 5)
	
