import numpy as np
import matplotlib.pyplot as plt

#Dataset
c=np.arange(0,10,1)
x=np.arange(0,256,0.1) #start stop step
print(x)

for i in range(len(c)):
    y=c[i]*np.log(1+x)
    #plotting the garph 
    plt.plot(x,y)

plt.title("log curve with varying c values")
plt.xlabel("x")
plt.ylabel("y")
plt.show()