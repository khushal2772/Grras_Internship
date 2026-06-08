my_set = {1, 2, 3, 3, 4}
print(my_set)
my_set.add(5)
my_set.discard(2)
if 4 in my_set:
    print('Found')
else:
    print('not found')

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))