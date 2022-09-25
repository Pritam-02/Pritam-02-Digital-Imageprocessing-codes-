import cv2
import numpy as np
import matplotlib.pyplot as plt

def imageNev(im):
    h,w=im.shape
    newIm=np.zeros([h,w]).astype(np.uint8)
    #newIm=new
    for i in range(h):
        for j in range(w):
            newIm[i][j]=255-im[i][j]
    return(newIm)


def imagechannels(im):
    h,w,c=im.shape
    rIm=np.zeros([h,w]).astype(np.uint8)
    gIm=np.zeros([h,w]).astype(np.uint8)
    bIm=np.zeros([h,w]).astype(np.uint8)
    #newIm=new
    for i in range(h):
        for j in range(w):
            rIm[i][j]=im[i][j][2]
            gIm[i][j]=im[i][j][1]
            bIm[i][j]=im[i][j][0]
    return rIm, gIm, bIm

im1=cv2.imread('2.jpg',1)
im2=cv2.imread('2.jpg',0)
im3=imageNev(im2)
im4, im5, im6=imagechannels(im1)


fig, axs=plt.subplots(2,3)

axs[0,0].imshow(im1)
axs[0,0].set_title('RGB Image')
axs[0,1].imshow(im2,cmap='gray')
axs[0,1].set_title('Gray Image')
axs[0,2].imshow(im3)
axs[0,2].set_title('Negative Image')

axs[1,0].imshow(im4)
axs[1,0].set_title('Red Image')
axs[1,1].imshow(im5)
axs[1,1].set_title('Green Image')
axs[1,2].imshow(im6)
axs[1,2].set_title('Blue Image')

plt.waitforbuttonpress()

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')