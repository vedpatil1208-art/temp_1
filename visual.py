import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,4,5,6])
y = x ** 2

uniform_dis = np.random.uniform(10, 20, 5)
normal_dis = np.random.normal(1, 5, 1)


plt.bar(uniform_dis, label="Uniform Distribution", height=0.5)
plt.title("Uniform Distribution")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.bar(normal_dis, label="Normal Distribution", height=0.5)
plt.title("Normal Distribution")
plt.legend()
plt.grid(True)
plt.bar(x,y)

plt.pie(x,y)
colors = ["red", "blue", "green", "yellow", "orange"]
labels = ["A", "B", "C", "D", "E"]
plt.pie(x, colors=colors, labels=labels)

plt.show()

