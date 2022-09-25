import numpy as np
import matplotlib.pyplot as plt

#Dataset
gamma=np.arange(0,1,0.1)
c=1.5
x=np.arange(0,256,0.1)
print(x)

for i in range(len(gamma)):
    y=c*x*gamma[i]
    #plotting the graph
    plt.plot(x,y)

plt.title("gamma curve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()