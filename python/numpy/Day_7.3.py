import numpy as np

# flattern() -- create copy and then works

# 2D
'''arr = np.arange(12).reshape(3,4)
print(arr)
arr1 = arr.flatten()
print(arr1)'''

# 3D
'''arr = np.arange(24).reshape(4,2,3)
print(arr)
arr1 = arr.flatten()
print(arr1)'''

# reval() -- it works on original array

# 2D
'''arr = np.arange(15).reshape(3,5)
print(arr)
arr1 = arr.ravel()
arr1[0] = 200
print(arr1)'''

# 3D
'''arr = np.arange(24).reshape(4,2,3)
print(arr)
arr1 = arr.ravel()
arr1[0] = 101
print(arr)
print(arr1)'''

# transpose -- convert rows to col && col to rows

# 2D
'''arr = np.arange(12).reshape(3,4)
print(arr,'\n')
arr1 = arr.T
print(arr1)'''

# slicing

# 1D
'''arr = np.arange(12)
print(arr)
uparr = arr[:3]
print(uparr)'''

# 2D
'''arr = np.arange(12).reshape(3,4)
print(arr)
uparr = arr[:2,:2] # [starting row : end row , col]
print(uparr)'''

# 3D
arr = np.arange(24).reshape(3,4,2)
print(arr)
# arr1 = arr[::2,::3,:]
uparr = [arr[0,0,0], arr[2, -1, -1]]
# print(arr1)
# print(arr[::2, ::3, ::1])