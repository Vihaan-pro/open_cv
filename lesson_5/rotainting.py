import cv2

image = cv2.imread("lesson_5/8.png")
cv2.imshow("original image",image)
cv2.waitKey(0)

(rows,coulms) = image.shape[:2]
transform = cv2.getRotationMatrix2D((coulms/2,rows/2),270,1)
result = cv2.warpAffine(image,transform,(coulms,rows))
cv2.imwrite("transformed_image.jpg",result)
cv2.imshow("transformed_image",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
