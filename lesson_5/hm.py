import cv2
 
#rotating

image = cv2.imread("lesson_5/8.png")
cv2.imshow("original image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

(rows,coulms) = image.shape[:2]
transform = cv2.getRotationMatrix2D((coulms/2,rows/2),270,1)
result = cv2.warpAffine(image,transform,(coulms,rows))
cv2.imwrite("transformed_image.jpg",result)
cv2.imshow("transformed_image",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
image1 = cv2.imread("lesson_5/Bart-Simpson-cartoon-686x1024.png")
cv2.imshow("original image 1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

(rows1,coulms1) = image1.shape[:2]
transform1 = cv2.getRotationMatrix2D((coulms1/2,rows1/2),155,1)
result1 = cv2.warpAffine(image1,transform1,(coulms1,rows1))
cv2.imwrite("transformed_image_1.jpg",result1)
cv2.imshow("transformed_image_1",result1)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread("lesson_5/dulingo.png")
cv2.imshow("original image 2",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
(rows2,coulms2) = image2.shape[:2]
transform2 = cv2.getRotationMatrix2D((coulms2/2,rows2/2),83,1)
result2 = cv2.warpAffine(image2,transform2,(coulms2,rows2))
cv2.imwrite("transformed_image_2.jpg",result2)
cv2.imshow("transformed_image_2",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()

image3 = cv2.imread("lesson_5/micey mouse.jpg")
cv2.imshow("original image 3",image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
(rows3,coulms3) = image3.shape[:2]
transform3 = cv2.getRotationMatrix2D((coulms3/2,rows3/2),40,1)
result3 = cv2.warpAffine(image3,transform3,(coulms3,rows3))
cv2.imwrite("transformed_image_3.jpg",result3)
cv2.imshow("transformed_image_3",result3)
cv2.waitKey(0)
cv2.destroyAllWindows()


image4 = cv2.imread("lesson_5/top25animecharacters.jpg")
cv2.imshow("original image 4",image4)
cv2.waitKey(0)
cv2.destroyAllWindows()

(rows4,coulms4) = image4.shape[:2]
transform4 = cv2.getRotationMatrix2D((coulms4/2,rows4/2),173,1)
result4 = cv2.warpAffine(image4,transform4,(coulms4,rows4))
cv2.imwrite("transformed_image_4.jpg",result4)
cv2.imshow("transformed_image4",result4)
cv2.waitKey(0)
cv2.destroyAllWindows()



# greysccale


image5 = cv2.imread("lesson_5/hera-bogini-grecka-1080x675 - Copy.jpg")
cv2.imshow("original image",image5)
cv2.waitKey(0)
cv2.destroyAllWindows()

grey_image5 = cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey_scale image",grey_image5)
cv2.waitKey(0)
cv2.destroyAllWindows()

image6 = cv2.imread("lesson_5/top25animecharacters.jpg")
cv2.imshow("original image",image6)
cv2.waitKey(0)
cv2.destroyAllWindows()


grey_image6 = cv2.cvtColor(image6,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey_scale image",grey_image6)
cv2.waitKey(0)
cv2.destroyAllWindows()


image7 = cv2.imread("lesson_5/micey mouse.jpg")
cv2.imshow("original image",image7)
cv2.waitKey(0)
cv2.destroyAllWindows()

grey_image7 = cv2.cvtColor(image7,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey_scale image",grey_image7)
cv2.waitKey(0)
cv2.destroyAllWindows()


image8 = cv2.imread("lesson_5/dulingo.png")
cv2.imshow("original image",image8)
cv2.waitKey(0)
cv2.destroyAllWindows()

grey_image8 = cv2.cvtColor(image8,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey_scale image",grey_image8)
cv2.waitKey(0)
cv2.destroyAllWindows()


# edge dection

image9 = cv2.imread("lesson_5/hera-bogini-grecka-1080x675 - Copy.jpg")
cv2.imshow("original image",image9)
cv2.waitKey(0)
cv2.destroyAllWindows()


edges9 = cv2.Canny(image9,100,200)
cv2.imshow("edged dection",edges9)
cv2.waitKey(0)
cv2.destroyAllWindows()


image10 = cv2.imread("lesson_5/top25animecharacters.jpg")
cv2.imshow("original image",image10)
cv2.waitKey(0)
cv2.destroyAllWindows()


edges10 = cv2.Canny(image10,100,200)
cv2.imshow("edged dection",edges10)
cv2.waitKey(0)
cv2.destroyAllWindows()


image11 = cv2.imread("lesson_5/dulingo.png")
cv2.imshow("original image",image11)
cv2.waitKey(0)
cv2.destroyAllWindows()


edges11 = cv2.Canny(image11,100,200)
cv2.imshow("edged dection",edges11)
cv2.waitKey(0)
cv2.destroyAllWindows()


image12 = cv2.imread("lesson_5/dog - Copy.png")
cv2.imshow("original image",image12)
cv2.waitKey(0)
cv2.destroyAllWindows()


edges12 = cv2.Canny(image12,100,200)
cv2.imshow("edged dection",edges12)
cv2.waitKey(0)
cv2.destroyAllWindows()



