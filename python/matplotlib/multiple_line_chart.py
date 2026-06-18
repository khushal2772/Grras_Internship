import matplotlib.pyplot as plt

x = [2010,2015,2020,2025]
y1= [100,200,260,290]
y2 = [150,185,195,300]

# plt.plot(x,y1, label="jeans")
# plt.plot(x,y2,label="shirt")
# plt. legend() # info of label
# plt.show()


subjects = ["Math", "Science", "English", "Computer"]
student1 = [80, 75, 90, 85]
student2 = [70, 85, 88, 80]

plt.plot(subjects, student1, label="Student 1")
plt.plot(subjects, student2, label="Student 2")

plt.title("Student Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()

plt.plot(subjects, student1, marker="o", label="Student 1")
plt.plot(subjects, student2, linestyle="--", label="Student 2")
plt.grid(True)
plt.show()
