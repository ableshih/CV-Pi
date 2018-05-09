OA 系統

參照 https://blog.csdn.net/deyili/article/details/79422500
-----------------------------------

-----------------------------------
先申請固定 IP

固定 IP 下來後，申請 DNS

SMTP relay 

-----------------------------------


-----------------------------------


-----------------------------------

1. java
download
https://www.java.com/zh_TW/download/windows-64bit.jsp

install
jre-8u171-windows-x64.exe

add path

test java
cmd
java -version
-----------------------------------

2. apache
download
https://httpd.apache.org/docs/current/platform/windows.html#down
https://www.apachehaus.com/cgi-bin/download.plx
http://www.apachehaus.com/downloads/httpd-2.4.33-o102o-x64-vc14-r2.zip
httpd-2.4.33-o102o-x64-vc14-r2.zip

add web folder

unzip to web folder
-----------------------------------

3. gerrit
download
https://www.gerritcodereview.com/
https://www.gerritcodereview.com/download/
gerrit-2.15.1.war

rename gerrit-2.15.1.war gerrit.war
copy to web folder


-----------------------------------






-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------
port folder
http://pclevin.blogspot.tw/2016/03/apache-httpd-virtualhost.html

 <VirtualHost *:8081>
  DocumentRoot "D:/Apache24/htdocs"
  ServerName localhost
 </VirtualHost>

 <VirtualHost *:8081>
  DocumentRoot "D:/Apache24/test/www/example1"
  ServerName www.test1.com
 </VirtualHost>

 <VirtualHost *:8081>
  DocumentRoot "D:/Apache24/test/www/example2"
  ServerName www.test2.com
 </VirtualHost>
 
  DocumentRoot 需配合 Directory，一個配一個

 <Directory "D:/Apache24/test/www/example1">
  Options Indexes FollowSymLinks
  AllowOverride None
  Require all granted
 </Directory>
 <Directory "D:/Apache24/test/www/example2">
  Options Indexes FollowSymLinks
  AllowOverride None
  Require all granted
 </Directory>
 
-----------------------------------

