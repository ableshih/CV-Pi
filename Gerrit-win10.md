
---------------------------------------------------
# 申請
---------------------------------------------------
## OA 桌機

## 查出 mac addr 
```cmd -> ipconfig/all ```

## 申請 固定 IP

## 得到固定IP，才申請 DNS 域名

## 在申請 SMTP relay

SSL (內網只要用本機 IIS 依 MIS SOP 自行簽署一簽五年，要對外要外購。)
反向代理伺服器 (要給公司以外人員)

---------------------------------------------------
# 硬體
---------------------------------------------------
## OA 系統



---------------------------------------------------
# 安裝
---------------------------------------------------
## 依 MIS SOP 安 IIS 取得 憑證

## 進 IIS 將憑證匯出到檔案 *.crt *.key

===========

## java

## git

## TortoiseGit

===========

## 選用 XAMPP (使用 XAMPP 可一次架好 Apache Mysql phpadmin，)

===========



# gerrit 用法
## install
```
java -jar .\gerrit-2.15.1.war init
```
## 起動
```
java -jar .\bin\gerrit.war daemon --console-log
```
===========

## 開 proxy

## gerrit 加掛 plugin

===========

## 加到開機後自動啟用 服務

commons-daemon-1.1.0-bin-windows.zip

## unzip

## copy *.exe to C:\web\Apache24\bin
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
===========





