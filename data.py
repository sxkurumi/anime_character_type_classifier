from PIL import Image
import Process as p
import os

list = os.listdir("./3")
# print(list)

for image in list:
    ix = image.find(".")
    name = image[0:ix]
    # print(name)
    p.resize_image("./3/"+image,128,"./3/"+image)
    for i in range(3):
        for j in range(2):
            p.image_transform("./data/1/" + image, "./data/1/"+name+"_"+str(i)+"_"+str(j)+".jpg", i)

    for i in range(3):
        p.image_enhance("./data/1/" + image, "./data/1/" + image, i)





