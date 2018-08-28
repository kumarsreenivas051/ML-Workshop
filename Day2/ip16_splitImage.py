import cv2
import numpy as np

img = cv2.imread('download.jpg')
height, width = img.shape[:2]
srow, scol = int(height*.1), int(width*.1)
srow1 ,scol1 = int(height*0.25), int(width*.25)
srow2 ,scol2 = int(height*0.5), int(width*.5)
srow3 ,scol3 = int(height*0.75), int(width*.75)


erow, ecol = int(height*.25),int(width*.25)
erow1, ecol1 = int(height*.5),int(width*.5)
erow2, ecol2 = int(height*.75),int(width*.75)
erow3, ecol3 = int(height*1),int(width*1)


cropped = img[srow:erow,scol:ecol]
cropped1= img[srow1:erow1,scol1:ecol1]
cropped2 = img[srow2:erow2,scol2:ecol2]
cropped3=img[srow3:erow3,scol3:ecol3]

cv2.imshow('cropped',cropped)
cv2.imshow('cropped1',cropped1)
cv2.imshow('cropped2',cropped2)
cv2.imshow('cropped3',cropped3)

cv2.waitKey(0)
cv2.destroyAllWindows()
