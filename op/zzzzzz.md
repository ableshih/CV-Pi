http://thegreatgeekery.blogspot.tw/
https://developer-blog.net/


key setup no ~ # issue
Localistion - > keyboard
set keyboard
Country Taiwan
Variant Taiwanese


$ cd ~
$ pwd
/home/pi

$ cd ..
$ pwd
/home

$ cd /
$ pwd
/

$ ls (dir)
$ ls -a

$ cp (copy)

$ mv (move)

$ rm (del)

$ nano (text edit)

$ more (type text)

$ echo “123” > test.txt (copy com)

$ mkdir (md)

$ rm -r mydir (del folder)

$ ls -l

$ chmod 777 test.txt

$ sudo

$ passwd

$ apt-cache

$ sudo apt-get remove xxx

$ sudo nano /etc/rc.local (boot auto run)

$ sudo apt-get install scrot (cat screen hot print)

$ hostname -I (ip )

$ route -n

$ sudo nano /etc/dhcpcd.conf

$ ip addr show eth0

$ sudo iwlist wlan0 scan

$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

$ ip addr show wlan0

$ sudo ifdown wlan0

$ sudo ifup wlan0

$ ssh pi@raspberrypi.local

$ ssh pi@192.168.1.1

$ ssh-keygen -R 192.168.1.1

FTP
FileZilla
VNC

$ vncserver :1

$ cd ~
$ cd .config
$ mkdir autostart
$ cd autostart
$ nano tightvnc.desktop


import RPi.GPIO as GPIO
$ sudo apt-get install python-rpi.gpio

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.HIGH)

$ sudo apt-get install fswebcam
$ sudo apt-get install python-serial

#--------------------------
RRB3 board 
$ cd ~
$ git cline http://github.com/simonmonk/rasprotboard3.git
$ cd raspirobotboard3/python
$ sudo python setup.py install
#--------------------------
#--------------------------
Arduino IDE
$ sudo apt-get install arduino
$ ls /dev/tty*
/dev/ttyACM0
$ sudo apt-get install python-serial python3-serial
#--------------------------
Firmata
$ sudo pip install pyfirmata
import pyfirmata
#--------------------------
guvcview
$ sudo apt-get install guvcview
$ sudo guvcview
https://iclab.hackpad.com/ep/pad/static/QZb0JX8iScu
#--------------------------



















4


https://elinux.org/RPiconfig

Raspberry Pi專案實作｜語音時鐘x動作偵測x網路電台x循跡機器人
http://books.gotop.com.tw/v_ACH019000

$ raspi-config
$ lsusb
$ lsusb -t
$ sudo find /dev/vid* 

https://gist.github.com/chyuaner/5317709

wifi IDE 
wicd-gtk

LXDE (look desktop)
lxshortcut -o ~/music.desktop

open root
$ sudo -s 
exit root
$ exit

task manager
luvcview
$ sudo apt-get install -y luvcview

rec video
raspivid
play video
omxplayer

gparted
view HDD partition


ALSA是Advanced Linux Sound Architecture 

VLC



fswebcam

利用 crontab 來做 Linux 固定排程
crontab -e (編輯該使用者的 crontab 指令)
還有一些人性化的參數，一次取代全部五個數字參數

【@reboot】 ：僅在開機的時候執行一次。
【@yearly】 ：一年執行一次，和0 0 1 1 * command效果一樣。
【@annually】：（和@yearly一樣）
【@monthly】：一個月執行一次，和0 0 1 * * command效果一樣。
【@weekly】：一個星期執行一次，和0 0 * * 0 command效果一樣。
【@daily】：每天執行，和0 0 * * * command效果一樣。
【@midnight】：（和@daily一樣）
【@hourly】 ：每小時執行，和0 * * * * command效果一樣。

#----------------------------------------
i2c

sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo adduser pi i2c
x reboot

sudo i2cdetect l
sudo i2cdetect -l
sudo i2cdetect -y 1 
sudo i2cdetect -F 1

ddc/ci python
https://gist.github.com/vdcrim/1964cd4247d6dbd01037
https://github.com/Informatic/python-ddcci
https://pythonexample.com/snippet/ddc-cipy_mchubby_python

http://sanki.imediabank.com/Docs-and-Samples/gpio-script/i2c/i2c-python
https://www.ptt.cc/bbs/Soft_Job/M.1244996101.A.8AE.html
https://www.raspberrypi.org/forums/viewtopic.php?f=44&t=144363
https://github.com/rockowitz/ddcutil
http://www.ddcutil.com/
http://www.ddcutil.com/raspberry/
http://boichat.ch/nicolas/ddcci/index-old.html
https://github.com/rockowitz/ddcutil/issues/14

