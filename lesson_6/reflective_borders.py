import cv2


image = cv2.imread("lesson_6/top25animecharacters.jpg")
cv2.imshow("original image",image)
cv2.waitKey(0)

reflective_border = cv2.copyMakeBorder(image,40,40,40,40,cv2.BORDER_REFLECT,value = 1)
cv2.imshow("reflective_border",reflective_border)
cv2.waitKey(0)
cv2.destroyAllWindows