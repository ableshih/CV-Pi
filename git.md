http://sam0512.blogspot.tw/2013/06/windowsgit-server.html


https://beginor.github.io/2013/03/01/config-apache-git-server-on-windows.html

http://mapler-learn.blogspot.tw/2016/03/windowsgit-server.html



windows架git server的安裝流程紀錄
http://sam0512.blogspot.tw/2013/06/windowsgit-server.html

git + apache + windows xp
http://phardera.blogspot.tw/2012/09/git-apache-windows-xp.html

Git Server on Windows 安裝手記
https://www.huanlintalk.com/2011/05/install-git-server-and-apache-on.html

Hosting a Git server under Apache on Windows
http://www.jeremyskinner.co.uk/2010/07/31/hosting-a-git-server-under-apache-on-windows/

Gitblit GO Installation & Setup
http://gitblit.com/setup_go.html

Installing IIS 8 on Windows Server 2012
https://docs.microsoft.com/en-us/iis/get-started/whats-new-in-iis-8/installing-iis-8-on-windows-server-2012

Git Server 架設，使用APACHE(windows 7)
http://dkstudiocms.blogspot.tw/2011/11/git-server-apachewindows-7.html

在 Windows 系统上配置 Apache Git 服务器
https://beginor.github.io/2013/03/01/config-apache-git-server-on-windows.html


http://wernbin.pixnet.net/blog/post/45716002-windows%E6%9E%B6git-server%E7%9A%84%E5%AE%89%E8%A3%9D%E6%B5%81%E7%A8%8B%E7%B4%80%E9%8C%84

note
到 http://git-scm.com 下載  git for windows  http://git-scm.com/
安裝tortoisegit，看你是32位元還是64位元，擇一安裝即可 https://code.google.com/p/tortoisegit/wiki/Download 
安裝apache，我是裝這個：httpd-2.2.22-win32-x86-openssl-0.9.8t.msi，port請選擇8080(如下圖)，並http://ftp.tc.edu.tw/pub/Apache/httpd/binaries/win32/ https://httpd.apache.org/download.cgi
在你想要的槽建立一個專門放倉儲管理的資料庫，C:/Kelvin/GitRepos
去修改apache的設定，到C:\Program Files (x86)\Apache Software Foundation\Apache2.2\conf找到httpd.conf檔案。
再在 httpd.conf 的末尾添加一句 Include conf/git.conf
新建一个 git.conf , 与 httpd.conf 保存在同一个目录, 實際目錄路徑可能因系統不同而不同
<Directory />
    Options FollowSymLinks
    AllowOverride None
    Order deny,allow
    Allow from all
</Directory>

<Directory "C:/Kelvin/GitRepos">
     Options Indexes FollowSymLinks
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>

<Directory "C:/Program Files/Git/mingw64/libexec/git-core/">
     Options Indexes FollowSymLinks
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>

#Set this to the root folder containing your Git repositories.
SetEnv GIT_PROJECT_ROOT C:/Kelvin/GitRepos

# Set this to export all projects by default (by default,
# git will only publish those repositories that contain a
# file named "git-daemon-export-ok"
SetEnv GIT_HTTP_EXPORT_ALL

# Route specific URLS matching this regular expression to the git http server.
ScriptAliasMatch \
  "(?x)^/git/(.*/(HEAD | \
    info/refs | \
    objects/(info/[^/]+ | \
      [0-9a-f]{2}/[0-9a-f]{38} | \
      pack/pack-[0-9a-f]{40}\.(pack|idx)) | \
    git-(upload|receive)-pack))$" \
    "C:/Program Files/Git/mingw64/libexec/git-core/git-http-backend.exe/$1"