http://atceiling.blogspot.tw/2014/01/raspberry-pigpio.html
https://sites.google.com/site/zsgititit/home/raspberry-shu-mei-pai/raspberry-qi-yongi2c-yuspi
https://coldnew.github.io/f0528f55/
http://0975128810.blogspot.tw/2016/01/raspberry-i2c.html
http://ajack-note.blogspot.tw/2015/11/i2c-on-raspberry-pi-2.html
https://hazy.today/1421-%E8%A9%A6%E7%94%A8%20Raspberry%20Pi%EF%BC%9A%E8%A9%A6%E7%94%A8%20I2C%2016x2%20LCD%20%E9%A1%AF%E7%A4%BA%E5%99%A8/

#----------------------------------------


https://sourceforge.net/p/zbar/code/ci/default/tree/python/
ng http://atceiling.blogspot.tw/2017/03/raspberry-pi-zbar.html


python setup.py install path Raspberry pi
modify sys.path python
uninstall zbar pi
Raspberry Pi：移除掉沒用到的套件
以底下指令來移除套件，IBM的Node-RED、Mathematica、Scratch。
$ sudo apt-get remove --purge --auto-remove nodered wolfram-engine scratch 

sudo pip install sightmachine-SimpleCV-1.3-913-g6c4d61b.zip

How to change sys.path or PYTHONPATH in Python
http://ask.xmodulo.com/change-syspath-pythonpath-python.html
import sys
print(sys.path)

import sys
sys.path.append('/custom/path/to/modules')
. . .
import <your-python-module>

export PYTHONPATH=$PYTHONPATH:/custom/path/to/modules

$ PYTHONPATH=$PYTHONPATH:/custom/path/to/modules python <your-program>


如何在Python中更改sys.path或PYTHONPATH
發表於 2015年12月8日由丹南妮	1評論
問題：當我運行一個Python應用程序時，它無法找到一個導入的模塊並失敗。看起來，Python模塊的目錄不包含在Python解釋器使用的默認sys.path中。我如何更改Python中的默認sys.path？
當Python解釋器執行導入模塊的程序時，它將檢查sys.path中列出的所有目錄路徑，直到找到該模塊。默認情況下，sys.path被構造為（1）當前工作目錄，（2）PYTHONPATH環境變量的內容，以及（3）由安裝的Python解釋器提供的一組缺省路徑。
如果您正在嘗試導入的模塊在sys.path中定義的任何目錄中都找不到，則會遇到“ 導入錯誤：No module named XXXXX ”錯誤。出現此錯誤的原因可能是您的系統上確實缺少模塊，或者是因為sys.path沒有指向模塊的安裝目錄。在後一種情況下，您需要讓Python解釋器知道模塊的位置。這裡是如何改變你的Python解釋器的sys.path。
方法一
第一種方法是顯式更改Python程序中的sys.path。
您可以按如下方式檢查當前sys.path的內容。
1
2	import sys
print(sys.path)
一旦你發現sys.path沒有包含必要的模塊目錄（例如/ custom / path / to / modules），你可以通過在import語句前添加下面的行來合併目錄。


1
2
3
4	import sys
sys.path.append('/custom/path/to/modules')
. . .
import <your-python-module>

方法二
或者，您可以在PYTHONPATH環境變量中添加自定義模塊目錄，這將增加Python解釋器使用的默認模塊搜索路徑。
將以下行添加到〜/ .bashrc中，這將會在Python中永久更改sys.path。
1	export PYTHONPATH=$PYTHONPATH:/custom/path/to/modules
指定的路徑將被添加到當前工作目錄之後的sys.path中，但在默認的解釋器提供的路徑之前。
如果要暫時更改PYTHONPATH變量，則可以使用以下命令。
$ PYTHONPATH = $ PYTHONPATH：/ custom / path / to / modules python <your-program>
 














































http://ask.xmodulo.com/change-syspath-pythonpath-python.html
import sys
sys.path.append('/custom/path/to/modules')
. . .
import <your-python-module>


Method Two
Alternatively, you can add the custom module directory in PYTHONPATH environment variable, which will augment the default module search paths used by the Python interpreter.

Add the following line to ~/.bashrc, which will have the effect of changing sys.path in Python permanently.

1. export PYTHONPATH=$PYTHONPATH:/custom/path/to/modules
The specified path will be added to sys.path after the current working directory, but before the default interpreter-supplied paths.

If you want to change PYTHONPATH variable temporarily, you can use the following command instead.

