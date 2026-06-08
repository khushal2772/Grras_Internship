# average of 3 no.

a = 5
b = 3
c = 8

def average(a, b, c):
    result = (a + b + c)/3
    print(result)

average(a,b,c)

average(a=5,b=4,c=6) #pass arg also like this


square = lambda x: x*x
print(square(4))

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

print(type(numbers))