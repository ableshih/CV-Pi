# ---------------------------------------------------------
# For RaspberryPi

# 安裝
Install_OpenCV_RaspberryPi

# 螢幕保護
PiScreenSaver

# 書本範例
MP31717_Ex

# 遙控
RaspberryPi-PuTTY

# 從 Windows 傳送檔案到樹莓派
WinFiles-to-Pi

# ---------------------------------------------------------

# For Windows

# 用 Visual Studio 2015 配 OpenCV 3.4 建開發環境
VS-CV

# 攝影機
Pi-Camera

# ---------------------------------------------------------

# git
github 建目錄
點擊“create new file”的按鈕
輸入目錄名稱 後加斜杠“/”

#可以做出像Windows的批次檔
$ sh int1.sh

#---Raspberry Pi 與 Ubuntu--------
Raspberry Pi 列出所有已安裝套件 dpkg --get-selections
$ dpkg --get-selections > installed_packages.txt
用 dpkg 指令查詢已安裝套件清單

Raspberry Pi 移除套件，Node-RED、Scratch。
$ sudo apt-get remove --purge --auto-remove nodered scratch

#---------常用程式
http://yehnan.blogspot.tw/2014/02/raspberry-piraspbian.html


Raspberry Pi：Raspbian編譯OpenCV原始碼 
http://yehnan.blogspot.tw/2015/12/raspberry-piraspbianopencv.html

raspberry指令
http://yhhuang1966.blogspot.tw/2014/02/linux.html
http://a0918513696.pixnet.net/blog/post/182492081-%5Braspberry-pi%5D%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4-%E9%99%B8%E7%BA%8C%E5%A2%9E%E5%8A%A0
http://storychen.blogspot.tw/2016/06/raspberry-pi-3-linux.html
https://www.raspberrypi.org/documentation/linux/usage/commands.md

檢查服務、元件及目前載入的核心模組
lsmod

檢查網路
iwconfig

檢查藍芽
hciconfig
藍芽驅動
apt-cache show pi-bluetooth

設定系統自動校時
sudo timedatectl set-ntp yes
檢查時間設定
timedatectl

apt-get 指令一覽
http://nathan-inlinux.blogspot.tw/2013/05/apt-get.html
#----------------------
apt裝完套件後 要怎樣才能查詢到 他們是被安裝到哪些目錄?
dpkg -L example


#--------
pip list
#-------
opencv zbar c++
http://blog.csdn.net/dcrmg/article/details/52132313
http://blog.csdn.net/cjj1130320082/article/details/52027214
http://blog.csdn.net/nick123chao/article/details/77573675
http://blog.csdn.net/jia20003/article/details/77348170
http://blog.csdn.net/dcrmg/article/details/52195999




http://storychen.blogspot.tw/2016/06/raspberry-pi-3-opencv.html

http://glophy.com/Python/python_note.html
