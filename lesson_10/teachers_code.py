import cv2, sys, os

haar_file = "lesson_10\haarcascade_frontalface_default.xml"
datasets = "lesson_10\data_sets"
sub_data = "Vihan"

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
    

(width, height) = (130, 100)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    sys.exit()
count = 1
while count < 30:
    # Capture the frame
    (_, im) = webcam.read()
    
    # Check if the frame is valid
    if im is None:
        print("Error: Failed to capture image.")
        continue
    
    # Convert to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
        count += 1
        cv2.imshow('OpenCV', im)
    
    key = cv2.waitKey(10)
    if key == 27:  # ESC key to exit
        break

webcam.release()
cv2.destroyAllWindows()