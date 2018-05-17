---------------------

# git 
### (內含 ssh-keygen)

#### https://gitforwindows.org/
---------------------
# java 
### (gerrit 是由 java 所開發其副檔名為 war 安裝時需使用 java 執行)
```
https://www.java.com/zh_TW/

只能用 32
https://java.com/zh_TW/download/manual.jsp
http://javadl.oracle.com/webapps/download/AutoDL?BundleId=233170_512cd62ec5174c3487ac17c61aaa89e8
jre-8u171-windows-i586.exe
```

---------------------

# XAMPP install 
### (Gerrit 需 Apache and Mysql 所以只要安裝 XAMPP 就包含)

## download and install
```
https://www.apachefriends.org/zh_tw/index.html
```
## change password 設定MySQL 的root 密碼
```
http://localhost/phpmyadmin/server_privileges.php?viewing_mode=server
```
---------------------
## Database Setup (ADD mysql DATA BASES)

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

### Gerrit
```
加到開機後自動啟用 服務
PS C:\xampp\Gerrit> prunsrv.exe //IS//Gerrit --DisplayName="Gerrit Code Review" --Startup=auto --Jvm="C:\Program Files (
x86)\Java\jre1.8.0_171\bin\client\jvm.dll" --Classpath=C:\xampp\GERRIT\bin\gerrit.war --LogPath=C:\xampp\GERRIT\logs --S
tartPath=C:\xampp\GERRIT --StartMode=jvm --StopMode=jvm --StartClass=com.google.gerrit.launcher.GerritLauncher --StartMe
thod=daemonStart --StopClass=com.google.gerrit.launcher.GerritLauncher --StopMethod=daemonStop



C:\Program Files\Java\jre1.8.0_171\bin\server
```
#### prunsrv.exe (Apache 掛開機啟動的小程式)
```
https://www.apache.org/dist/commons/daemon/binaries/windows/
https://www.apache.org/dist/commons/daemon/binaries/windows/commons-daemon-1.1.0-bin-windows.zip
```
##### unzip to Apache C:\xampp\apache\bin
---------------------
# Download Gerrit
#### https://gerrit-review.googlesource.com/Documentation/install.html#download

---------------------

https://gerrit-review.googlesource.com/Documentation/install.html#init



# Gerrit Installation on Windows
```
https://gerrit-review.googlesource.com/Documentation/install.html#installation_on_windows

```

#### https://www.gerritcodereview.com/download/gerrit-2.15.1.war


## gerrit install

```
Windows PowerShell
著作權 (C) 2016 Microsoft Corporation. 著作權所有，並保留一切權利。

PS C:\Users\9709732> d:
PS D:\> cd .\ddgit\
PS D:\ddgit> cd .\Gerrit\
PS D:\ddgit\Gerrit> java -jar .\gerrit.war init
```
### MySql server 密碼要一樣



## gerrit 用法
```
install
java -jar .\gerrit.war init
```
## 起動
```
java -jar .\bin\gerrit.war daemon --console-log

127.0.0.1:8080

ctrl + c (exit)
```
## xx review
```
xx java -jar gerrit.war init -d review_site
```




































































































