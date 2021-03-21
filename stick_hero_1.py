import numpy as np
import os
from matplotlib import pyplot as plt
import pause
import cv2

rate = 0.51
def srcTarget(rcord):
    prev=rcord[0]
    for i in rcord:
        # print(prev,i)
        if abs(i-prev) > 10:
            return i, prev + 5    # +5 is just to vaguely compenate for extra distance where stick rises
        prev=i
while True:

    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')

    # read the image using openCV
    img = cv2.imread('screencap.png')
    screen_height, screen_width, _ = img.shape

    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    yf, xf, zf = np.shape(img)
    yf = yf/2280
    xf = xf/1080
    
    img_crop = img[int(np.floor(1500*yf)):int(np.floor(1640*yf)), :]
    y_crop, x_crop, z_crop = np.shape(img_crop)
    
    """   setting all the rgb values to ZERO gives black color, here we do the same using np.zeros_like()   """ 
    my_img = np.zeros_like(img_crop)

    rcord=set()
    
    for j in range(y_crop):
        for k in range(x_crop):
            if(((img_crop[j,k,0]==255) and (img_crop[j,k,1]==0) and (img_crop[j,k,2]==0)) or ((img_crop[j,k,0]==247) and (img_crop[j,k,1]==27) and (img_crop[j,k,2]==27))):
                my_img[j,k,0] = 0
                my_img[j,k,1] = 255
                my_img[j,k,2] = 0
                rcord.add(k)  # record the x-coordinates of your red-color cells in a set
                
    # sort the elements in the set in ascending order and make a list

    rcord = sorted(rcord)
    target, src = srcTarget(rcord)
    
    dist = abs(src-target)
    rate = 1.0475 * (screen_width/1080)
    time = str(int(dist/rate))
    
    print(dist)
    
    """   just fix some x, y coordinate to swipe on the screen, with time already calculated before  """ 

    x = str(int(np.ceil(530*yf)))
    y = str(int(np.ceil(830*xf)))

    os.system('adb shell input touchscreen swipe ' + x + ' ' + x + ' ' + y + ' ' + y + ' ' + time)
    pause.seconds(2)