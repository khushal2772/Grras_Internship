def greater_than_9(x):
    if x>9:
        return True
    else:
        return False
def less_than_9(x):
    if x>9:
        return False
    else:
        return True
    
a = [21,5,3,756,856,12,4,5,643,6,45,7,]

greater = filter(greater_than_9, a)

print(list(greater))

leser = filter(less_than_9, a)

print(list(leser))

less = list(filter(lambda x: x<9 , a))