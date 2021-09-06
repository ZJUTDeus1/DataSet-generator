import shutil
import cv2 as cv
import os

sets=['train2019',  'val2019', 'test2019']
for dir_name in sets:
    os.makedirs('./images/%s'%(dir_name), exist_ok=True)
    os.makedirs('./labelme/%s'%(dir_name),exist_ok=True)

for image_set in sets:
    image_ids = open('./%s.txt'%(image_set)).read().strip().split()
    for image_id in image_ids:
        img = cv.imread('images/total2019/%s.jpg' % (image_id))
        json='labelme/total2019/%s.json'% (image_id)
        cv.imwrite('images/%s/%s.jpg' % (image_set,image_id), img)
        cv.imwrite('labelme/%s/%s.jpg' % (image_set,image_id), img)
        shutil.copy(json,'labelme/%s/%s.json' % (image_set,image_id))
print("完成")
