#### OA 系統

參照 https://blog.csdn.net/deyili/article/details/79422500
-----------------------------------

-----------------------------------
#### 先申請固定 IP

固定 IP 下來後，申請 DNS

SMTP relay 

-----------------------------------


-----------------------------------


-----------------------------------

#### 1. java
download
https://www.java.com/zh_TW/download/windows-64bit.jsp

install
jre-8u171-windows-x64.exe

add path

test java
cmd
```
java -version
```
-----------------------------------

#### 2. apache
```
download
https://httpd.apache.org/docs/current/platform/windows.html#down
https://www.apachehaus.com/cgi-bin/download.plx
http://www.apachehaus.com/downloads/httpd-2.4.33-o102o-x64-vc14-r2.zip
httpd-2.4.33-o102o-x64-vc14-r2.zip

add web folder

unzip to web folder

add path
C:\web\Apache24\bin

cmd

httpd.exe -k install



http://www.apache.org/dist/commons/daemon/binaries/windows/

commons-daemon-1.1.0-bin-windows.zip

unzip

copy *.exe to C:\web\Apache24\bin


modify C:\web\Apache24\conf\httpd.conf
#Define SRVROOT "/Apache24"
Define SRVROOT "C:/web/Apache24"

start web server
run C:\web\Apache24\bin\ApacheMonitor.exe

check server
http://127.0.0.1/

```



-----------------------------------
# mysql

mysql-installer-community-8.0.11.0.msi

https://www.youtube.com/watch?v=WuBcTJnIuzo

https://dev.mysql.com/downloads/

https://dev.mysql.com/downloads/mysql/

https://dev.mysql.com/downloads/windows/installer/8.0.html

https://dev.mysql.com/downloads/file/?id=476477

https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.11.0.msi

run *.msi

select Developer Default

run 
MySQL -> MySQL Server 8.0 -> MySQL 8.0 Command Line Client
```
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 8.0.11 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE USER 'gerrit'@'localhost' IDENTIFIED BY 'secret';
Query OK, 0 rows affected (0.04 sec)

mysql> CREATE DATABASE reviewdb DEFAULT CHARACTER SET 'utf8';
Query OK, 1 row affected, 1 warning (0.03 sec)

mysql> GRANT ALL ON reviewdb.* TO 'gerrit'@'localhost';
Query OK, 0 rows affected (0.05 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)

mysql>
```


-----------------------------------
ssh-keygen
Git for Windows installed
https://gitforwindows.org/

https://github.com/git-for-windows/git/releases/download/v2.17.0.windows.1/Git-2.17.0-64-bit.exe
```
cmd

add PATH c:\Program Files\Git\usr\bin

git

ssh-keygen
```

-----------------------------------

#### 3. gerrit
download
https://www.gerritcodereview.com/
https://www.gerritcodereview.com/download/
gerrit-2.15.1.war

rename gerrit-2.15.1.war gerrit.war
copy to web folder


-----------------------------------
#### PATH
```
D:\ddgit\Apache24\bin
C:\Program Files\Java\jdk-10.0.1\bin


D:\>path
PATH=D:\ddgit\Apache24\bin;C:\Python27\;C:\Python27\Scripts;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\Git\bin;C:\Program Files\Git\usr\bin;C:\Program Files\TortoiseGit\bin;C:\ProgramData\chocolatey\bin;C:\Program Files\Java\jdk-10.0.1\bin;C:\Program Files\PuTTY\;C:\Users\9709732\AppData\Local\Programs\Python\Python36-32\Scripts\;C:\Users\9709732\AppData\Local\Programs\Python\Python36-32\;C:\Users\9709732\AppData\Local\Microsoft\WindowsApps;C:\ProgramData\chocolatey\lib\msys2;C:\tools\msys64

```



-----------------------------------



-------------------------------------------
#### gerrit install

