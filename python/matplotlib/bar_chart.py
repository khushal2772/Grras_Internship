import matplotlib.pyplot as plt
import numpy as np


# x = [2015,2020,2025,2030]
# y = [100,150,200,290]
 
# plt.bar(x,y)
# # size
# plt.figure(figsize=(6,2))
# plt.show()


x = np.array([1,2,3,4])
y1 = [10,20,20,40]
y2 = [20,30,25,30]
y3 = [15,25,35,45]
# calculation -> width
w = 0.20
plt.bar(x - w,y1 , label="boys",width=w) # hide second
plt.bar(x + w,y2, label="girls",width=w) # show
plt.bar(x ,y3, label="others",width=w)
 
plt.xlabel("groups")
plt.ylabel("number of students")
plt.title("Number of Students in Each group")
plt.legend()
plt.show()