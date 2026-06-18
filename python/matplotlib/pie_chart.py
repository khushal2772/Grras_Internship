import matplotlib.pyplot as plt
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