s1 = {4, 5,"khushal", 2, 8}
s2 = {4, 6, 1, 8, 45}
print(type(s1))
print(len(s1))
e = set()  # empty set
print(type(e))

a = s1.remove(2)
s2.remove(45)
s1.discard(6) # remove if it is present in set 
print(a)
print(s1.union(s2))  # all elements of both set present

print(s1.intersection(s2)) # same elements is presrnt in this

print(s1.issubset(s2)) #subset of s2 in s1

print(s1.difference(s2))  #elements that is not present in s2
e.add(27)
e.add('27')
print(e)