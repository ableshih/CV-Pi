Gerrit 系統的搭建

http://mqjing.blogspot.tw/2016/09/gerrit-code-review-server.html

https://blog.miniasp.com/post/2008/03/02/Open-relay-for-localhost-when-using-IIS-SMTP-Service-at-the-first-time.aspx



https://blog.csdn.net/zyaiwmy/article/details/54617544
https://blog.csdn.net/u013686019/article/details/54382231

https://blog.csdn.net/hudashi/article/details/54668359

https://blog.csdn.net/melody157398/article/details/39894975

https://blog.csdn.net/wangjicong_215/article/details/77800082
https://blog.csdn.net/u012769691/article/details/50214825

https://blog.csdn.net/tq08g2z/article/details/78627653

https://gerrit-review.googlesource.com/Documentation/config-gerrit.html

https://www.packtpub.com/mapt/book/application_development/9781783289479/3/ch03lvl1sec24/active-directory

http://chuquan.me/2017/12/12/ubuntu-gerrit-apache/

https://blog.csdn.net/Leo_ZN_0/article/details/79532827

https://blog.csdn.net/Coder80/article/details/48176559

https://www.wolfcstech.com/2017/11/24/gerrit_codereview/

https://blog.csdn.net/alittleyatou/article/details/52485259

https://stackoverflow.com/questions/10447520/gerrit-and-active-directory



https://books.google.com.tw/books?id=D_GqyR27Jw4C&pg=PT91&lpg=PT91&dq=gerrit+code+review+Active+Directory&source=bl&ots=tso6diBqa2&sig=SqhWc42YsXFIGts5NB9roDoWHyo&hl=zh-TW&sa=X&ved=0ahUKEwiKvfSdrPDaAhWFmJQKHfD7BFcQ6AEIcTAH#v=onepage&q=gerrit%20code%20review%20Active%20Directory&f=false

---------------------

authentication method ldap gerrit windows

https://blog.csdn.net/deyili/article/details/79422500

http://www.itread01.com/content/1508838031.html

http://www.cnblogs.com/kevingrace/p/5624122.html

http://www.itread01.com/articles/1476185404.html

https://hk.saowen.com/a/3516dfac3dc2d69cd3f7920640a0d049605c0a7717d10f9877008dae4c82dc21

https://www.dayexie.com/detail429094.html

https://www.gaott.info/install-gerrit-ldap-gitweb-mysql-on-centos-7/

https://blog.csdn.net/wulinxiangzhu/article/details/77743786

https://blog.csdn.net/wulinxiangzhu/article/details/77742758

https://blog.csdn.net/mr_raptor/article/details/77337710

http://stackoverflow.org.cn/front/ask/view?ask_id=492073

http://www.worldhello.net/gotgit/05-git-server/055-gerrit.html



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

=======================================================================================

Microsoft Windows [版本 10.0.16299.371]
(c) 2017 Microsoft Corporation. 著作權所有，並保留一切權利。

C:\Users\5578>cd\gitweb

C:\gitweb>path
PATH=C:\gitweb\Apache24\bin;C:\gitweb\OpenSSH-Win64;C:\tools\msys64;C:\Python27\;C:\Program Files\Java\jdk-10.0.1\bin;C:\ProgramData\chocolatey\bin;C:\Python27\Scripts;C:\Program Files\Java\jre-10.0.1\bin;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\iCLS\;C:\Program Files\Intel\Intel(R) Management Engine Components\iCLS\;C:\Program Files\Python36\Scripts\;C:\Program Files\Python36\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\PuTTY\;C:\ProgramData\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Users\5578\AppData\Local\Microsoft\WindowsApps;C:\Program Files\Git\cmd;C:\Users\5578\AppData\Local\Microsoft\WindowsApps;C:\ProgramData\chocolatey\lib\msys2;C:\tools\msys64;