```
PS C:\xampp\Gerrit> java -jar gerrit.war init
Using secure store: com.google.gerrit.server.securestore.DefaultSecureStore

*** Gerrit Code Review 2.15.1
***


*** Git Repositories
***

Location of Git repositories   [git]:

*** SQL Database
***

Database server type           [mysql]: mysql
Server hostname                [localhost]:
Server port                    [3306]:
Database name                  [reviewdb]:
Database username              [gerrit2]:
Change gerrit2's password      [y/N]? y
gerrit2's password             :
              confirm password :

*** Index
***

Type                           [lucene/?]:

*** User Authentication
***

Authentication method          [openid/?]:
Enable signed push support     [y/N]?

*** Review Labels
***

Install Verified label         [y/N]?

*** Email Delivery
***

SMTP server hostname           [localhost]:
SMTP server port               [(default)]:
SMTP encryption                [none/?]:
SMTP username                  :

*** Container Process
***

Run as                         [v570]: gerrit2
Java runtime                   [C:\Program Files\Java\jre1.8.0_171]:
Upgrade .\bin\gerrit.war       [Y/n]?
Copying gerrit.war to .\bin\gerrit.war

*** SSH Daemon
***

Listen on address              [*]:
Listen on port                 [29418]:

*** HTTP Daemon
***

Behind reverse proxy           [y/N]?
Use SSL (https://)             [y/N]?
Listen on address              [*]:
Listen on port                 [8099]: 6267
Canonical URL                  [http://v570-PC:8080/]: http://localhost:6267/

*** Cache
***


*** Plugins
***

Installing plugins.
Install plugin commit-message-length-validator version v2.15.1 [Y/n]?
commit-message-length-validator v2.15.1 is already installed, overwrite it [Y/n]?
Updated commit-message-length-validator to v2.15.1
Install plugin download-commands version v2.15.1 [Y/n]?
download-commands v2.15.1 is already installed, overwrite it [Y/n]?
Updated download-commands to v2.15.1
Install plugin hooks version v2.15.1 [Y/n]?
hooks v2.15.1 is already installed, overwrite it [Y/n]?
Updated hooks to v2.15.1
Install plugin replication version v2.15.1 [Y/n]?
replication v2.15.1 is already installed, overwrite it [Y/n]?
Updated replication to v2.15.1
Install plugin reviewnotes version v2.15.1 [Y/n]?
reviewnotes v2.15.1 is already installed, overwrite it [Y/n]?
Updated reviewnotes to v2.15.1
Install plugin singleusergroup version v2.15.1 [Y/n]?
singleusergroup v2.15.1 is already installed, overwrite it [Y/n]?
Updated singleusergroup to v2.15.1
Initializing plugins.

*** Experimental features
***

Enable any experimental features [y/N]? y
Default to PolyGerrit UI       [Y/n]?
Enable GWT UI                  [Y/n]?

fatal: DbInjector failed
fatal: Unable to determine SqlDialect
fatal:   caused by java.sql.SQLException: Access denied for user 'gerrit2'@'localhost' (using password: YES)
PS C:\xampp\Gerrit> java -jar gerrit.war init
Using secure store: com.google.gerrit.server.securestore.DefaultSecureStore

*** Gerrit Code Review 2.15.1
***


*** Git Repositories
***

Location of Git repositories   [git]:

*** SQL Database
***

Database server type           [mysql]:
Server hostname                [localhost]:
Server port                    [3306]:
Database name                  [reviewdb]:
Database username              [gerrit2]:
Change gerrit2's password      [y/N]?

*** Index
***

Type                           [lucene/?]:

*** User Authentication
***

Authentication method          [openid/?]:
Enable signed push support     [y/N]?

*** Review Labels
***

Install Verified label         [y/N]?

*** Email Delivery
***

SMTP server hostname           [localhost]:
SMTP server port               [(default)]:
SMTP encryption                [none/?]:
SMTP username                  :

*** Container Process
***

Run as                         [gerrit2]:
Java runtime                   [C:\Program Files\Java\jre1.8.0_171]:
Upgrade .\bin\gerrit.war       [Y/n]?
Copying gerrit.war to .\bin\gerrit.war

*** SSH Daemon
***

Listen on address              [*]:
Listen on port                 [29418]:

*** HTTP Daemon
***

Behind reverse proxy           [y/N]?
Use SSL (https://)             [y/N]?
Listen on address              [*]:
Listen on port                 [6267]:
Canonical URL                  [http://localhost:6267/]:

*** Cache
***


*** Plugins
***

Installing plugins.
Install plugin commit-message-length-validator version v2.15.1 [Y/n]?
commit-message-length-validator v2.15.1 is already installed, overwrite it [Y/n]?
Updated commit-message-length-validator to v2.15.1
Install plugin download-commands version v2.15.1 [Y/n]?
download-commands v2.15.1 is already installed, overwrite it [Y/n]?
Updated download-commands to v2.15.1
Install plugin hooks version v2.15.1 [Y/n]?
hooks v2.15.1 is already installed, overwrite it [Y/n]?
Updated hooks to v2.15.1
Install plugin replication version v2.15.1 [Y/n]?
replication v2.15.1 is already installed, overwrite it [Y/n]?
Updated replication to v2.15.1
Install plugin reviewnotes version v2.15.1 [Y/n]?
reviewnotes v2.15.1 is already installed, overwrite it [Y/n]?
Updated reviewnotes to v2.15.1
Install plugin singleusergroup version v2.15.1 [Y/n]?
singleusergroup v2.15.1 is already installed, overwrite it [Y/n]?
Updated singleusergroup to v2.15.1
Initializing plugins.

*** Experimental features
***

Enable any experimental features [y/N]?

fatal: DbInjector failed
fatal: Unable to determine SqlDialect
fatal:   caused by java.sql.SQLException: Access denied for user 'gerrit2'@'localhost' (using password: YES)
PS C:\xampp\Gerrit> java -jar gerrit.war init
Using secure store: com.google.gerrit.server.securestore.DefaultSecureStore

*** Gerrit Code Review 2.15.1
***


*** Git Repositories
***

Location of Git repositories   [git]:

*** SQL Database
***

Database server type           [mysql]:
Server hostname                [localhost]:
Server port                    [3306]:
Database name                  [reviewdb]:
Database username              [gerrit2]:
Change gerrit2's password      [y/N]? y
gerrit2's password             :
              confirm password :

*** Index
***

Type                           [lucene/?]:

*** User Authentication
***

Authentication method          [openid/?]:
Enable signed push support     [y/N]?

*** Review Labels
***

Install Verified label         [y/N]?

*** Email Delivery
***

SMTP server hostname           [localhost]:
SMTP server port               [(default)]:
SMTP encryption                [none/?]:
SMTP username                  :

*** Container Process
***

Run as                         [gerrit2]:
Java runtime                   [C:\Program Files\Java\jre1.8.0_171]:
Upgrade .\bin\gerrit.war       [Y/n]?
Copying gerrit.war to .\bin\gerrit.war

*** SSH Daemon
***

Listen on address              [*]:
Listen on port                 [29418]:

*** HTTP Daemon
***

Behind reverse proxy           [y/N]?
Use SSL (https://)             [y/N]?
Listen on address              [*]:
Listen on port                 [6267]:
Canonical URL                  [http://localhost:6267/]:

*** Cache
***


*** Plugins
***

Installing plugins.
Install plugin commit-message-length-validator version v2.15.1 [Y/n]?
commit-message-length-validator v2.15.1 is already installed, overwrite it [Y/n]?
Updated commit-message-length-validator to v2.15.1
Install plugin download-commands version v2.15.1 [Y/n]?
download-commands v2.15.1 is already installed, overwrite it [Y/n]?
Updated download-commands to v2.15.1
Install plugin hooks version v2.15.1 [Y/n]?
hooks v2.15.1 is already installed, overwrite it [Y/n]?
Updated hooks to v2.15.1
Install plugin replication version v2.15.1 [Y/n]?
replication v2.15.1 is already installed, overwrite it [Y/n]?
Updated replication to v2.15.1
Install plugin reviewnotes version v2.15.1 [Y/n]?
reviewnotes v2.15.1 is already installed, overwrite it [Y/n]?
Updated reviewnotes to v2.15.1
Install plugin singleusergroup version v2.15.1 [Y/n]?
singleusergroup v2.15.1 is already installed, overwrite it [Y/n]?
Updated singleusergroup to v2.15.1
Initializing plugins.

*** Experimental features
***

Enable any experimental features [y/N]?

Initialized C:\xampp\Gerrit
PS C:\xampp\Gerrit> java -jar .\bin\gerrit.war daemon --console-log
[2018-05-17 15:43:57,468] [main] INFO  com.google.gerrit.server.cache.h2.H2CacheFactory : Enabling disk cache C:\xampp\G
errit\cache
[2018-05-17 15:43:59,432] [main] INFO  com.google.gerrit.server.config.ScheduleConfig : gc schedule parameter "gc.interv
al" is not configured
[2018-05-17 15:43:59,433] [main] INFO  com.google.gerrit.server.config.ScheduleConfig : changeCleanup schedule parameter
 "changeCleanup.interval" is not configured
五月 17, 2018 3:43:59 下午 com.google.inject.assistedinject.FactoryProvider2 isValidForOptimizedAssistedInject
警告: AssistedInject factory com.google.gerrit.sshd.DispatchCommand$Factory will be slow because class com.google.gerrit
.sshd.DispatchCommand has assisted Provider dependencies or injects the Injector. Stop injecting @Assisted Provider<T> (
instead use @Assisted T) or Injector to speed things up. (It will be a ~6500% speed bump!)  The exact offending deps are
: [Key[type=com.google.inject.Injector, annotation=[none]]@com.google.gerrit.sshd.BaseCommand.injector]
[2018-05-17 15:44:00,812] [main] WARN  com.google.gerrit.sshd.SshDaemon : Cannot format SSHD host key [EdDSA]: invalid k
ey type
[2018-05-17 15:44:00,828] [main] WARN  com.google.gerrit.server.config.GitwebCgiConfig : gitweb not installed (no \usr\l
ib\cgi-bin\gitweb.cgi found)
[2018-05-17 15:44:02,130] [main] INFO  org.eclipse.jetty.util.log : Logging initialized @11420ms
[2018-05-17 15:44:02,519] [main] WARN  com.google.gerrit.metrics.proc.OperatingSystemMXBeanProvider : No implementation
of UnixOperatingSystemMXBean found
[2018-05-17 15:44:02,532] [main] INFO  com.google.gerrit.server.git.LocalDiskRepositoryManager : Defaulting core.streamF
ileThreshold to 906m
[2018-05-17 15:44:02,574] [main] INFO  com.google.gerrit.server.plugins.PluginLoader : Loading plugins from C:\xampp\Ger
rit\.\plugins
五月 17, 2018 3:44:02 下午 com.google.inject.servlet.GuiceFilter setPipeline
警告: Multiple Servlet injectors detected. This is a warning indicating that you have more than one GuiceFilter running
in your web application. If this is deliberate, you may safely ignore this message. If this is NOT deliberate however, y
our application may not work as expected.
[2018-05-17 15:44:02,671] [main] INFO  com.google.gerrit.server.plugins.PluginLoader : Loaded plugin commit-message-leng
th-validator, version v2.15.1
[2018-05-17 15:44:02,738] [main] INFO  com.google.gerrit.server.plugins.PluginLoader : Loaded plugin download-commands,
version v2.15.1
[2018-05-17 15:44:02,819] [main] INFO  com.google.gerrit.server.plugins.PluginLoader : Loaded plugin hooks, version v2.1
5.1
[2018-05-17 15:44:02,915] [main] WARN  com.googlesource.gerrit.plugins.replication.ReplicationFileBasedConfig : Config f
ile .\etc\replication.config does not exist; not replicating
[2018-05-17 15:44:02,922] [main] INFO  com.google.gerrit.server.plugins.PluginLoader : Loaded plugin replication, versio
n v2.15.1
[2018-05-17 15:44:02,978] [main] INFO  com.google.gerrit.server.plugins.PluginLoader : Loaded plugin reviewnotes, versio
n v2.15.1
[2018-05-17 15:44:03,020] [main] INFO  com.google.gerrit.server.plugins.PluginLoader : Loaded plugin singleusergroup, ve
rsion v2.15.1
[2018-05-17 15:44:03,285] [main] INFO  com.google.gerrit.server.git.GarbageCollectionRunner : Ignoring missing gc schedu
le configuration
[2018-05-17 15:44:03,285] [main] INFO  com.google.gerrit.server.config.ScheduleConfig : accountDeactivation schedule par
ameter "accountDeactivation.interval" is not configured
[2018-05-17 15:44:03,286] [main] INFO  com.google.gerrit.server.change.ChangeCleanupRunner : Ignoring missing changeClea
nup schedule configuration
[2018-05-17 15:44:03,318] [main] INFO  com.google.gerrit.sshd.SshDaemon : Started Gerrit SSHD-CORE-1.6.0 on *:29418
[2018-05-17 15:44:03,323] [main] INFO  org.eclipse.jetty.server.Server : jetty-9.3.18.v20170406
[2018-05-17 15:44:03,761] [main] INFO  org.eclipse.jetty.server.handler.ContextHandler : Started o.e.j.s.ServletContextH
andler@327ac23{/,null,AVAILABLE}
[2018-05-17 15:44:03,782] [main] INFO  org.eclipse.jetty.server.AbstractConnector : Started ServerConnector@18a538a0{HTT
P/1.1,[http/1.1]}{0.0.0.0:6267}
[2018-05-17 15:44:03,784] [main] INFO  org.eclipse.jetty.server.Server : Started @13076ms
[2018-05-17 15:44:03,786] [main] INFO  com.google.gerrit.pgm.Daemon : Gerrit Code Review 2.15.1 ready
[2018-05-17 15:44:16,094] [HTTP-76] WARN  org.eclipse.jgit.util.FS_Win32 :

```
