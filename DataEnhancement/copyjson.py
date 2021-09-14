import os
enhance_set=['SaltAndPepper','addGaussianNoise','darker','brighter'] 
filenameset=[]
for file in os.listdir('total2019'):
    filenameset.append(file)
print(filenameset)
for enhance_way in enhance_set:
    for file in filenameset:
        new_file=file.split('.')[0]+'_'+enhance_way+'.'+file.split('.')[1]
        print(file.split('.')[0]+'_'+enhance_way+'.'+file.split('.')[1])
        os.system('cp total2019/'+file+' '+'total2019/'+new_file)
    

