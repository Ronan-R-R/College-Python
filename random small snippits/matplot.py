import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [9,8,7,6,5]

""" plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Our Line Graph") """

plt.pie(x,labels=y, autopct="%1.1f%%")
plt.show()