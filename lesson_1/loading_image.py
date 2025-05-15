import cv2
# importin computer vision library
image1 = cv2.imread("lesson_1\Jigglypuff - Copy.jpeg", cv2.IMREAD_COLOR)
# loading the image in orignal
cv2.imshow("jigglypuff image", image1)
# displaying the image "jigglypuff is the name of the window "
cv2.waitKey(0)
# hold the window on the screen until the user presses any key
cv2.destroyAllWindows()
# delete all the threads after code exquition



