import numpy as np
import cv2
def distance(x,y):
    return (np.sqrt(np.sum(np.square(x-y))))

img=cv2.imread("1.jpeg")

width=img.shape[1]
height=img.shape[0]

myimg=np.zeros([height,width,3])

white=np.array([255,255,255])
black=np.array([0,0,0])
gray=np.array([125,125,125])

for y in range(height-1):
    for x in range(width-1):
        current=img[y,x,:]
        right=img[y,x+1,:]
        bottom=img[y+1,x,:]

        if distance(current,right)>20 and distance(current,bottom)>20:
            myimg[y,x,:]=black
        elif distance(current,right)<20 and distance(current,bottom)<20:
            myimg[y, x, :] = white
        else:
            myimg[y, x, :] = gray

cv2.imwrite("2.jpeg",myimg)