$ PYTHONPATH=$PYTHONPATH:/custom/path/to/modules python <your-program>

export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/dist-packages/zbar-0.10.dist-info


工作站安裝 python package 教學
大部份的python package 安裝都很簡單，只要執行

python setup.py install

就可以了，可是這個指令會把一些檔案copy 到/lib/ 之類需要有root權限才能讀寫的資料夾， 一般的user 不會有這個權限，但是只要加上 prefix 後就可以自由選擇安裝路徑

python setup.py install –prefix=/home/student/00/b00902001/python-packages/package-name

這樣library 檔就會裝到/home/student/00/b00902001/python-packages/package-name 裡面了，但是因為路徑是自己設的，所以這時候如果在python 裡面直接import，會顯示出錯誤訊息，告訴你沒有這個module。這時我們要記得

export PYTHONPATH=$HOME/python-packages/package-name/lib/python2.7/site-packages/:$PYTHONPATH

然後python 就會知道要去這個路徑找我們要的module 了，當然我們也可以把這個指令放在.bashrc 之類的地方，這樣每次重新登入的時候，package path 就會自動被加到PYTHONPATH中了。



列出設定 Python path
$ python -c 'import sys; print(sys.path)'


pi@raspberrypi:~ $ python -c 'import sys; print(sys.path)'
['', '/app/.apt/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-arm-linux-gnueabihf', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/home/pi/.local/lib/python2.7/site-packages', '/usr/local/lib/python2.7/dist-packages', '/home/pi/Code/SimpleCV', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/python2.7/dist-packages/wx-2.8-gtk2-unicode']
pi@raspberrypi:~ $ 


/home/pi/zbar-0.10/build/include/zbar
/home/pi/zbar-0.10/build/share/zbar
/home/pi/zbar-0.10/build/share/doc/zbar
/home/pi/zbar-0.10/perl/ZBar
/home/pi/zbar-0.10/zbar
/home/pi/zbar-0.10/include/zbar
/usr/include/zbar





Raspberry Pi：移除掉沒用到的套件
不過，因為下載的套件檔仍在，試著清除吧，也移除掉因相依關係而自動安裝的套件：
$ sudo apt-get clean
$ sudo apt-get autoremove --purge

以底下指令來移除套件，IBM的Node-RED、Mathematica、Scratch、Sonic Pi、Minecraft Pi。
$ sudo apt-get remove --purge --auto-remove nodered wolfram-engine scratch sonic-pi minecraft-pi





設定 PYTHONPATH 方便開發 package
由於開發 python package 時，常常看別人如此寫著:

from <package_name>.<subdir> import OOXX
問題是，如果不邊開發邊把 package 安裝在 site-packages 裡，該怎麼辦呢？ 就來設定 PYTHONPATH 吧:

export PYTHONPATH=.:/usr/local/lib/python2.6:/usr/local/lib/python2.6/site-packages:<NEW_PACKAGE_PATH> # zsh, bash, ...
setenv PYTHONPATH .:/usr/local/lib/python2.6:/usr/local/lib/python2.6/site-packages:<NEW_PACKAGE_PATH> # csh, tcsh...


列出、設定 Python 套件 Include Path
https://blog.longwin.com.tw/2014/08/list-set-python-package-include-path-2014/



列出、設定 Python 套件 Include Path

Python 套件載入的路徑可以用下述方式查看:


import sys
print (sys.path) # 這邊就會印出來有哪些 path

另外也可以於 Shell 另外設定 PYTHONPATH 的參數, ex:

export PYTHONPATH=/實體完整路徑/path/your/module

範例

1. mkdir /tmp/pythonlib
2. export PYTHONPATH=/tmp/pythonlib
3. vim /tmp/pythonlib/d.py

View Raw Code?
#!/usr/bin/python
# -*- coding: utf-8 -*-
print "hello"

4. chmod +x /tmp/pythonlib/d.py
5. vim /tmp/a.py

View Raw Code?
import d

6. cd /tmp
7. python a.py # 會印出 "hello"






Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> print sys.path
SyntaxError: Missing parentheses in call to 'print'
>>> print (sys.path)
['', '/home/pi', '/usr/bin', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-arm-linux-gnueabihf', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']
>>> 
















