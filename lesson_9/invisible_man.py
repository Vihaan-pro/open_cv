import cv2
import numpy as np

count = 0

raw = cv2.VideoCapture("lesson_9/video.mp4")
for i in range (61):
    return_value,baground = raw.read()
    if return_value == False:
        continue

# capturing the baground which will be used for masking pourpuses and we are flipping it for the mirror image
baground = np.flip(baground,axis=1)
while raw.isOpened():
    return_value, image = raw.read()
    if not return_value or image is None:
        break
    count += 1
    image = np.flip(image, axis=1)

#while raw.isOpened():
    #return_value,image = raw.read()
    # to keep track of the frame no. we are using (count)
    #count += 1
    # every frame of the viedio is flipped to create the mirror efect
    #image = np.flip(image,axis = 1)
    # ...existing code...
    # converting the baground colors into the hsv colors 
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    # to ensure there is no trace of red in the viedio by giveing starting rgb code of red and ending code
    starting_range = np.array([100,40,40])
    ending_range = np.array([100,255,255])
    mask_one = cv2.inRange(hsv,starting_range,ending_range)
    # we are covering the mising shades of red 
    start_one = np.array([50,40,40])
    end_one = np.array([180,255,255])
    mask_two = cv2.inRange(hsv,start_one,end_one)
    # we are combining all the shades of red
    mask_one = mask_one + mask_two
    # apply morfology to remove the noise 
    mask_one = cv2.morphologyEx(mask_one,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    # dialegiht or expand the image so that it will cover the entire red color
    mask_one = cv2.dilate(mask_one,np.ones((3,3),np.uint8),iterations=1)
    # inverse mask one and focus on non red areas 
    mask_two = cv2.bitwise_not(mask_one)
    # sepearating baground and the object
    result_one = cv2.bitwise_and(baground,baground,mask = mask_one)    
    result_two = cv2.bitwise_and(image,image,mask = mask_two)
    final_output = cv2.addWeighted(result_one,1,result_two,1,0)
    cv2.imshow("invisible man",final_output)
    abcd = cv2.waitKey(10)
    if abcd == 27:
        break
