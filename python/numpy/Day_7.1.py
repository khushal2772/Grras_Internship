import numpy as np

# 1D list
l1 = [1,2,3]

# 1D array
arr1 = np.array(l1)

# 2D list
l = [
    [1,2,3],
    [4,5,6]
]

# 2D array
arr = np.array([
    [1,2,3],
    [4,5,6]
])


#Questions:

# change 4 to 100 in list
l[1][0] = 100
print(l)

# change 4 to 100 in array
arr[1][0] = 100
print(arr)

#list
lm = l1*2
print(lm)

#array
ar = arr1*2
print(ar)

#zeros arr
arr = np.zeros(5)
print(arr)

arr = np.zeros((3,4))
print(arr)