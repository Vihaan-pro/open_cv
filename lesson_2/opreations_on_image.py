import cv2

alien = cv2.imread(r"D:\dekstop\Open_cv\lesson_2\pika.png",cv2.IMREAD_COLOR)
alien_blue,alien_green,alien_red = cv2.split(alien)
cv2.imshow("alien_image_blue",alien_blue)
cv2.imshow("alien_image_green",alien_green)
cv2.imshow("alien_image_red",alien_red)

cv2.waitKey(0)
cv2.destroyAllWindows()

bg = cv2.imread(r"D:\dekstop\Open_cv\lesson_2\bg_2.jpg",cv2.IMREAD_COLOR)
bg_one = cv2.imread(r"D:\dekstop\Open_cv\lesson_2\bg_1.jpg",cv2.IMREAD_COLOR)
bg3 = cv2.addWeighted(bg,0.5,bg_one,0.5,0)
cv2.imshow("bg3",bg3)


cv2.waitKey(0)
cv2.destroyAllWindows()
