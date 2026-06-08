# def logger(func):
#     def wapper():
#         print("Function is called")
#         func()
#     return wapper

# @logger
# def say_hello():
#     print("Hello!")

# say_hello()


from time import time
def timer(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2 = time()
        print(t2-t1)
    return wrapper

@timer
def sum1(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

a = sum1(1000000)
print(a)