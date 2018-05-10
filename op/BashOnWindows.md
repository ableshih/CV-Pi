安裝Bash on Windows

安裝VcXsrv並啟動XLaunch

download vcxsrv Vcxsrv link:https://sourceforge.net/projects/vcxsrv/
install vcxsrv
run XLaunch
setting vcxsrv in desktop XLaunch icon, setup display number to 0
run XLaunch <---常註
run bash
sudo apt-get install ubuntu-desktop unity compizconfig-settings-manager
export DISPLAY=:0 
dconf reset -f /org/compiz/ 
unity --reset-icons
echo "export DISPLAY=:0.0" >> ~/.bashrc
sudo sed -i 's$<listen>.*</listen>$<listen>tcp:host=localhost,port=0</listen>$' /etc/dbus-1/session.conf

啟動Unity桌面
在bash中輸入：compiz


---------------------------------------------
阿三的方法 https://www.youtube.com/watch?v=GxeabWuqjLQ

download vcxsrv Vcxsrv link:https://sourceforge.net/projects/vcxsrv/
install vcxsrv
setting vcxsrv in desktop XLaunch icon, setup display number to 0
run bash
apt-get install xfce4
xfce4-session <---這行開始

可作可不作
設定 個人化 工作列 在電腦模式中自動隱藏工作列


----------------------------------
windows 10 中的 ubuntu 子系統安裝桌面環境的方法
大陸 https://blog.csdn.net/u011138447/article/details/78262369

download vcxsrv Vcxsrv link:https://sourceforge.net/projects/vcxsrv/
install vcxsrv
setting vcxsrv in desktop XLaunch icon, setup display number to 0

run bash
sudo apt-get install ubuntu-desktop unity compizconfig-settings-manager
約 2.5gb 要跑很久

sudo apt-get install compizconfig-settings-manager
DISPLAY=:0 ccsm


run XLaunch <---常註


sudo apt-get install xfce4-session
xfce4-session



export  DISPLAY=localhost:0
ccsm



locale-gen zh_TW.UTF-8  
locale-gen  
locale  

舉報回复
en_us.utf-8

sudo apt-get install gtk2-engines-murrine gtk2-engines-pixbuf gtk3-engines-unico
sudo apt-get install gtk-chtheme
sudo apt-get install gtk-theme-switch gtk-theme-switch2 thewidgetfactory


sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade



