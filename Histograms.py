from matplotlib import pyplot as plt
import cv2
import os
def createHistogram(image,i_name,dir):
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.title(i_name+' histogram')
    plt.xlabel('intensity')
    plt.ylabel('frequency')
    plt.savefig(dir+'\\'+str(i_name)+'.png')
    plt.close()

def collectHistograms(img_list,dir):
    for i,img in enumerate(img_list):
        createHistogram(loadImage(img),img_list[i],dir)

def setImageNames(list):
    names=[]
    for img in list:
        name= img.split(".jpg")[0]
        names.append(name)
    return names

def loadImage(name):
    name = get_before_image_path() +'\\'+ name
    return cv2.imread(name,1)

def save_final_image(image,name):
    path = get_after_image_path()+"\\"+name+'.jpg'
    cv2.imwrite(path,image)

#Image paths
def get_before_image_path():
    return os.getcwd()+"\\images\\before"

def get_after_image_path():
    return os.getcwd()+"\\images\\after"

def getBeforeHistogram():
    return os.getcwd()+'\\histogram\\before'

def getAfterHistogram():
    return os.getcwd()+'\\histogram\\after'

def getImageList(path):
    return os.listdir(path)