```
Windows PowerShell
著作權 (C) 2016 Microsoft Corporation. 著作權所有，並保留一切權利。

PS C:\Users\9709732> d:
PS D:\> cd .\ddgit\
PS D:\ddgit> cd .\Gerrit\
PS D:\ddgit\Gerrit> java -jar .\gerrit.war init
Using secure store: com.google.gerrit.server.securestore.DefaultSecureStore

*** Gerrit Code Review 2.15.1
***


*** Git Repositories
***

Location of Git repositories   [git]:

*** SQL Database
***

Database server type           [mysql]: h2

*** Index
***

Type                           [lucene/?]:

*** User Authentication
***

Authentication method          [openid/?]:
Enable signed push support     [y/N]?

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

Run as                         [9709732]:
Java runtime                   [C:\Program Files (x86)\Java\jre1.8.0_171]:
Upgrade .\bin\gerrit.war       [Y/n]? y
Copying gerrit.war to .\bin\gerrit.war

*** SSH Daemon
***

Listen on address              [ddgit.wistron.com]:
Listen on port                 [29418]:

*** HTTP Daemon
***

Behind reverse proxy           [y/N]?
Use SSL (https://)             [y/N]?
Listen on address              [ddgit.wistron.com]:
Listen on port                 [8088]:
Canonical URL                  [http://ddgit.wistron.com:8088/]:

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

Initialized D:\ddgit\Gerrit
PS D:\ddgit\Gerrit>

```

-----------------------------------
#### gerrit 設定檔
```
[gerrit]
	basePath = git
	serverId = 9745273f-59fe-4cb8-8d96-449a6bd9d798
	canonicalWebUrl = http://ddgit.wistron.com:8088/
[database]
	type = h2
	hostname = localhost
	database = reviewdb
	username = 9709732
[index]
	type = LUCENE
[auth]
	type = OPENID
[receive]
	enableSignedPush = false
[sendemail]
	smtpServer = localhost
[container]
	user = 9709732
	javaHome = C:\\Program Files (x86)\\Java\\jre1.8.0_171
[sshd]
	listenAddress = ddgit.wistron.com:29418
[httpd]
	listenUrl = http://ddgit.wistron.com:8099/
[cache]
	directory = cache

```
-----------------------------------
#### 加到開機後自動啟用 服務
```
PS D:\ddgit\Gerrit> prunsrv.exe //IS//Gerrit --DisplayName="Gerrit Code Review" --Startup=auto --Jvm="C:\Program Files (
x86)\Java\jre1.8.0_171\bin\client\jvm.dll" --Classpath=D:\ddgit\GERRIT\bin\gerrit.war --LogPath=D:\ddgit\GERRIT\logs --S
tartPath=D:\ddgit\GERRIT --StartMode=jvm --StopMode=jvm --StartClass=com.google.gerrit.launcher.GerritLauncher --StartMe
thod=daemonStart --StopClass=com.google.gerrit.launcher.GerritLauncher --StopMethod=daemonStop

```
-----------------------------------
#### prunsrv 用法
```
PS D:\ddgit\Gerrit> prunsrv.exe //DS//Gerrit 

IS install
DS del
```
-----------------------------------
#### gerrit 用法
```
install
java -jar .\gerrit-2.15.1.war init

起動
java -jar .\bin\gerrit.war daemon --console-log

127.0.0.1:8080

ctrl + c (exit)

```
-----------------------------------

#### apache 設定檔 

