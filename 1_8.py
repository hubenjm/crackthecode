def isRotation(s1, s2):
	t  = s1 + s1
	return s2 in t

s1 = "waterbottle"
s2 = "erbottlewat"

print isRotation(s1, s2)

s1 = "hello"
s2 = "ello h"

print isRotation(s1, s2)
