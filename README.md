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





---

# 樹莓派
## image
    image to SD
## 開終端機
    預設帳號 pi 密碼 raspberry
    raspi-config 環境設定
## 指令
    date 時間
    cal 行事歷
    df 查 SD 空間
    free 查記憶體
    exit 關終端機
    shutdown -h now 立即關機
    ls (dir)
    cp (copy)
    mv (move)
    rm (del)
    nano filename.txt 文字編輯器
    mkdir 建目錄
    chmod 664 filename.txt (檔案權限 r.w.x)
    passwd 舊 新 新 (改密碼)
    sudo apt-get update
    sudo apt-get upgrade
    host name 查看 IP addr.
## 開機自動執行
    sudo nano /etc/rc.local
        在第一行加入
            /usr/bin/python /home/pi/hmtt.py
## 指令1
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get dist-upgrade
$ sudo rpi-update
$ sudo reboot
## kernel version check
uname -a
## 硬體比較
    https://3q.9527.tw/123
## 樹莓派4問題USB-C無法充電
## 調整 SD 大小
    樹莓 icon
        偏好設定
            GParted
                調整
                    套用所有動作
                        會 自動重開機 
## 忘記密碼
    將樹莓派關機，移除sd卡，插入到你的電腦。
    在PC上打開SD卡根目錄，啟動部分是可見的，並包含一個名為“cmdline.txt”的文件。
    用編輯軟體編輯，於內容最後加入 init=/bin/sh
    保存，將sd卡插入樹莓派
    mount -o remount, rw /
    passwd pi
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    sync
    exec /sbin/init
    樹莓派會繼續啟動，然後關掉樹莓派並且斷電。
    sudo halt
    用電腦再次編輯“cmdline.txt” 刪除 init=/bin/sh 存檔
    插入sd卡到你的樹莓派啦，再次啟動就可以使用新的密碼啦。
## Raspberry Pi - 調整SD分割空間
## 安裝 ubnutu 要非常久，不建議

