'''
measuring pixel brightness 測量像素的亮度
https://stackoverflow.com/questions/6442118/python-measuring-pixel-brightness
Extracting and Saving Video Frames
https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
'''
#import Image
from PIL import Image
import cv2
import math
import time

cap = cv2.VideoCapture(0)
#success, image = cap.read()

#count = 0
success = True
while success:
    success, image = cap.read()
    #print('Read a new frame: ', success)
    cv2.imwrite("frameabc.jpg", image)  # save frame as JPEG file
    #count += 1
    imag = Image.open("frameabc.jpg") # girl obama
    #cv2.imshow('img', image)
    #Convert the image te RGB if it is a .gif for example
    imag = imag.convert ('RGB')
    #imag = imag.convert(imag)
    #coordinates of the pixel
    X,Y = 0,0
    #Get RGB
    pixelRGB = imag.getpixel((X,Y))
    R,G,B = pixelRGB
    brightness = sum([R,G,B])/3 ##0 is dark (black) and 255 is bright (white)
    print("brightness = ", brightness)
    time.sleep(1)

'''


import cv2
vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1



#Standard
LuminanceA = (0.2126*R) + (0.7152*G) + (0.0722*B)
print("LuminanceA = ", LuminanceA)
#Percieved A
LuminanceB = (0.299*R + 0.587*G + 0.114*B)
print(LuminanceB)
#Perceived B, slower to calculate
LuminanceC = sqrt( 0.241*R^2 + 0.691*G^2 + 0.068*B^2 )
print("LuminanceC = ", LuminanceC)

'''



