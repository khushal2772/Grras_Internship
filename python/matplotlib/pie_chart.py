import matplotlib.pyplot as plt
import numpy as np
fruits = ['apple','banana','orange','watermelon']
count = [40,30,15,70]
# plt.pie(count, labels=fruits)
# plt.show()


data = [40, 30, 20, 10]
labels = ["A", "B", "C", "D"]

# plt.pie(data, labels=labels)
# plt.show()

# plt.pie(data, labels=labels, autopct="%1.1f%%")
# plt.show()

# plt.pie(data, labels=labels, startangle=90)
# plt.show()

explode = [0.1, 0, 0, 0]

plt.pie(data, labels=labels, explode=explode)
plt.show()

colors = ["red", "blue", "green", "yellow"]

# plt.pie(data, labels=labels, colors=colors)
# plt.show()



x = np.array([1, 2, 3, 4])
y = np.array([80, 75, 90, 85])

x_smooth = np.linspace(x.min(), x.max(), 100)
y_smooth = np.interp(x_smooth, x, y)   # smooth-ish interpolation

plt.plot(x_smooth, y_smooth)
plt.scatter(x, y)   # original points
plt.show()