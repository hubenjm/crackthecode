import linkedlist
import linkedlistutils

L = linkedlist.SinglyLinkedList()
s = [1,4,3,2,67,34,2,2,4,6,7,1]
for item in s:
	L.add(item)

print L

linkedlistutils.deleteDuplicates(L)

print L
