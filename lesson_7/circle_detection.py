import cv2
import numpy as np 

image = cv2.imread("lesson_7/ovals.jpg")
cv2.imshow("image",image)
cv2.waitKey(0)

# always convert colored image to greyscale because the the computer will be able to dectecte the circles much easier

grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# convert the image to grid of 3/3 so it will help detect the circles

grid = cv2.blur(grey,(3,3))

# cv2.HOUGH_GRADIENT is an fuction to find circles , 1 is reseultion , 20 is min distance between circles (pixels) , param1=50,param2=30 helps deside  
# , param1=50,param2=30 helps decide the machine if it is a circle even id there is a minor change, minRadius=1,maxRadius=50 these are to detect small and big circles

detected_circles = cv2.HoughCircles(grid,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=50)

if detected_circles is not None :
    detected_circles = np.uint16(np.around(detected_circles))
    for i in detected_circles[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(image,(x,y),r,(0,255,0),5)
        cv2.circle(image,(x,y),1,(0,255,255),3)
        cv2.imshow("detected_circles",image)
        cv2.waitKey(0)

cv2.destroyAllWindows()


    