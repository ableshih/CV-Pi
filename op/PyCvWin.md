Python OpenCV Windows



1.安裝Python

  下載 python-2.7.11.msi 17.7 MB (18,636,800 位元組)
  https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi

  安裝 python2.7.11，(安裝時要抅選的安裝項目都要抅)

  安裝完後 win+r cmd，
  在 cmd 輸入 python -V，(出現 "不是內部或外部命令"，將python的安裝目錄加到PATH，例如 "C:\Python27"。)

2.安裝 Numpy

  要先安裝pip
  (用上一步的 win+r cmd)
  輸入 python -m pip install -U pip 
  下載到的檔案 pip-9.0.1-py2.py3-none-any.whl (1.3MB)
  安裝有抅選就不用加path(安裝完後將pip的路徑加到PATH裡，例如 "C:\Python27\Scripts" )

  (用上一步的 win+r cmd) 
  pip 出現 "不是內部或外部命令" 表示失敗
  
  cd /d C:\Python27\Scripts


  安裝numpy
  (用上一步的 win+r cmd)
  輸入pip install numpy 
  下載到的檔案 numpy-1.14.0-cp27-none-win32.whl (9.8MB)

下載安裝opencv 
opencv-2.4.13.exe 266 MB (279,685,353 位元組)
https://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.13/opencv-2.4.13.exe/download

複製cv2.pyd 
將 c:\opencv\build\python\2.7\x86\cv2.pyd，複製到 C:\Python27\Lib\site-packages 文件夾中。

測試：
(用上一步的 win+r cmd)
  輸入python
  
.C:\Python27\Scripts>python
.Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
.Type "help", "copyright", "credits" or "license" for more information.
.>>> import numpy as np
.>>> import cv2
.>>> cv2.__version__
.'2.4.13'
.>>>





安裝環境：Win10，Python2.7.11，pip-9.0.1， Numpy 1.14.0，OpenCV2.4.13



C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml
