from functools import reduce
num = [1,2,3,4,5,6]
    # [3,3,4,5,6]
    # [6,4,5,6]
    # [10,5,6]
    # [15,6]
    # [21]

def sum (a,b):
    return a+b

x = reduce(sum, num)
print(x)

sum_of_numbers = reduce(lambda x, y: x + y, num)
print(sum_of_numbers)