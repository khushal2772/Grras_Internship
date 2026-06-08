num = [1,2,3,4,5]

def found(x,a=4):
    if(a == x):
        return True

def square(x):
    return x*x

new = list(map(square, num))
print(new)

n = list(map(found, num))
print(n)

# print(map(found,4,num))