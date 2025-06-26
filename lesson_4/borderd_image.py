import cv2


image = cv2.imread("lesson_4\hera-bogini-grecka-1080x675 - Copy.jpg")
cv2.imshow("original image",image)
cv2.waitKey(0)

borderd_image = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=1)
cv2.imshow("border image",borderd_image)
cv2.waitKey(0)
cv2.destroyAllWindows()