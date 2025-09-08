import cv2
import sys 
import os
import numpy as np

mcl = "lesson_10/haarcascade_frontalface_default.xml"

datasets = "lesson_10/data_sets" 

subfolder = "Vihaan"

size = 4
print("recognising face please ensure there is sufficient lighting on face")
(images, labels, names, id) = ([], [], {}, 0)
# searching for the images
# to browsw to each of the file stored in the main folder and the sub folder. if it finds the file then it creates the path of the file and to keep it unique it gives an id which is als called as a label
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = os.path.join(subjectpath, filename)
            label = id
            img = cv2.imread(path,0)
            if img is None:
                print("fail to load the image ")
                continue
            images.append(img)
            labels.append(label)

        id += 1

images = np.array(images)
labels = np.array(labels)

recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.train(images,labels)
face_capture = cv2.CascadeClassifier(mcl)
webcam = cv2.VideoCapture(0)

while True:
    # Capture the frame
    (_, im) = webcam.read()
    
    # Check if the frame is valid
    if im is None:
        print("Error: Failed to capture image.")
        continue
    
    # Convert to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_capture.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (130, 100))

        prediction = recogniser.predict(face_resize)

        # Display the result
        if prediction[1] < 500:
            confidence = int(100 * (1 - (prediction[1] / 300)))  # Confidence percentage
            cv2.putText(im, f'{names[prediction[0]]} - {confidence}%', (x - 10, y - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        else:
            cv2.putText(im, 'Not recognized', (x - 10, y - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

    cv2.imshow('Face Recognition', im)

    key = cv2.waitKey(10)
    if key == 27:  # Exit on ESC key
        break

webcam.release()
cv2.destroyAllWindows()



