import cv2
import numpy as np

# addition
jigglypuff = cv2.imread(r"lesson_3/Jigglypuff - Copy.jpeg",cv2.IMREAD_COLOR)
pika = cv2.imread(r"lesson_3/pika1.png",cv2.IMREAD_COLOR)
mix = cv2.addWeighted(jigglypuff,0.7,pika,0.3,0)
cv2.imshow("mix",mix)


cv2.waitKey(0)
cv2.destroyAllWindows()


# subtraction

jigglypuff1 = cv2.imread(r"lesson_3/Jigglypuff - Copy.jpeg")
pika1 = cv2.imread(r"lesson_3/pika1.png")
subtracted_image = cv2.subtract(jigglypuff1,pika1)
cv2.imshow("subtracted_image",subtracted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#largenig

jigglypuff2 = cv2.imread(r"lesson_3/pika1.png")
cv2.imshow("original_image",jigglypuff2)
cv2.waitKey(0)

resised_image = cv2.resize(jigglypuff2,(400,400))
cv2.imshow("largened image",resised_image)
cv2.waitKey(0)
cv2.destroyAllWindows

#shortened

pika2 = cv2.imread(r"lesson_3/pika1.png")
cv2.imshow("original_image",pika2)
cv2.waitKey(0)

resised_image_2 = cv2.resize(pika2,(100,100))
cv2.imshow("shortened image",resised_image_2)
cv2.waitKey(0)
cv2.destroyAllWindows

# erosion

pika3 = cv2.imread(r"lesson_3/pika1.png")
cv2.imshow("original_image",pika3)
cv2.waitKey(0)
kernel = np.ones((5,5),np.uint8)
eroed_image = cv2.erode(pika,kernel)
cv2.imshow("erodeed_image",eroed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()