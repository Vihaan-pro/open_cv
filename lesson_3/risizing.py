import cv2

image_1 = cv2.imread(r"lesson_3/pika.png")
cv2.imshow("original_image",image_1)
cv2.waitKey(0)

resised_image = cv2.resize(image_1,(400,400))
cv2.imshow("reduced_image",resised_image)
cv2.waitKey(0)
cv2.destroyAllWindows


resised_image_2 = cv2.resize(image_1,(1000,1000))
cv2.imshow("enlargened_image",resised_image_2)
cv2.waitKey(0)
cv2.destroyAllWindows