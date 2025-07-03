import cv2

image = cv2.imread("lesson_5\hera-bogini-grecka-1080x675 - Copy.jpg")
cv2.imshow("original image",image)
cv2.waitKey(0)


edges = cv2.Canny(image,100,200)
cv2.imshow("edged dection",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()