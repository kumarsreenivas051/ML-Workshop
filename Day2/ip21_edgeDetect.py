import cv2
import numpy as np

img = cv2.imread("download.jpg",0)

height, width = img.shape

sobelX= cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelY= cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('Original Image',img)
cv2.waitKey(0)

cv2.imshow('Sobel X Image',sobelX)
cv2.waitKey(0)

cv2.imshow('Sobel Y Image',sobelY)
cv2.waitKey(0)

sobelOr= cv2.bitwise_or(sobelY,sobelY)
cv2.imshow('Sobel OR Image',sobelOr)
cv2.waitKey(0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('Laplacian Image',laplacian)
cv2.waitKey(0)

canny = cv2.Canny(img,20,170)
cv2.imshow('Canny edge',canny)
cv2.waitKey(0)

cv2.destroyAllWindows()