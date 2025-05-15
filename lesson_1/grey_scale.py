import cv2
# importin computer vision library
image1 = cv2.imread(r"d:\dekstop\Open_cv\lesson_1\8.png", 0)
# loading the image in grey scale 
cv2.imshow("Alien alone", image1)
# displaying the image "jigglypuff is the name of the window "
cv2.waitKey(0)
# hold the window on the screen until the user presses any key
cv2.destroyAllWindows()
# delete all the threads after code exquition





