from Filters import *
from Histograms import *

def cat_Modification(cat,name):
    cat_contrast= equalize(cat,name)
    cat_blur = blur(cat_contrast,name,3)
    return equalize(cat_blur,name+"_1")

def cheetah_Modification(cheetah,name):
    darken_cheetah =  adjust_brightness(cheetah, 0.6, 0.5,name)
    blur_cheetah = blur(darken_cheetah,name,3)
    mask = laplacian(blur_cheetah,name)
    return unsharpened(darken_cheetah,1,mask,0.5,name)

def city_Modification(city,name):
    city_equal = equalize(city,name)
    city_blur = blur(city_equal,name,8)
    return equalize(city_blur,name+"_1")

def deer_Modification(deer,name):
    darken = adjust_brightness(deer,0.5,0.5,name)
    blur_deer = blur(darken,name,3)
    mask = laplacian(blur_deer,name)
    return unsharpened(darken,1, mask,0.6, name)

def dog_Modification(dog,name):
    return equalize(dog,name)

def husky_Modification(husky,name):
    return equalize(husky,name)

def leopard_Modification(leopard,name):
    equalize_gray(cv2.cvtColor(leopard,cv2.COLOR_BGR2GRAY),name)
    blur0 = blur(leopard,name,3)
    lighten= adjust_brightness(blur0,2,0.5,name)
    mask = laplacian(lighten,name)
    return unsharpened(lighten,1, mask,0.6, name)

def ny_Modification(ny,name):
    return equalize(ny,name)

def rose_Modification(rose,name):
    contrast = equalize(rose,name)
    blur0 = blur(contrast,name,7)
    return sharpen(blur0,name,5)

def tricycle_Modification(bike,name):
    equal = equalize(bike,name)
    sharp = sharpen(equal,name,7)
    mask = laplacian(sharp,name)
    return unsharpened(equal, 1, mask, 0.5, name)


#---MAIN -------

#Problem 1
img_list = getImageList(get_before_image_path())
img_name = setImageNames(img_list)
collectHistograms(img_list, getBeforeHistogram())

for i in range(len(img_list)):
    image = loadImage(img_list[i])
    name = img_name[i]
    result = np.zeros(image.shape,image.dtype)

    if(i == 0):result = cat_Modification(image,name)
    elif(i == 1): result = cheetah_Modification(image,name)
    elif(i == 2): result = city_Modification(image,name)
    elif(i == 3): result = deer_Modification(image,name)
    elif(i == 4): result = dog_Modification(image,name)
    elif(i == 5): result = husky_Modification(image,name)
    elif(i == 6): result = leopard_Modification(image,name)
    elif(i == 7): result = ny_Modification(image,name)
    elif(i == 8): result = rose_Modification(image,name)
    elif(i == 9): result = tricycle_Modification(image,name)
    createHistogram(result,name, getAfterHistogram())
    save_final_image(result,name)

#Problem 2
image = loadImage(img_list[0])
name = img_list[0]+"_scale_"
scaled_up = cv2.resize(image,None,3,1,cv2.INTER_LINEAR)
save_final_image(scaled_up,name+"_up")

#scaled_down = cv2.resize(scaled_up,None,54,140,cv2.INTER_NEAREST)
#print scaled_down.size
#save_final_image(scaled_up,name+"_down")
print "Done"
