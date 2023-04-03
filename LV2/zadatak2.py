import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
print(np.shape(data))
x =data[:,0]
y =data[:,3]
weight=data[:,5]
plt.scatter(y,x, weight)
plt.xlabel("hp")
plt.ylabel("mpg")
plt.show()