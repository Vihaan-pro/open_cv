import cv2


image = cv2.imread("lesson_4/An_illustration_of_ancient_Greek_gods_and_goddesse_smaller - Copy.png")
cv2.imshow("original image",image)
cv2.waitKey(0)
# this type of technick is mostly used in machin learning or photo editing it is used clean or soften the image
gaussian = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("gaussian blur",gaussian)
cv2.waitKey(0)

# this a random noise(disturbing elements in picture) to keep te border sharp
median = cv2.medianBlur(image,5)
cv2.imshow("median blur",median)
cv2.waitKey(0)

# bilateral
bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow("bilateral blur",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()