```

#
# This is the main Apache HTTP server configuration file.  It contains the
# configuration directives that give the server its instructions.
# See <URL:http://httpd.apache.org/docs/2.4/> for detailed information.
# In particular, see 
# <URL:http://httpd.apache.org/docs/2.4/mod/directives.html>
# for a discussion of each configuration directive.
#
# Do NOT simply read the instructions in here without understanding
# what they do.  They're here only as hints or reminders.  If you are unsure
# consult the online docs. You have been warned.  
#
# Configuration and logfile names: If the filenames you specify for many
# of the server's control files begin with "/" (or "drive:/" for Win32), the
# server will use that explicit path.  If the filenames do *not* begin
# with "/", the value of ServerRoot is prepended -- so "logs/access_log"
# with ServerRoot set to "/usr/local/apache2" will be interpreted by the
# server as "/usr/local/apache2/logs/access_log", whereas "/logs/access_log" 
# will be interpreted as '/logs/access_log'.
#
# NOTE: Where filenames are specified, you must use forward slashes
# instead of backslashes (e.g., "c:/apache" instead of "c:\apache").
# If a drive letter is omitted, the drive on which httpd.exe is located
# will be used by default.  It is recommended that you always supply
# an explicit drive letter in absolute paths to avoid confusion.

#
# ServerRoot: The top of the directory tree under which the server's
# configuration, error, and log files are kept.
#
# Do not add a slash at the end of the directory path.  If you point
# ServerRoot at a non-local disk, be sure to specify a local disk on the
# Mutex directive, if file-based mutexes are used.  If you wish to share the
# same ServerRoot for multiple httpd daemons, you will need to change at
# least PidFile.
#

# Define SRVROOT "/Apache24"
Define SRVROOT "D:/ddgit/Apache24"
#ServerRoot "${SRVROOT}"
ServerRoot "D:/ddgit/Apache24"

#
# Mutex: Allows you to set the mutex mechanism and mutex file directory
# for individual mutexes, or change the global defaults
#
# Uncomment and change the directory if mutexes are file-based and the default
# mutex file directory is not on a local disk or is not appropriate for some
# other reason.
#
# Mutex default:logs

#
# Listen: Allows you to bind Apache to specific IP addresses and/or
# ports, instead of the default. See also the <VirtualHost>
# directive.
#
# Change this to Listen on specific IP addresses as shown below to 
# prevent Apache from glomming onto all bound IP addresses.
#
#Listen 12.34.56.78:80
#Listen 80
Listen 8080
Listen 8088
#Listen 8888

#
# Dynamic Shared Object (DSO) Support
#
# To be able to use the functionality of a module which was built as a DSO you
# have to place corresponding `LoadModule' lines at this location so the
# directives contained in it are actually available _before_ they are used.
# Statically compiled modules (those listed by `httpd -l') do not need
# to be loaded here.
#
# Example:
# LoadModule foo_module modules/mod_foo.so
#
LoadModule access_compat_module modules/mod_access_compat.so
LoadModule actions_module modules/mod_actions.so
LoadModule alias_module modules/mod_alias.so
LoadModule allowmethods_module modules/mod_allowmethods.so
LoadModule asis_module modules/mod_asis.so
LoadModule auth_basic_module modules/mod_auth_basic.so
#LoadModule auth_digest_module modules/mod_auth_digest.so
#LoadModule auth_form_module modules/mod_auth_form.so
#LoadModule authn_anon_module modules/mod_authn_anon.so
LoadModule authn_core_module modules/mod_authn_core.so
#LoadModule authn_dbd_module modules/mod_authn_dbd.so
#LoadModule authn_dbm_module modules/mod_authn_dbm.so
LoadModule authn_file_module modules/mod_authn_file.so
#LoadModule authn_socache_module modules/mod_authn_socache.so
#LoadModule authnz_fcgi_module modules/mod_authnz_fcgi.so
#LoadModule authnz_ldap_module modules/mod_authnz_ldap.so
LoadModule authz_core_module modules/mod_authz_core.so
#LoadModule authz_dbd_module modules/mod_authz_dbd.so
#LoadModule authz_dbm_module modules/mod_authz_dbm.so
LoadModule authz_groupfile_module modules/mod_authz_groupfile.so
LoadModule authz_host_module modules/mod_authz_host.so
#LoadModule authz_owner_module modules/mod_authz_owner.so
LoadModule authz_user_module modules/mod_authz_user.so
LoadModule autoindex_module modules/mod_autoindex.so
#LoadModule buffer_module modules/mod_buffer.so
#LoadModule cache_module modules/mod_cache.so
#LoadModule cache_disk_module modules/mod_cache_disk.so
#LoadModule cache_socache_module modules/mod_cache_socache.so
#LoadModule cern_meta_module modules/mod_cern_meta.so
LoadModule cgi_module modules/mod_cgi.so
#LoadModule charset_lite_module modules/mod_charset_lite.so
#LoadModule data_module modules/mod_data.so
#LoadModule dav_module modules/mod_dav.so
#LoadModule dav_fs_module modules/mod_dav_fs.so
#LoadModule dav_lock_module modules/mod_dav_lock.so
#LoadModule dbd_module modules/mod_dbd.so
#LoadModule deflate_module modules/mod_deflate.so
LoadModule dir_module modules/mod_dir.so
#LoadModule dumpio_module modules/mod_dumpio.so
LoadModule env_module modules/mod_env.so
#LoadModule expires_module modules/mod_expires.so
#LoadModule ext_filter_module modules/mod_ext_filter.so
#LoadModule file_cache_module modules/mod_file_cache.so
#LoadModule filter_module modules/mod_filter.so
#LoadModule headers_module modules/mod_headers.so
#LoadModule heartbeat_module modules/mod_heartbeat.so
#LoadModule heartmonitor_module modules/mod_heartmonitor.so
#LoadModule http2_module modules/mod_http2.so
#LoadModule ident_module modules/mod_ident.so
#LoadModule imagemap_module modules/mod_imagemap.so
LoadModule include_module modules/mod_include.so
LoadModule info_module modules/mod_info.so
LoadModule isapi_module modules/mod_isapi.so
#LoadModule lbmethod_bybusyness_module modules/mod_lbmethod_bybusyness.so
#LoadModule lbmethod_byrequests_module modules/mod_lbmethod_byrequests.so
#LoadModule lbmethod_bytraffic_module modules/mod_lbmethod_bytraffic.so
#LoadModule lbmethod_heartbeat_module modules/mod_lbmethod_heartbeat.so
#LoadModule ldap_module modules/mod_ldap.so
#LoadModule logio_module modules/mod_logio.so
LoadModule log_config_module modules/mod_log_config.so
#LoadModule log_debug_module modules/mod_log_debug.so
#LoadModule log_forensic_module modules/mod_log_forensic.so
#LoadModule lua_module modules/mod_lua.so
#LoadModule macro_module modules/mod_macro.so
#LoadModule md_module modules/mod_md.so
LoadModule mime_module modules/mod_mime.so
#LoadModule mime_magic_module modules/mod_mime_magic.so
LoadModule negotiation_module modules/mod_negotiation.so
LoadModule proxy_module modules/mod_proxy.so
#LoadModule proxy_ajp_module modules/mod_proxy_ajp.so
LoadModule proxy_balancer_module modules/mod_proxy_balancer.so
LoadModule proxy_connect_module modules/mod_proxy_connect.so
#LoadModule proxy_express_module modules/mod_proxy_express.so
#LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so
LoadModule proxy_ftp_module modules/mod_proxy_ftp.so
#LoadModule proxy_html_module modules/mod_proxy_html.so
LoadModule proxy_http_module modules/mod_proxy_http.so
#LoadModule proxy_http2_module modules/mod_proxy_http2.so
#LoadModule proxy_scgi_module modules/mod_proxy_scgi.so
#LoadModule proxy_uwsgi_module modules/mod_proxy_uwsgi.so
#LoadModule proxy_wstunnel_module modules/mod_proxy_wstunnel.so
#LoadModule ratelimit_module modules/mod_ratelimit.so
#LoadModule reflector_module modules/mod_reflector.so
#LoadModule remoteip_module modules/mod_remoteip.so
#LoadModule request_module modules/mod_request.so
#LoadModule reqtimeout_module modules/mod_reqtimeout.so
LoadModule rewrite_module modules/mod_rewrite.so
#LoadModule sed_module modules/mod_sed.so
#LoadModule session_module modules/mod_session.so
#LoadModule session_cookie_module modules/mod_session_cookie.so
#LoadModule session_crypto_module modules/mod_session_crypto.so
#LoadModule session_dbd_module modules/mod_session_dbd.so
LoadModule setenvif_module modules/mod_setenvif.so
#LoadModule slotmem_plain_module modules/mod_slotmem_plain.so
LoadModule slotmem_shm_module modules/mod_slotmem_shm.so
#LoadModule socache_dbm_module modules/mod_socache_dbm.so
#LoadModule socache_memcache_module modules/mod_socache_memcache.so
LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
#LoadModule speling_module modules/mod_speling.so
LoadModule ssl_module modules/mod_ssl.so
LoadModule status_module modules/mod_status.so
#LoadModule substitute_module modules/mod_substitute.so
#LoadModule unique_id_module modules/mod_unique_id.so
#LoadModule userdir_module modules/mod_userdir.so
#LoadModule usertrack_module modules/mod_usertrack.so
#LoadModule version_module modules/mod_version.so
#LoadModule vhost_alias_module modules/mod_vhost_alias.so
#LoadModule watchdog_module modules/mod_watchdog.so
#LoadModule xml2enc_module modules/mod_xml2enc.so

