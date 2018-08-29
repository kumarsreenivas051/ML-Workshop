import cv2
img = cv2.imread("edge3.png")
cv2.imshow("Original", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 30, 200)
cv2.imshow("Canny Edged", edged)
cv2.waitKey(0)

_,contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Canny edged after contouring",edged)
cv2.waitKey(0)
print(_)
print("No. of contours found", str(len(contours)))
cv2.drawContours(img, contours ,-1 ,(0,255,0),3)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
