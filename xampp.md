---------------------

# git (內含 ssh-keygen)

#### https://gitforwindows.org/
---------------------
# java 
## (gerrit 是由 java 所開發其副檔名為 war 安裝時需使用 java 執行)
```
https://www.java.com/zh_TW/
https://www.java.com/zh_TW/download/windows-64bit.jsp
http://javadl.oracle.com/webapps/download/AutoDL?BundleId=233172_512cd62ec5174c3487ac17c61aaa89e8
jre-8u171-windows-x64.exe
```
---------------------

# XAMPP install (Gerrit 需 Apache and Mysql 所以只要安裝 XAMPP 就包含)

## download and install
```
https://www.apachefriends.org/zh_tw/index.html
```
## change password 設定MySQL 的root 密碼
```
http://localhost/phpmyadmin/server_privileges.php?viewing_mode=server
```
---------------------
# ADD mysql DATA BASES

#### https://gerrit-review.googlesource.com/Documentation/install.html#createdb_mysql
```
http://localhost/phpmyadmin/server_sql.php

貼上
CREATE USER 'gerrit'@'localhost' IDENTIFIED BY 'secret';
CREATE DATABASE reviewdb DEFAULT CHARACTER SET 'utf8';
GRANT ALL ON reviewdb.* TO 'gerrit'@'localhost';
FLUSH PRIVILEGES;
執行
```

## check data bases
```
http://localhost/phpmyadmin/server_databases.php

資料庫	reviewdb	
  
編碼與排序  utf8_general_ci
```

## check user
```
http://localhost/phpmyadmin/server_privileges.php?viewing_mode=server

使用者帳號 'gerrit'@'localhost'

```

---------------------
## xampp start on boot windows

### Apache
```
Run cmd as Administrator
Go to apache bin direcotry, eg.: C:\xampp\apache\bin
Run: httpd.exe -k install more info
Restart comp, or run service manually (from services.msc)
```
### MySQL
```
Run cmd as Administrator
Go to apache bin direcotry, eg.: C:\xampp\mysql\bin
Run: mysqld.exe --install more info
Restart comp, or run service manually (from services.msc)
```
## or 建立捷徑
```
C:\Users\v570\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

C:\xampp\xampp-control.exe
```
---------------------
# Download Gerrit
#### https://gerrit-review.googlesource.com/Documentation/install.html#download

---------------------
# Gerrit Installation on Windows
```
https://gerrit-review.googlesource.com/Documentation/install.html#installation_on_windows

```

#### https://www.gerritcodereview.com/download/gerrit-2.15.1.war