<IfModule unixd_module>
#
# If you wish httpd to run as a different user or group, you must run
# httpd as root initially and it will switch.  
#
# User/Group: The name (or #number) of the user/group to run httpd as.
# It is usually good practice to create a dedicated user and group for
# running httpd, as with most system services.
#
User daemon
Group daemon

</IfModule>

# 'Main' server configuration
#
# The directives in this section set up the values used by the 'main'
# server, which responds to any requests that aren't handled by a
# <VirtualHost> definition.  These values also provide defaults for
# any <VirtualHost> containers you may define later in the file.
#
# All of these directives may appear inside <VirtualHost> containers,
# in which case these default settings will be overridden for the
# virtual host being defined.
#

#
# ServerAdmin: Your address, where problems with the server should be
# e-mailed.  This address appears on some server-generated pages, such
# as error documents.  e.g. admin@your-domain.com
#
ServerAdmin able_shih@wistron.com

#
# ServerName gives the name and port that the server uses to identify itself.
# This can often be determined automatically, but we recommend you specify
# it explicitly to prevent problems during startup.
#
# If your host doesn't have a registered DNS name, enter its IP address here.
#
#ServerName ddgit.wistron.com:8888
#ServerName ddgit.wistron.com:8080
#ServerName 10.34.200.100:8080
ServerName ddgit.wistron.com

