---------------------

# git
```
https://gitforwindows.org/
```
---------------------

# XAMPP install

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
```

## check user
```
http://localhost/phpmyadmin/server_privileges.php?viewing_mode=server
```
---------------------
# Gerrit Installation on Windows
```
https://gerrit-review.googlesource.com/Documentation/install.html#installation_on_windows

```
