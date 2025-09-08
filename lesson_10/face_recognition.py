import cv2
import sys
import os

mcl = "lesson_10/haarcascade_frontalface_default.xml"

datasets = "lesson_10/data_sets" 

subfolder = "Vihaan"

path = os.path.join(datasets,subfolder)
# witdh and hight is for the image that the camera is going to capture
height,width = (100,130)
# this function is used to call the machine learnig model 
face_capture = cv2.CascadeClassifier(mcl)
# it will capture the excat picture and only the face will be captured
webcam = cv2.VideoCapture(0)

count = 1 

while count < 30 :
     ret, im = webcam.read()
     if not ret or im is None:
         print("Failed to capture image from webcam.")
         continue
     grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
     faces = face_capture.detectMultiScale(grey, 1.3, 4)

     for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),5)
        face = grey[y:y+h,x:x+w]
        face_resized = cv2.resize(face,(width,height))
        cv2.imwrite('% s/% s.png'%(path,count),face_resized)
        count+=1
     cv2.imshow("opencv",im)
     key = cv2.waitKey(100)
     if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
