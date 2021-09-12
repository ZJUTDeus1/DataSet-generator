import os
import cv2
def SaltAndPepper(src,percetage=0.5):  
    SP_NoiseImg=src.copy()
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1]) 
    for i in range(SP_NoiseNum): 
        randR=np.random.randint(0,src.shape[0]-1) 
        randG=np.random.randint(0,src.shape[1]-1) 
        randB=np.random.randint(0,3)
        if np.random.randint(0,1)==0: 
            SP_NoiseImg[randR,randG,randB]=0 
        else: 
            SP_NoiseImg[randR,randG,randB]=255 
    return SP_NoiseImg 
def addGaussianNoise(image,percetage=0.5): 
    G_Noiseimg = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    G_NoiseNum=int(percetage*image.shape[0]*image.shape[1]) 
    for i in range(G_NoiseNum): 
        temp_x = np.random.randint(0,h) 
        temp_y = np.random.randint(0,w) 
        G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0] 
    return G_Noiseimg
#dimming
def darker(image,percetage=0.9):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    #get darker
    for xi in range(0,w):
        for xj in range(0,h):
            image_copy[xj,xi,0] = int(image[xj,xi,0]*percetage)
            image_copy[xj,xi,1] = int(image[xj,xi,1]*percetage)
            image_copy[xj,xi,2] = int(image[xj,xi,2]*percetage)
    return image_copy
def brighter(image, percetage=1.5):
    #image_copy = image.copy()
    #w = image.shape[1]
    #h = image.shape[0]
    ##get brighter
    #for xi in range(0,w):
    #    for xj in range(0,h):
    #        image_copy[xj,xi,0] = np.clip(int(image[xj,xi,0]*percetage),a_max=255,a_min=0)
    #        image_copy[xj,xi,1] = np.clip(int(image[xj,xi,1]*percetage),a_max=255,a_min=0)
    #        image_copy[xj,xi,2] = np.clip(int(image[xj,xi,2]*percetage),a_max=255,a_min=0)
    img_bright=cv2.convertScaleAbs(image,alpha=1.5,beta=0)
    return img_bright


filepath='total2019'
enhance_set=['SaltAndPepper','addGaussianNoise','darker','brighter'] 
for enhance_way in enhance_set:
    if(os.path.exists(filepath+'-'+enhance_way)):
        pass
    else:
        os.mkdir(filepath+'-'+enhance_way)
    for img_name in os.listdir(filepath):
        img=cv2.imread(filepath+'/'+img_name)
        enhanced_img_name=img_name.split('.')[0]+'_'+enhance_way+'.'+img_name.split('.')[1]
        enhanced_img=locals()[enhance_way](img)\
        print(enhance_img_name)
        cv2.imwrite(filepath+'-'+enhance_way+'/'+enhanced_img_name,enhanced_img)
