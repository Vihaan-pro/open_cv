import cv2


image = cv2.imread("lesson_6/top25animecharacters.jpg")
cv2.imshow("original image",image)
cv2.waitKey(0)

start_point = (0,0)
ending_point = (250,250)
color = (0,255,0)
thicknes = (10)
draw_on_image = cv2.line(image,start_point,ending_point,color,thicknes)
cv2.imshow("draw_on_image",draw_on_image)
cv2.waitKey(0)
cv2.destroyAllWindows()