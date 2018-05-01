Gerrit 系統的搭建

一、安裝Apache

下載Apache:
https://www.apachehaus.com/cgi-bin/download.plx?dli=gWrR2dOtWQ04ERBtmVYhWTKVlUGR1Uwp3VYpFb

綠色軟件，不用安裝，解壓縮即可。
我的目錄是：c:\gitweb\Apache24。
修改文件Apache24\conf\httpd.conf，如下：
------------------
#Define SRVROOT "/Apache24"
定義SRVROOT "c:/gitweb/Apache24"

ServerName localhost:8080

Listen 8080
-------------------


將目錄 c:\gitweb\Apache24\bin 放在系統環境變量（$PATH）裡

cmd
httpd

new a one cmd
httpd.exe -k install -n "apache_service" -f "C:\gitweb\Apache24\conf\httpd.conf"

關 cmd

new cmd
httpd <---啟動指令(關閉 cmd server就關閉)

瀏覽器地址欄輸入：127.0.0.1:8080 可以看到Apache Web服務器已經運行起來了

=====================================================

二、配置Gerrit

install java

Gerrit 需要用到Java和Git，这个不多说了，请自行安装。

----------ssh-keygen.exe
1.
---------------
download openssh (command line工具)
https://github.com/PowerShell/Win32-OpenSSH/releases/download/v7.6.1.0p1-Beta/OpenSSH-Win64.zip
unzip
add path
-----------
or 2.
add path
C:\Program Files\Git\usr\bin
--------------
下载最新版本 https://gerrit-releases.storage.googleapis.com/index.html 


Java -jar gerrit.war init -d  c:/gitweb/gerrit




http://desktop-5578.mshome.net:8080/


htpasswd -c -m c:/gitweb/config/gerrit_passwd aUser