#
# Deny access to the entirety of your server's filesystem. You must
# explicitly permit access to web content directories in other 
# <Directory> blocks below.
#
<Directory />
    AllowOverride none
    Require all denied
</Directory>

#
# Note that from this point forward you must specifically allow
# particular features to be enabled - so if something's not working as
# you might expect, make sure that you have specifically enabled it
# below.
#

#
# DocumentRoot: The directory out of which you will serve your
# documents. By default, all requests are taken from this directory, but
# symbolic links and aliases may be used to point to other locations.
#
#DocumentRoot "${SRVROOT}/htdocs"
DocumentRoot "D:/ddgit/Apache24/htdocs"
#<Directory "${SRVROOT}/htdocs">
<Directory "D:/ddgit/Apache24/htdocs">
    #
    # Possible values for the Options directive are "None", "All",
    # or any combination of:
    #   Indexes Includes FollowSymLinks SymLinksifOwnerMatch ExecCGI MultiViews
    #
    # Note that "MultiViews" must be named *explicitly* --- "Options All"
    # doesn't give it to you.
    #
    # The Options directive is both complicated and important.  Please see
    # http://httpd.apache.org/docs/2.4/mod/core.html#options
    # for more information.
    #
    Options Indexes FollowSymLinks

    #
    # AllowOverride controls what directives may be placed in .htaccess files.
    # It can be "All", "None", or any combination of the keywords:
    #   Options FileInfo AuthConfig Limit
    #
    AllowOverride None

    #
    # Controls who can get stuff from this server.
    #
    Require all granted
</Directory>

#
# DirectoryIndex: sets the file that Apache will serve if a directory
# is requested.
#
<IfModule dir_module>
    DirectoryIndex index.html
</IfModule>

#
# The following lines prevent .htaccess and .htpasswd files from being 
# viewed by Web clients. 
#
<Files ".ht*">
    Require all denied
</Files>

#
# ErrorLog: The location of the error log file.
# If you do not specify an ErrorLog directive within a <VirtualHost>
# container, error messages relating to that virtual host will be
# logged here.  If you *do* define an error logfile for a <VirtualHost>
# container, that host's errors will be logged there and not here.
#
ErrorLog "logs/error.log"

#
# LogLevel: Control the number of messages logged to the error_log.
# Possible values include: debug, info, notice, warn, error, crit,
# alert, emerg.
#
LogLevel warn

<IfModule log_config_module>
    #
    # The following directives define some format nicknames for use with
    # a CustomLog directive (see below).
    #
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common

    <IfModule logio_module>
      # You need to enable mod_logio.c to use %I and %O
      LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O" combinedio
    </IfModule>

    #
    # The location and format of the access logfile (Common Logfile Format).
    # If you do not define any access logfiles within a <VirtualHost>
    # container, they will be logged here.  Contrariwise, if you *do*
    # define per-<VirtualHost> access logfiles, transactions will be
    # logged therein and *not* in this file.
    #
    CustomLog "logs/access.log" common

    #
    # If you prefer a logfile with access, agent, and referer information
    # (Combined Logfile Format) you can use the following directive.
    #
    #CustomLog "logs/access.log" combined
</IfModule>

