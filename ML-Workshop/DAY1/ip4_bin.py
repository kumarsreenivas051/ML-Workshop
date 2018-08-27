import cv2

img=cv2.imread("index1.jpg",0)
ret,th=cv2.threshold(img,125,255,cv2.THRESH_BINARY)
ret,th1=cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
print(ret)
cv2.imshow("Hello World",img)
cv2.imshow("Hello World",th)
cv2.imshow("Hello World",th1)
cv2.waitKey(0)
cv2.destroyAllWindows()
