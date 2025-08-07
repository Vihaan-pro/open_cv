import cv2
import os
from PIL import Image
 


image_folder = r"D:/dekstop/photos_for_colage_in _opencv"

os.chdir(image_folder)

mean_hight = 0
mean_witdh = 0
number_of_images = len([i for i in os.listdir(image_folder)])
for i in os.listdir(image_folder):

    im = Image.open(os.path.join(image_folder,i))
    witdh,hight = im.size
    mean_hight + hight
    mean_witdh + witdh

mean_witdh = int(mean_witdh/number_of_images)
mean_hight = int(mean_hight/number_of_images)
for i in os.listdir(image_folder):

     im = Image.open(os.path.join(image_folder,i))
     witdh,hight = im.size
     im_resise = im.resize((mean_witdh,mean_hight),Image.LANCZOS)
     im_resise.save(i,"JPG",quality = 95)

def viedio_genrator():
    viedo_name = "my_first_viedio"
    os.chdir(r"D:/dekstop/photos_for_colage_in _opencv")
    images = []
    for a in os.listdir("."):
        if a.endswith(".jpg"):
            images.append(a)
    print(images)
    frame = cv2.imread(os.path.join(".",images[0]))
    hight,witdh,layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video = cv2.VideoWriter(viedo_name,fourcc,1,(witdh,hight))
    for i in images:
        video.write(cv2.imread(os.path.joint(".",i)))
    cv2.destroyAllWindows()
    video.release()

viedio_genrator()


