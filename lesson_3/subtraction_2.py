import cv2

image_1 = cv2.imread(r"lesson_3/bg_1.jpg")
image_2 = cv2.imread(r"lesson_3/bg_2.jpg")
subtracted_image = cv2.subtract(image_2,image_1)
cv2.imshow("subtracted_image",subtracted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
