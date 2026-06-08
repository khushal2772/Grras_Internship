coordinates = (10, 20)
print(coordinates)
#coordinates[0] = 50 #nat doable because it is inmutable

l1 = list(coordinates)
l1[0] = 50
print(l1)

coordinates = tuple(l1)
print(coordinates)

