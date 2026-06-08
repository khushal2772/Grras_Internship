import numpy as np

# while loop

# 1D
'''arr = np.arange(12)
i=0
while(i<len(arr)):
    print(arr[i], end=" ")
    i += 1'''

# 2D
'''arr1 = np.arange(20).reshape(4,5)
len_i = len(arr1)
len_j = len(arr1[0])
i=0
while i < len_i:
    j=0
    while j < len_j:
        print(arr1[i][j], end=" ")
        j+=1
    i+=1'''

# 3D
'''arr2 = np.arange(27).reshape(3,3,3)
len_i = len(arr2)
len_j = len(arr2[0])
len_k = len(arr2[0][0])
i=0
while i < len_i:
    j=0
    while j < len_j:
        k=0
        while k < len_k:
            print(arr2[i][j][k], end=" ")
            k+=1
        j+=1
    i+=1'''

# for loop

# 1D
'''arr = np.arange(12)
for i in arr:
    print(arr[i], end=" ")'''

# 2D
'''arr1 = np.arange(20).reshape(4,5)
for i in arr1:
    for j in i:
        print(j, end=" ")'''
        
# 3D
arr2 = np.arange(27).reshape(3,3,3)
for i in arr2:
    # print(i)
    for j in i:
        # print(j)
        for k in j:
            print(k, end=" ")