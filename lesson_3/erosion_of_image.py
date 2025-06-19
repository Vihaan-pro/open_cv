import cv2
import numpy as np
image_1 = cv2.imread(r"lesson_3/pika.png")
cv2.imshow("original_image",image_1)
cv2.waitKey(0)
kernel = np.ones((5,5),np.uint8)
eroed_image = cv2.erode(image_1,kernel)
cv2.imshow("erodeed_image",eroed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