command "/usr/bin/python -c "import setuptools, tokenize;__file__='/tmp/pip-build-mzukaq/zbar/setup.py';exec(compile(getattr(tokenize, 'open', open) (__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-jixrjt-record/install-record.txt --single-version-externally-managed --compile" failed error code 1 in /tmp/pip-build-mzukaq/zbar
did install:

code: select all

sudo apt-get install python-zbar
tutorial says?


raspberrypi




sudo apt-get install python-qrtools

sudo apt-get install zbar-tools
sudo apt-get install libzbar-dev
sudo apt-get install python-zbar


>>> import zbar
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named zbar



heroku config:add PYTHONPATH=/app/.apt/usr/lib/python2.7/dist-packages/


import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')




export PYTHONPATH=/app/.apt/usr/lib/python2.7/dist-packages/



http://yehnan.blogspot.tw/2015/12/raspberry-piraspbianopencv.html

嗯，因為/usr/local/lib/...不是Python預設的模組搜尋路徑，所以要自己加，

你可以設定環境變數PYTHONPATH，把/usr/local/lib/python2.7/site-packages放進去，

修改適當的.pth檔，詳情請參閱官方文件 https://docs.python.org/2/library/site.html




sudo apt-get install libzbar-dev

sudo pip install zbar


-------------------------------------------------------------------------------




-----------------------------------------------------------------------------
en US UTF-8


zh TW EUC-TW
Asia Taipei
TW


https://github.com/jabelone/OpenCV-for-Pi


https://www.raspberrypi.com.tw/tag/opencv/


http://yehnan.blogspot.tw/2015/12/raspberry-piraspbianopencv.html


http://www.powenko.com/wordpress/?p=9180


http://scout-jj.blogspot.tw/2015/04/raspberry-pi-raspberry-pi-opencv.html


https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/




https://github.com/milq/milq/blob/master/scripts/bash/install-opencv.sh






https://blog.gtwang.org/iot/raspberry-pi-install-opencv/


--------------------------------------
https://blog.gtwang.org/iot/raspberry-pi/how-to-diy-home-alarm-system-with-raspberry-pi-and-webcam/


如果權限沒有設定好，會造成 motion 中止執行。


檢查 motion 系統服務的狀態：
service motion status
由於 motion 預設會將圖片與影片的輸出儲存於 /var/lib/motion 中，但是 motion 帳號這個沒有該目錄的寫入權限，我們要自行將這個目錄的擁有者改為 motion：
sudo chown motion:motion /var/lib/motion
-------------------------------


https://blog.gtwang.org/iot/raspberry-pi-usb-webcam/
















[感謝祭，有下有推]Raspbian openCV img 檔下載 – 可用於 Raspberry Pi B、B+ 以及 Banana Pi


http://blog.cavedu.com/%E7%89%A9%E8%81%AF%E7%B6%B2/raspberrypi-%E5%96%AE%E6%9D%BF%E9%9B%BB%E8%85%A6/%E6%84%9F%E8%AC%9D%E7%A5%AD%EF%BC%8C%E6%9C%89%E4%B8%8B%E6%9C%89%E6%8E%A8raspbian-opencv-img-%E6%AA%94%E4%B8%8B%E8%BC%89-%E5%8F%AF%E7%94%A8%E6%96%BC-raspberry-pi-b%E3%80%81b-%E4%BB%A5%E5%8F%8A-ban/




https://www.google.com.tw/search?q=raspberry+pi+3+b+opencv+img&source=lnt&tbs=ctr:countryTW&cr=countryTW&sa=X&ved=0ahUKEwin3ubbq7HYAhVDxLwKHVnyDCIQpwUIHg&biw=1280&bih=541


https://github.com/Tes3awy/OpenCV-3.2.0-Compiling-on-Raspberry-Pi






http://storychen.blogspot.tw/2016/06/raspberry-pi-3-opencv.html
https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/




http://storychen.blogspot.tw/search/label/Raspberry%20Pi?updated-max=2016-06-07T20:22:00%2B08:00&max-results=20&start=8&by-date=false
----------------------------------


可以做出像Windows的批次檔


棓麔楈琣抻 .sh


$ sh int1.sh


---------------------------
https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/


https://www.pyimagesearch.com/practical-python-opencv/?src=pi-opencv-install






xxxxxxxxxxxxxxxxxx======================
https://imaginghub.com/projects/144-installing-opencv-3-on-raspberry-pi-3?gclid=CjwKCAiA7JfSBRBrEiwA1DWSG9e6BMAwoxsxyowHxDvMALaElPp1u-Wx_nZDZ6DaRFVyDUYgyR6_WxoC_f8QAvD_BwE#documentation




sudo apt-get update
sudo apt-get dist-upgrade


xxx
sudo raspi-update


chg to
sudo raspi-config
update


sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3-dev


cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
unzip opencv_contrib.zip




wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py


pip install numpy










xxxxxxxxxxxxxxxxxx======================