OA 桌機


# 申請
---------------------------------------------------
## 1. 查出 mac addr

```cmd -> ipconfig/all ```

## 2. 申請 固定 IP

## 3. 得到固定IP，才申請 DNS 域名

## 4. 在申請 SMTP relay

## SSL (內網只要用本機 IIS 依 MIS SOP 自行簽署一簽五年，要對外要外購。)
## 反向代理伺服器 (要給公司以外人員)


# 硬體
---------------------------------------------------
## OA 系統




# 安裝
---------------------------------------------------
## 憑證

### 1. 依 MIS SOP 安 IIS 取得 憑證

### 2. 進 IIS 將憑證匯出到檔案 *.crt *.key




## 1. java
https://www.java.com/zh_TW/download/windows-64bit.jsp

x64 C:\Program Files\Java\jre1.8.0_171\bin\server\jvm.dll

x32 C:\Program Files (x86)\Java\jre1.8.0_171\bin\client\jvm.dll

```cmd -> java -version```

## 2. git
https://git-scm.com/download/win

https://github.com/git-for-windows/git/releases/download/v2.17.1.windows.2/Git-2.17.1.2-64-bit.exe

## 3. TortoiseGit
https://tortoisegit.org/download/

https://download.tortoisegit.org/tgit/2.6.0.0/TortoiseGit-2.6.0.0-64bit.msi



## 4. 選用 XAMPP (使用 XAMPP 可一次架好 Apache Mysql phpMyAdmin )

https://www.apachefriends.org/download.html

xampp-win32-7.2.5-0-VC15-installer.exe


## 5. MySQL 建資料庫
```
  mysql

  CREATE USER 'gerrit'@'localhost' IDENTIFIED BY 'secret';
  CREATE DATABASE reviewdb DEFAULT CHARACTER SET 'utf8';
  GRANT ALL ON reviewdb.* TO 'gerrit'@'localhost';
  FLUSH PRIVILEGES;
```

## 6. gerrit 用法
https://www.gerritcodereview.com/

https://www.gerritcodereview.com/download/gerrit-2.15.2.war

### install
```
java -jar .\gerrit-2.15.1.war init
```
### 起動
```
java -jar .\bin\gerrit.war daemon --console-log
```

### 安裝說明
https://gerrit-documentation.storage.googleapis.com/Documentation/2.15.2/install.html

https://gerrit-documentation.storage.googleapis.com/Documentation/2.15.2/install.html#installation_on_windows



## 開 proxy

## gerrit 加掛 plugin
直接 copy 檔案到目錄裡


## 7. 加到開機後自動啟用 服務

commons-daemon-1.1.0-bin-windows.zip

## unzip

## copy *.exe to C:\Apache24\bin
```
PS D:\ddgit\Gerrit> prunsrv.exe //IS//Gerrit --DisplayName="Gerrit Code Review" --Startup=auto --Jvm="C:\Program Files (
x86)\Java\jre1.8.0_171\bin\client\jvm.dll" --Classpath=D:\ddgit\GERRIT\bin\gerrit.war --LogPath=D:\ddgit\GERRIT\logs --S
tartPath=D:\ddgit\GERRIT --StartMode=jvm --StopMode=jvm --StartClass=com.google.gerrit.launcher.GerritLauncher --StartMe
thod=daemonStart --StopClass=com.google.gerrit.launcher.GerritLauncher --StopMethod=daemonStop
```
## prunsrv 用法
```
PS D:\ddgit\Gerrit> prunsrv.exe //DS//Gerrit 

IS install
DS del
```

## 另一方法
建捷徑 copy 到啟動

win+R

```shell:Common Startup```

C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup







