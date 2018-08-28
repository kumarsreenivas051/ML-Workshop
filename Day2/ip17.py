import cv2
import numpy as np
img = cv2.imread('download.jpg')
cv2.imshow('Original',img)
cv2.waitKey()
m=np.ones(img.shape,dtype="uint8")*150
added= cv2.add(img,m)
cv2.imshow('added',added)
subtract = cv2.subtract(img,m)
cv2.imshow('subtracted',subtract)
mul= cv2.multiply(img,m)
cv2.imshow('multiplied',mul)
cv2.waitKey(0)
cv2.destroyAllWindows()