<IfModule alias_module>
    #
    # Redirect: Allows you to tell clients about documents that used to 
    # exist in your server's namespace, but do not anymore. The client 
    # will make a new request for the document at its new location.
    # Example:
    # Redirect permanent /foo http://www.example.com/bar

    #
    # Alias: Maps web paths into filesystem paths and is used to
    # access content that does not live under the DocumentRoot.
    # Example:
    # Alias /webpath /full/filesystem/path
    #
    # If you include a trailing / on /webpath then the server will
    # require it to be present in the URL.  You will also likely
    # need to provide a <Directory> section to allow access to
    # the filesystem path.

    #
    # ScriptAlias: This controls which directories contain server scripts. 
    # ScriptAliases are essentially the same as Aliases, except that
    # documents in the target directory are treated as applications and
    # run by the server when requested rather than as documents sent to the
    # client.  The same rules about trailing "/" apply to ScriptAlias
    # directives as to Alias.
    #
    #ScriptAlias /cgi-bin/ "${SRVROOT}/cgi-bin/"
    ScriptAlias /cgi-bin/ "D:/ddgit/Apache24/cgi-bin/"

</IfModule>

<IfModule cgid_module>
    #
    # ScriptSock: On threaded servers, designate the path to the UNIX
    # socket used to communicate with the CGI daemon of mod_cgid.
    #
    #Scriptsock logs/cgisock
</IfModule>

#
# "${SRVROOT}/cgi-bin" should be changed to whatever your ScriptAliased
# CGI directory exists, if you have that configured.
#
<Directory "${SRVROOT}/cgi-bin">
    AllowOverride None
    Options None
    Require all granted
</Directory>

<IfModule mime_module>
    #
    # TypesConfig points to the file containing the list of mappings from
    # filename extension to MIME-type.
    #
    TypesConfig conf/mime.types

    #
    # AddType allows you to add to or override the MIME configuration
    # file specified in TypesConfig for specific file types.
    #
    #AddType application/x-gzip .tgz
    #
    # AddEncoding allows you to have certain browsers uncompress
    # information on the fly. Note: Not all browsers support this.
    #
    #AddEncoding x-compress .Z
    #AddEncoding x-gzip .gz .tgz
    #
    # If the AddEncoding directives above are commented-out, then you
    # probably should define those extensions to indicate media types:
    #
    AddType application/x-compress .Z
    AddType application/x-gzip .gz .tgz

    #
    # AddHandler allows you to map certain file extensions to "handlers":
    # actions unrelated to filetype. These can be either built into the server
    # or added with the Action directive (see below)
    #
    # To use CGI scripts outside of ScriptAliased directories:
    # (You will also need to add "ExecCGI" to the "Options" directive.)
    #
    #AddHandler cgi-script .cgi .pl

    # For type maps (negotiated resources):
    #AddHandler type-map var

    #
    # Filters allow you to process content before it is sent to the client.
    #
    # To parse .shtml files for server-side includes (SSI):
    # (You will also need to add "Includes" to the "Options" directive.)
    #
    #AddType text/html .shtml
    #AddOutputFilter INCLUDES .shtml
</IfModule>

#
# The mod_mime_magic module allows the server to use various hints from the
# contents of the file itself to determine its type.  The MIMEMagicFile
# directive tells the module where the hint definitions are located.
#
#MIMEMagicFile conf/magic

#
# Customizable error responses come in three flavors:
# 1) plain text 2) local redirects 3) external redirects
#
# Some examples:
#ErrorDocument 500 "The server made a boo boo."
#ErrorDocument 404 /missing.html
#ErrorDocument 404 "/cgi-bin/missing_handler.pl"
#ErrorDocument 402 http://www.example.com/subscription_info.html
#

#
# MaxRanges: Maximum number of Ranges in a request before
# returning the entire resource, or one of the special
# values 'default', 'none' or 'unlimited'.
# Default setting is to accept 200 Ranges.
#MaxRanges unlimited

#
# EnableMMAP and EnableSendfile: On systems that support it, 
# memory-mapping or the sendfile syscall may be used to deliver
# files.  This usually improves server performance, but must
# be turned off when serving from networked-mounted 
# filesystems or if support for these functions is otherwise
# broken on your system.
# Defaults: EnableMMAP On, EnableSendfile Off
#
#EnableMMAP off
#EnableSendfile on

#AcceptFilter http none
#AcceptFilter https none

# Supplemental configuration
#
# The configuration files in the conf/extra/ directory can be 
# included to add extra features or to modify the default configuration of 
# the server, or you may simply copy their contents here and change as 
# necessary.

# Server-pool management (MPM specific)
#Include conf/extra/httpd-mpm.conf

# Multi-language error messages
#Include conf/extra/httpd-multilang-errordoc.conf

# Fancy directory listings
Include conf/extra/httpd-autoindex.conf

# Language settings
#Include conf/extra/httpd-languages.conf

