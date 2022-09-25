import cv2
import numpy as np
import matplotlib.pyplot as plt

#Dataset
c=1
x=np.arange(0,256,0.1)
print(x)
y=c*np.log(1+x)
print(y)

#plotting the garph
plt.plot(x,y)
plt.title("log curve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()