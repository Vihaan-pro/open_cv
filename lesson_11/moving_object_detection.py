import cv2
# captures the frame from the viedio 
capture = cv2.VideoCapture("lesson_11/car.mp4")
ml = cv2.CascadeClassifier("lesson_11/cars.xml")
# loading the ml model 
while True :
    # read the frames from the viedio 
    ret,frames = capture.read()
    grey = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    # detect the vechles of diffrent sizes 
    cars =  ml.detectMultiScale(grey,1.1,1)
    for (x,y,w,h) in cars :
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("vechle detection",frames)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