# User home directories
#Include conf/extra/httpd-userdir.conf

# Real-time info on requests and configuration
Include conf/extra/httpd-info.conf

# Virtual hosts
# Include conf/extra/httpd-vhosts.conf

# Local access to the Apache HTTP Server Manual
#Include conf/extra/httpd-manual.conf

# Distributed authoring and versioning (WebDAV)
#Include conf/extra/httpd-dav.conf

# Various default settings
#Include conf/extra/httpd-default.conf

# Configure mod_proxy_html to understand HTML4/XHTML1
<IfModule proxy_html_module>
Include conf/extra/httpd-proxy-html.conf
</IfModule>

# Secure (SSL/TLS) connections
# Note: The following must must be present to support
#       starting without SSL on platforms with no /dev/random equivalent
#       but a statically compiled-in mod_ssl.
#
<IfModule ssl_module>
#Include conf/extra/httpd-ssl.conf
Include conf/extra/httpd-ahssl.conf
SSLRandomSeed startup builtin
SSLRandomSeed connect builtin
</IfModule>
<IfModule http2_module>
    ProtocolsHonorOrder On
    Protocols h2 h2c http/1.1
</IfModule>


#<VirtualHost *:8080>  
#    ServerName ddgit.wistron.com
#    ProxyPreserveHost On  
 
    #AllowEncodedSlashes On  
    #ProxyPass / http://ddgit.wistron.com:8080/ nocanon
#</VirtualHost> 

#<VirtualHost *:8888>  
#    ServerName ddgit.wistron.com
#	#, the same with gerrit.config "canonicalWebUrl"
#    ProxyPreserveHost On  
#    <Proxy *> 
#        Order deny,allow  
#        Allow from all  
#    </Proxy>  
#    <Location /login/>  
#        AuthType Basic  
#        AuthName "Welcome to Gerrit Code Review!"  
#        Require valid-user  
#        AuthBasicProvider file  
#        AuthUserFile D:/ddgit/config/gerrit_password  
#    </Location> 
# 
#    AllowEncodedSlashes On  
#    ProxyPass / http://ddgit.wistron.com:8888/ nocanon  
#</VirtualHost>

#<VirtualHost *:8088>
#    ServerName ddgit.wistron.com
#    DocumentRoot "D:/ddgit/index.html"
#</VirtualHost>

<VirtualHost *:8088>  
  ServerName review.example.com
  ProxyRequests Off  
  ProxyVia Off  
  ProxyPreserveHost On  

  <Proxy *8088>  
        Order deny,allow  
        Allow from all  
  </Proxy>  

    <Location /login/>
      AuthType Basic
      AuthName "Gerrit Code Review"
      Require valid-user
      AuthUserFile D:/ddgit/config/gerrit_passwd
    </Location>

  AllowEncodedSlashes On
#  ProxyPass / http://192.168.100.123:8099/ nocanon
#  ProxyPassReverse / http://192.168.100.123:8099/
  ProxyPass / http://ddgit.wistron.com:8099/ nocanon
  ProxyPassReverse / http://ddgit.wistron.com:8099/
</VirtualHost>

```

-----------------------------------

#### Eform
```

類別

佈線工程 
 網域相關服務 
 電子郵件 
 網路權限 
 通訊服務(電話傳真) 
 OS(作業系統)及軟體 
 Notes系統 
 OA Application 
 電腦設備服務 
 網路服務 
 系統監控服務 
 服務器硬體設備 
 ITSM  


項目  (網域相關服務)  
 Lync 服務 
 電腦帳號 
 安全性群組 
 檔案伺服器/FTP 
 印表機服務 
 網域帳號  

項目  (電子郵件)
 SMTP relay 權限 
 憑證服務(郵件加密/簽章) 
 Push Mail 服務 
 郵件信箱 
 郵件群組 
 郵件帳戶  

項目  (網路權限)
 IM 即時通訊 
 ISA Policy 
 固定IP地址 
 Firewall Policy 
 VPN權限  


項目  (網路服務)
 憑證服務 
 網路設備組態 
 反向代理伺服器 
 Internet 
 域名(Domain Name)註冊  
 
 

 
 
 
                                
 







10.34.201.189 ddgit.wistron.com
local PC, OA system, win10 apache 
2023.01.01



Display BU 軟體設計中心 
Git Gerrit Code Review server (source code 簽核系統)
```

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------

-----------------------------------
#### 虛擬網站
```
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
 
 ```
-----------------------------------





```

