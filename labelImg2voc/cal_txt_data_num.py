import sys
import os

# 计算txt中有多少个数据，即有多上行

names_txt = os.listdir('/home/zjutrobot/Desktop/mm_new/data/VOC2007/ImageSets/Main')
#print(names_txt)
for name_txt in names_txt:
    with open(os.path.join('./ImageSets/Main', name_txt)) as f:
        lines = f.readlines()
        print(('文件 %s'%name_txt).ljust(35) + ("共有数据：%d个"%len(lines)).ljust(50))

