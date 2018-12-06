import numpy as np
import cv2
import os


def save_image_with_filter(img, path):
    path = os.getcwd()+'\\filters\\'+path+'.jpg'
    cv2.imwrite(path,img)

def get_sharpen_intensity_name(intensity):
    if intensity <=5: return "_low"
    elif intensity ==6: return "_mid"
    return "_high"

def get_blur_intensity_name(intensity):
    if intensity <=5: return "_a_low"
    elif intensity == 6: return "_a_mid"
    return "_a_high"

#---------FILTERS AND MASKS-----------------------------------
def unsharpened(src, w1, mask, w2, name):
    dst = cv2.addWeighted(src,w1,mask,w2,0)
    path = 'sharpen\\unsharpen\\unsharpen_'+name
    save_image_with_filter(dst, path)
    return dst

def laplacian(img, name):
    kernel =np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    dst = cv2.filter2D(img,-1,kernel)
    path ='mask\\'+name
    save_image_with_filter(dst, path)
    return dst

#Manipulate contrast and light
#formula: y = alpha * f(x) + beta + gamma
#alpah: contrast and beta: brightness
def adjust_brightness(img, w1,w2,name):
    mask = get_black_mask(img)
    dst =cv2.addWeighted(img,w1,mask,w2,0)
    path = '\\brightness\\'+name
    save_image_with_filter(dst, path)
    return dst

def get_black_mask(img):
    black_img = np.zeros(img.shape,img.dtype)
    return black_img

#5 to 7 - sharpen from low to high
def sharpen(image,name,intensity):
    kernel =np.array([[0,-1,0],[-1,intensity,-1],[0,-1,0]]) #range from 5 to 7
    dst = cv2.filter2D(image,-1,kernel)
    name = name+get_sharpen_intensity_name(intensity)
    path = 'sharpen\\sharp\\sharpen_'+name
    save_image_with_filter(dst, path)
    return dst

#3 to 8 - average blur from low to high
def blur(image, name, intensity):
    kernel = np.ones((intensity,intensity),np.float32)/(intensity*intensity)
    dst = cv2.filter2D(image,-1,kernel)
    name = name + get_blur_intensity_name(intensity)
    path = 'blur\\average\\'+name
    save_image_with_filter(dst, path)
    return dst

#increase contrast
def equalize(image,name):
    b,g,r = cv2.split(image)
    b_dst = cv2.equalizeHist(b)
    g_dst = cv2.equalizeHist(g)
    r_dst = cv2.equalizeHist(r)
    dst = cv2.merge((b_dst,g_dst,r_dst))
    path = 'equalize\\equalize_'+name
    save_image_with_filter(dst, path)
    return dst

def equalize_gray(image,name):
    dst = cv2.equalizeHist(image)
    path = 'equalize\\equalize_'+name
    save_image_with_filter(dst, path)
    return dst
