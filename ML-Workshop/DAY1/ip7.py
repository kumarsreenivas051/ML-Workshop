import cv2
import numpy as np

#img=np.zeros((512,512,3),np.uint8)
img1=np.zeros((512,512,3),np.uint8)+255
cv2.imshow('Black Rectangle(colour)',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
