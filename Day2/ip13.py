import cv2
img=cv2.imread('index.jpg')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

img_scaled = cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('Scaling-Linear Interplotation',img_scaled)
cv2.waitKey()

img_scaled1 = cv2.resize(img,None,fx=2,fy=2)