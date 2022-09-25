import cv2
import numpy as np
import matplotlib.pyplot as plt

#Dataset
x=np.arange(0,256,1)
print(x)
y=255-x
print(y)

#plotting the garph
plt.plot(x,y)
plt.title("negative image graph")
plt.xlabel("x")
plt.ylabel("y")
plt.show()