import os
os.chdir("/home/zjutrobot/Desktop/VOC2007/JPEGImages")
for file in os.listdir("/home/zjutrobot/Desktop/VOC2007/JPEGImages"):
    print(file)
    if(os.path.splitext(file)[1]==".png"):
         os.rename(file,os.path.splitext(file)[0]+".jpg")
