import cv2
import os

# Corrected save path
save_file = "d:/dekstop/Open_cv"

# Load the image
image1 = cv2.imread("lesson_1/Jigglypuff - Copy.jpeg", cv2.IMREAD_COLOR)
# 1 = color , 0 = greyscale , -1 unchanged
# Display the image
cv2.imshow("jigglypuff image", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Change directory to the save path
os.chdir(save_file)

# Save the image with a valid filename and extension
cv2.imwrite("colored_jigglypuff.jpg", image1)
print("The image is correctly saved")