Apache - VirtualHost 架設虛擬網站
分享: facebook PLURK twitter  
利用 Apache 架設網站伺服器服務 這一篇文章裡我們已經建立好 Apache 網站伺服器，它預設安裝在 C:\AppServ (以後稱此目錄為 「APACHE_ROOT」 )，預設網址的主目錄是 「APACHE_HOME\www」 ，這是在 Apache 伺服器的設定檔( 「APACHE_ROOT\Apache2.2\conf\httpd.conf」 )中定義的。

「APACHE_ROOT\Apache2.2\conf\httpd.conf 」檔案的內容： 

Apache 伺服器的設定檔 httpd.conf

?
#
# DocumentRoot: The directory out of which you will serve your
# documents. By default, all requests are taken from this directory, but
# symbolic links and aliases may be used to point to other locations.
#
DocumentRoot "C:/AppServ/www"
　　預設一台主機只有一個獨立的網站，若您想要在同一台主機能夠有一個以上的獨立網站，可以利用 Apache 伺服器中的 Virtual Host 的設定，從下面的示意圖可以瞭解，這些不同的獨立網站都架設在同一個IP的主機上。


1. 申請個人網域後(mistech.localhost.com)，在原有主機上(127.0.0.1)加設虛擬主機為個人網站(http://mistech.localhost.com/)。這裡的 http://mistech.localhost.com/ 是以本站為例，您應該改為您個人專屬的網域。

2. 在 DNS 伺服器的設定
 

dns                   IN   A      127.0.0.1  ;這個IP的名稱是dns，是本尊
www                 IN   CNAME    dns    ;這是第一個虛擬網站 mistech.localhost.com   --分身
forum                IN   CNAME    dns   ;這是第二個虛擬網站 forum.mistech.localhost.com --分身
phpMyAdmin     IN   CNAME    dns ;這是第三個虛擬網站 phpmyadmin.mistech.localhost.com --分身

若您沒有 DNS 伺服器，也可以直接修改 C:\Windows\System32\drivers\etc\host 檔案也可以，只是這樣的設定只限這台主機適用。

Windows XP/Vista/7 的 hots 檔案
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.

127.0.0.1  www.mistech.localhost.com forum.mistech.localhost.com mistech.localhost.com
 

 3. 在 APACHE_ROOT\Apache2.2\conf\httpd.conf 的內容


BloggerAds 部落格行銷

BloggerAds 部落格行銷
# Real-time info on requests and configuration
#Include conf/extra/httpd-info.conf

# Virtual hosts
Include conf/extra/httpd-vhosts.conf        ; 將前面的 # 刪除，並修改 APACHE_ROOT\Apache2.2\conf\extra/httpd-vhosts.conf 這個檔案


 
# Local access to the Apache HTTP Server Manual
#Include conf/extra/httpd-manual.conf

 4. 在 APACHE_ROOT\Apache2.2\conf\extra\httpd-vhosts.conf 的內容

#
# Virtual Hosts
#
# If you want to maintain multiple domains/hostnames on your
# machine you can setup VirtualHost containers for them. Most configurations
# use only name-based virtual hosts so the server doesn't need to worry about
# IP addresses. This is indicated by the asterisks in the directives below.
#
# You may use the command line option '-S' to verify your virtual host
# configuration.
# Use name-based virtual hosting.
#
NameVirtualHost 127.0.0.1:80

# 這是第一個虛擬網站 www.mistech.localhost.com   --分身
<VirtualHost *:80>
    ServerAdmin webamin@mistech.localhost.com
    DocumentRoot "C:/AppServ/www/mistech"
    ServerName www.mistech.localhost.com
</VirtualHost>

#這是第二個虛擬網站 forum.mistech.localhost.com --分身
<VirtualHost *:80>
    ServerAdmin webamin@mistech.localhost.com
    DocumentRoot "C:/AppServ/www/forum"
    ServerName forum.mistech.localhost.com
</VirtualHost>


 
#這是第三個虛擬網站 phpmyadmin.workplace.netau.net --分身
<VirtualHost *:80>
    ServerAdmin webamin@mistech.localhost.com
    DocumentRoot "C:/AppServ/www/phpMyAdmin"
    ServerName phpmyadmin.mistech.localhost.com
</VirtualHost>

 重新啟動 Apache 伺服器，就可以了，測試一下吧。
 
 ```
