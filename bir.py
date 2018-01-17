'''
measuring pixel brightness 測量像素的亮度
https://stackoverflow.com/questions/6442118/python-measuring-pixel-brightness
Extracting and Saving Video Frames
https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames

Illuminance python

https://github.com/MilesGordenker/Luxometer/blob/master/luxometer.py

http://python-colormath.readthedocs.io/en/latest/color_appearance_models.html

http://answers.opencv.org/question/24260/how-to-determine-an-image-with-strong-or-weak-illumination-in-opencv/

http://scikit-image.org/docs/dev/api/skimage.color.html

https://pypi.python.org/pypi/grapefruit/
https://github.com/xav/Grapefruit/

http://colour-science.org/

http://tbleicher.github.io/wxfalsecolor/

https://sourceforge.net/p/raspfm/code-0/1/tree/trunk/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_TCS34725/Adafruit_TCS34725.py

http://mri.ee.ntust.edu.tw/wp/?p=665

樹莓派系列4——環境光照強度測量
http://blog.csdn.net/weixiazailaide/article/details/52782458

https://ccw1986.blogspot.tw/2017/05/opencv-tutorial.html

https://packages.debian.org/zh-cn/jessie/python-grapefruit

http://pillow.readthedocs.io/en/3.1.x/reference/Image.html

http://python.jobbole.com/81593/

https://yq.aliyun.com/articles/70768

http://zqdevres.qiniucdn.com/data/20160322112041/index.html

http://zhaoxuhui.top/blog/2017/06/28/%E5%9F%BA%E4%BA%8EPython%E7%9A%84OpenCV%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%8617.html

http://blog.csdn.net/chenbang110/article/details/56011119


https://www.youtube.com/watch?v=pHD9YfJaqeY

Python Generators in Image Luminance Conversion and Binarization
1) Relative Luminance Formula
2) Conversion of RGB Images to Gray Level Images with Relative Luminance
3) Global Binarization Gray Level Images
4) Python Generator Factories
5) Pixel Iteration with Python Generators
6) Class Home Page is at http://vkedco.blogspot.com/2012/01/py...
7) Video Narration: Vladimir Kulyukin

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



