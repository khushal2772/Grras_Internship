import math
import requests
import time

# def factorial(n):
#     if n == 0 || n == 1:
#         return 1
#     return n * factorial(n-1)

# a = int(input("Enter the no that you want to find factorial"))

# print(factorial(a))

# def greet():
#     return "Hello Python Programmer!"

# def square(n):
#     return n*n

# def full_name(a, b):
#     global name 
#     name = a+" "+b

# a ='khushal'
# b = 'singh'
# full_name(a, b)
# print(name.title())

# def calculate_area(length, breadth = 10):
#     return length*breadth

# a = lambda a,b: a+b

# x = [1, 2, 3, 4, 5]

# square = lambda  x: x**2
# s = list(map(square, x))
# print(s)

# def sum_of_digits(n):
#     if n==0:
#         return 0
#     return n%10 + sum_of_digits(n//10)

# print(sum_of_digits(5))

# print(math.sqrt(144))
# print(math.sin(math.radians(90)))


url = 'https://api.github.com/'
r = requests.get(url)
print(r.status_code)
if r.status_code == 200:
    print(r.json())
else:
    print('Error')
    
# for i in range(5):
#     r = requests.get(url)
#     print(r.status_code)
#     time.sleep(2)   # wait 2 seconds
#     print(time.ctime())
#     t = time.localtime()
#     print(time.strftime('%y-%m-%d  %H:%M:%S', t))

for i in range(1, 5):
    for j in range(1, i+1):
        print(2*j-1, end=" ")
    print()