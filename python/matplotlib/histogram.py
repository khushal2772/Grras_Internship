import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# plt.hist(marks)
# plt.show()

# plt.hist(marks, bins=5)
# plt.show()

# plt.hist(marks, bins=5, edgecolor="black")
# plt.show()

plt.hist(marks, bins=5, range=(70, 100))
plt.show()

plt.hist(marks, bins=5, alpha=0.5)  # transparency 0 to 1
plt.show()