import cv2
import numpy
Mat src= imread("index1.jpg",CV_LOAD_IMAGE_COLOR); //load  image

Mat bgr[3];   //destination array
split(src,bgr);//split source  

//Note: OpenCV uses BGR color order
cv2.imwrite("blue.png",bgr[0]); //blue channel
cv2.imwrite("green.png",bgr[1]); //green channel
cv2.imwrite("red.png",bgr[2]); //red channel
cv2.waitKey(0)
cv2.destroyAllWindows()