ScriptAlias /git/ "C:/Program Files/Git/mingw64/libexec/git-core/git-http-backend.exe/"
<Location /git/>
AuthType Basic
AuthName "GIT Repository"
AuthUserFile "C:/Kelvin/GitRepos/htpasswd"
Require valid-user
</Location>
對著GitRepos的資料夾按右鍵,選擇Git Bash，會出現console視窗，
輸入
git init --bare project
建立出project資料夾後，再輸入
cd project
進入後再輸入 
git update-server-info
輸入完再輸入
touch daemon-export-ok
為目錄http://ip_addr/git增加權限
請到C:\Program Files (x86)\Apache Software Foundation\Apache2.2\bin  按右鍵點選git bash
輸入htpasswd -cmb /C/Kelvin/GitRepos/htpasswd root calvin
/C/Kelvin/GitRepos/為你的倉儲路徑 (必須和git.conf一致)
後面接著htpasswd則是你命名的檔案名稱 (必須和git.conf一致)
ID: root
PWD: calvin
到C:/Kelvin/GitRepos如果你有看到htpasswd檔出來你就成功了
測試：隨便開一個資料夾，對他按右鍵選擇選擇 Git clone，將之前建置的project資料夾給複製一份起來到另外個資料夾，
git clone http://root:calvin@ip_addr/git/project
複製URL打 http:127.0.0.1:8080/git/project
接著輸入帳密的部分：root/calvin
如果有成功抓下來，那就恭喜你成功哩。


note
到 http://git-scm.com 下載  git for windows  http://git-scm.com/
安裝tortoisegit，看你是32位元還是64位元，擇一安裝即可 https://code.google.com/p/tortoisegit/wiki/Download 
安裝apache，我是裝這個：httpd-2.2.22-win32-x86-openssl-0.9.8t.msi，port請選擇8080(如下圖)，並http://ftp.tc.edu.tw/pub/Apache/httpd/binaries/win32/ https://httpd.apache.org/download.cgi
在你想要的槽建立一個專門放倉儲管理的資料庫，C:/Kelvin/GitRepos
去修改apache的設定，到C:\Program Files (x86)\Apache Software Foundation\Apache2.2\conf找到httpd.conf檔案。
再在 httpd.conf 的末尾添加一句 Include conf/git.conf
新建一个 git.conf , 与 httpd.conf 保存在同一个目录, 實際目錄路徑可能因系統不同而不同
<Directory />
    Options FollowSymLinks
    AllowOverride None
    Order deny,allow
    Allow from all
</Directory>

<Directory "C:/Kelvin/GitRepos">
     Options Indexes FollowSymLinks
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>

<Directory "C:/Program Files/Git/mingw64/libexec/git-core/">
     Options Indexes FollowSymLinks
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>

#Set this to the root folder containing your Git repositories.
SetEnv GIT_PROJECT_ROOT C:/Kelvin/GitRepos

# Set this to export all projects by default (by default,
# git will only publish those repositories that contain a
# file named "git-daemon-export-ok"
SetEnv GIT_HTTP_EXPORT_ALL

# Route specific URLS matching this regular expression to the git http server.
ScriptAliasMatch \
  "(?x)^/git/(.*/(HEAD | \
    info/refs | \
    objects/(info/[^/]+ | \
      [0-9a-f]{2}/[0-9a-f]{38} | \
      pack/pack-[0-9a-f]{40}\.(pack|idx)) | \
    git-(upload|receive)-pack))$" \
    "C:/Program Files/Git/mingw64/libexec/git-core/git-http-backend.exe/$1"

ScriptAlias /git/ "C:/Program Files/Git/mingw64/libexec/git-core/git-http-backend.exe/"
<Location /git/>
AuthType Basic
AuthName "GIT Repository"
AuthUserFile "C:/Kelvin/GitRepos/htpasswd"
Require valid-user
</Location>
對著GitRepos的資料夾按右鍵,選擇Git Bash，會出現console視窗，
輸入
git init --bare project
建立出project資料夾後，再輸入
cd project
進入後再輸入 
git update-server-info
輸入完再輸入
touch daemon-export-ok
為目錄http://ip_addr/git增加權限
請到C:\Program Files (x86)\Apache Software Foundation\Apache2.2\bin  按右鍵點選git bash
輸入htpasswd -cmb /C/Kelvin/GitRepos/htpasswd root calvin
/C/Kelvin/GitRepos/為你的倉儲路徑 (必須和git.conf一致)
後面接著htpasswd則是你命名的檔案名稱 (必須和git.conf一致)
ID: root
PWD: calvin
到C:/Kelvin/GitRepos如果你有看到htpasswd檔出來你就成功了
測試：隨便開一個資料夾，對他按右鍵選擇選擇 Git clone，將之前建置的project資料夾給複製一份起來到另外個資料夾，
git clone http://root:calvin@ip_addr/git/project
複製URL打 http:127.0.0.1:8080/git/project
接著輸入帳密的部分：root/calvin
如果有成功抓下來，那就恭喜你成功哩。

