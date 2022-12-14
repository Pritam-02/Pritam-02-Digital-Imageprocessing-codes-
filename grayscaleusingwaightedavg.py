import cv2
import numpy as np

def grey(im):
    h,w,c=im.shape
    gim=np.zeros([h,w])
    gim=gim.astype(np.uint8)
    for i in range(h):
        for j in range(w):
            gim[i][j]=0.3*im[i][j][2]+0.59*im[i][j][1]+0.1*im[i][j][0]
    
    return gim


im=cv2.imread('2.jpg')
cv2.imshow('imagedisplay',im)
ans=grey(im)
cv2.imshow('imagedisplay',ans)