C:\gitweb>Java -jar gerrit.war init -d  c:/gitweb/gerrit
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by com.google.inject.internal.cglib.core.$ReflectUtils$1 (file:/C:/Users/5578/.gerritcodereview/tmp/gerrit_6452764980244851884_app/guice-4.1.0.jar) to method java.lang.ClassLoader.defineClass(java.lang.String,byte[],int,int,java.security.ProtectionDomain)
WARNING: Please consider reporting this to the maintainers of com.google.inject.internal.cglib.core.$ReflectUtils$1
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
Using secure store: com.google.gerrit.server.securestore.DefaultSecureStore
[2018-04-30 22:28:09,765] [main] INFO  com.google.gerrit.server.config.GerritServerConfigProvider : No c:\gitweb\gerrit\etc\gerrit.config; assuming defaults

*** Gerrit Code Review 2.15.1
***

Create 'c:\gitweb\gerrit'      [Y/n]? y

*** Git Repositories
***

Location of Git repositories   [git]:

*** SQL Database
***

Database server type           [h2]: mysql

Gerrit Code Review is not shipped with MySQL Connector/J 5.1.43
**  This library is required for your configuration. **
Download and install it now [Y/n]? y
Downloading https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.43/mysql-connector-java-5.1.43.jar ... OK
Checksum mysql-connector-java-5.1.43.jar OK
Server hostname                [localhost]:
Server port                    [(mysql default)]:
Database name                  [reviewdb]:
Database username              [5578]:
5578's password                :
              confirm password :

*** NoteDb Database
***

Use NoteDb for change metadata?
  See documentation:
  https://gerrit-review.googlesource.com/Documentation/note-db.html
Enable                         [Y/n]? y

*** Index
***

Type                           [lucene/?]:

*** User Authentication
***

Authentication method          [openid/?]:
Enable signed push support     [y/N]? y

*** Review Labels
***

Install Verified label         [y/N]? y

*** Email Delivery
***

SMTP server hostname           [localhost]:
SMTP server port               [(default)]:
SMTP encryption                [none/?]:
SMTP username                  :

*** Container Process
***

Run as                         [5578]:
Java runtime                   [C:\Program Files\Java\jdk-10.0.1]:
Copy gerrit.war to c:\gitweb\gerrit\bin\gerrit.war [Y/n]? y
Copying gerrit.war to c:\gitweb\gerrit\bin\gerrit.war

*** SSH Daemon
***

Listen on address              [*]:
Listen on port                 [29418]:
Generating SSH host key ... rsa... dsa... ed25519... ecdsa 256... ecdsa 384... ecdsa 521... done

*** HTTP Daemon
***

Behind reverse proxy           [y/N]?
Use SSL (https://)             [y/N]?
Listen on address              [*]:
Listen on port                 [8080]:
Canonical URL                  [http://DESKTOP-5578.mshome.net:8080/]:

*** Cache
***


*** Plugins
***

Installing plugins.
Install plugin commit-message-length-validator version v2.15.1 [y/N]? y
Installed commit-message-length-validator v2.15.1
Install plugin download-commands version v2.15.1 [y/N]? y
Installed download-commands v2.15.1
Install plugin hooks version v2.15.1 [y/N]? y
Installed hooks v2.15.1
Install plugin replication version v2.15.1 [y/N]? y
Installed replication v2.15.1
Install plugin reviewnotes version v2.15.1 [y/N]? y
Installed reviewnotes v2.15.1
Install plugin singleusergroup version v2.15.1 [y/N]? y
Installed singleusergroup v2.15.1
Initializing plugins.

*** Experimental features
***

Enable any experimental features [y/N]? y
Default to PolyGerrit UI       [Y/n]? y
Enable GWT UI                  [Y/n]? y

fatal: DbInjector failed
fatal: Unable to determine SqlDialect
fatal:   caused by com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
fatal:
fatal: The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
fatal:   caused by java.net.ConnectException: Connection refused: connect

C:\gitweb>

