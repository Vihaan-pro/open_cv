import cv2

image = cv2.imread("lesson_5/hera-bogini-grecka-1080x675 - Copy.jpg")
cv2.imshow("original image",image)
cv2.waitKey(0)


grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey_scale image",grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()