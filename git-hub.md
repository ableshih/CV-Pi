----------------------------------------------------------------------------
# 下載
```
https://git-scm.com/downloads
安裝 (阿呆安裝法)
建 目錄
copy 專案進目錄
點一下目錄 -> 按右鍵 -> 'Git Bash Here'
```
----------------------------------------------------------------------------
## 指令集
```
---
ls (dir)
ls -a (顯示隱藏)
clear (cls)
touch 檔名 (建立檔案)
git status (狀態檢視)
git log (顯示修改記錄)
---

git config --global user.name "Able Shih"
git config --global user.email "Able_Shih@wistron.com"

git config user.name
git config user.email

git init (建立 .git 目錄作為版本記事)

---
~/Desktop/123

[當 git init 之後會出現 master]
~/Desktop/123 (master)
---

git add 檔名
或
git add .
```
---
加入檔案
---

----------------------------------------------------------------------------
## git 四階段圖
```
untracked unmodified modified staged
untracked 用add 到staged 用commit 回到unmodified
unmodified 用edit 到modified 用add  到staged 用commit 回到unmodified
modified 用add 到staged 用commit 回到unmodified
staged 用commit 回到unmodified 
```
----------------------------------------------------------------------------
# 增加與修改
```
git log
git add .
git commit -m "輸入變更說明"
git log
git status -s (精簡顯示)
git diff (顯示現在的內容差異)
git diff --cached (顯示之前的內容差異) 查看 status
git diff HEAD (顯示所有?) 查看 status 與 unstatus
git add .
git commit
```
----------------------------------------------------------------------------
# 返回
```
git log --oneline

git add 111.txt
git commit --amend --no-edit (強制將111.txt檔案加入並且不作註解說明)

staged返回到modified
--(modified -> staged)
修改1.txt內容
git add 1.txt 

--(staged -> modified)
git reset 1.txt

git reflog (查看歷史記錄)
```
----------------------------------------------------------------------------
# 跳版 HEAD是版本指標器
```
git reset --hard HEAD^ (回上一版)
git reset --hard HEAD^^ (回上上一版)
git reset --hard HEAD~3 (回上第三版)
git reset --hard ID號碼 (回上指定的版)
git reset --hard HEAD@{2}(回上指定的版)
```

----------------------------------------------------------------------------
# 回到之前版本使用 checkout 針對單一檔案 
```
git chcekout c356e34 -- 123.txt (git chcekout ID -- 檔名)
git add 123.txt
git commit -m "dfcsdsd"
```

----------------------------------------------------------------------------
# 分支 branch (有兩種方法)
```
git log --oneline --graph

git branch dev (建立名稱為 dev 的分支)
git branch (查看分支)
git checkout dev (切換分支)
git branch -d dev (刪除分支) 不能在將要刪除的分支執行 

git checkout -b dev (建立名稱為 dev 的分支 並且切換分支)

git commit -am "wgaawrg" (git add 與 git commit 同時執行，只針對已經存在的檔案)

git merge --no-ff -m "dvdfvdfvfv" dev (合併)
```

----------------------------------------------------------------------------
# merge 分支衝突(conflict)
```
修改檔案
git merge dev
merge不過 進入檔案作手動修改檔案
git commit -am "svsdvs"
```

----------------------------------------------------------------------------
# rebase 分支衝突 (使用上要很小心 因為會覆蓋掉或抹掉版本記錄)
rebase 有三個指令
```
git rebase --continue
git rebase --skip
git rebase --abort
```

當有兩個分支 branchA branchB 使用 rebase 就會在記憶體建構出沒有名稱的 branchX
```
git log --oneline --graph
git checkout dev
git log --oneline --graph
git checkout master
git rebase dev
手動修改衝突
git add 123.txt
git rebase --continue
```

----------------------------------------------------------------------------
# stash 臨時修改 (暫存版本)
```
git checkout dev
修改檔案內容 但是還不要 commit
git status -s (會發現有檔案內容已經被修改)
git stash (將修改中的檔案暫存)
git status -s (未發現在任何修改)
git checkout -b MMM (建立另一個分支)
修改檔案內容 
git commit -am "sdsdfds"
git checkout master
git merge --no-ff -m "dvdfvdfvfv" MMM
手動修改衝突
git commit -am "svddsdvs"
git log --oneline --graph
git checkout dev
git stash pop
```
----------------------------------------------------------------------------
# github 線上

github -> New repository

HTTPS SSH link
```
git remote add origin https://github.com/MorvanZhou/git-demo.git
git push -u origin master     # 推送本地 master 去 origin
git push -u origin dev        # 推送本地 dev  去 origin

手動修改本地檔案
git commit -am "cdcd"
git push -u origin master
```

# Source Insight與github的使用
uft8有正面的支持，其默認編碼方式為ANSI碼

# source-insight-vim
(https://github.com/kiddlu/Source-Insight-config)


# 將vim打造成source insight

ctags
```
sudo apt-get install ctags
or
sudo apt-get install exuberant-ctags
```

# 如何在linux（ubuntu）下安裝source insight
安裝wine
```wine ~/Desktop/Si35Setup.exe
```

啟動source insight建立工程
```wine "c:\Program Files\Source Insight 3\Insight3.exe"
```

編寫一個簡單的腳本方便每次啟動source insight
```!/bin/bash
wine "c:\Program Files\Source Insight 3\Insight3.exe" &
```

-------------------


Git 是 Linus Torvalds 寫的， 也就是寫企鵝系統 Linux 的那個。 你可以看看他 介紹 Git 的影片。 裡面一直說用 Subversion 的人很笨，所以他聽起來有點沒水準。 世上的人不可能每個人都像他那麼聰明吧？ Linux 的版本管理就是用 Git 的喔， 所以 Git 也很適合超大型的檔案版本管理。 Git 很快也很省空間。 它利用分散式的管理方法， 也就是說每個人下載的版本裡有包含有史以來更改過的紀錄。 沒有一個人的版本是主要的版本， 你喜歡把自己的版本怎麼改就怎麼改， 那你喜歡接受任何人的更改就接受人和人的更改。 這樣來說，不就天下大亂？ Linus 說不會， 因為他只接收他信任的人的修改， 不會隨便去跟阿貓阿狗的程式碼合併。 而他信任的人也同樣的只會接受他們信任的人的修改， 依此類推。

GIT 功能太多，我也不想那麼瞭解。夠用就好。先貼一下 command 介紹。

$ git init         # 開始用 Git 來管理
$ git add .        # 把所有檔案加入 Git
$ git commit -a       # 做成一個版本
$ git commit -a -m "your message here"  # commit 時直接寫訊息， 不用到下個螢幕上寫
$ git tag v0.02       # 本版別名取為 v0.02
$ git tag v0.03 40e3e      # 把版本 40e3e 取名為 v0.03;
$ git status       # 查詢從上個版本到現在哪些檔案被修改
$ git diff        # 查詢從上個版本到現在哪幾行被修改
$ git diff v0.01 v0.03      # 查詢兩個版本間的差異
$ git diff v0.01:story.txt v0.03:story.txt   # 查詢兩個版本間某個檔案的差異
$ git log        # 查詢有史以來哪幾個檔案被修改
$ git log -p        # 查詢有史以來哪幾行被修改
$ git log --stat --summary     # 查詢每個版本間變動的檔案跟行數
$ git show v1.01       # 查詢 v1.01 版裡的修改內容
$ git show v1.01:story.txt     # 叫出在 v1.01 版時的 story.txt 檔案
$ git show v1.01:story.txt > test.txt   # 把 v1.01 版的 story.txt 抓出來，放入一個叫 test.txt 的檔案
$ git show HEAD      # 看此版本修改的資料
$ git show HEAD^      # 看此版本前一版的修改的資料
$ git show HEAD^^      # 看此版本前前一版的修改的資料
$ git show HEAD~4      # 看此版本前前前前一版的修改的資料
$ gitk        # 版本瀏覽軟體, GUI
$ git gui        # 瀏覽從上一版本到現在變動的地方; 沒辦法顯示中文
下列就我用到的部份。整理一下。
--- Remote 端建好progect ，但還沒上傳。
1. mkdir 目錄      // 建好目錄。
2. git init        // initial 完後，並將檔案放入
3. git add .        // 將檔案加入git
4. $ git remote add origin [remote repository.git] // remote add告訴 GIT 我的 source code 要上傳到哪裡去
         // ex: git remote add origin git@10.1.2.212:RD3/C2CSA_Main.git
5. $ git commit -m "註解" -a
6. $ git tag v0.10 XXXX     // 建立 tag
7. $ git push origin master --tags    // 上傳

------------------------------------------------------------------------------
$ git remote -v   // 可以看 remote repository.git
$ git remote rm origin  // 如果 remote repository.git 設錯。可以用 rm 殺掉
------------------------------------------------------------------------------

--- Remote 已有project，複製到 local 端，再做 sync
1. git clone -v [remote repository.git] checkout // 將 project 下載 checkout 目錄
2. 將修改和新增的檔案放入
3. git add .
4. git commit -a -m "註解"
5. git log        // 查看 LOG
6. git push origin master --tags    // 上傳


--- Remote 已有project，下載 git server 上新的版本
1. git pull origin master             // 下載 master 版本
2. git reset --hard                     // 回覆的上次下載的 master 版本 
Reference :
1. http://www.qweruiop.org/nchcrails/posts/49
2. http://plog.longwin.com.tw/my_note-unix/2009/05/20/git-learn-test-command-2009
3. http://www.technow.com.hk/git-learn

-------------------------------------------

# git command

Git 基本知識

由 project/.git/config 可知: (若有更多, 亦可由此得知)

origin(remote) 是 Repository 的版本
master(branch) 是 local 端, 正在修改的版本
平常沒事不要去動到 origin, 如果動到, 可用 git reset --hard 回覆到沒修改的狀態.


1. git tag
     git tag                                → 列出既有 tag
     git tag -l "XX.*"                 → 搜尋XX.*

    How to: Delete a remote Git tag
        tag named '12345'
        git tag -d 12345
        git push origin :refs/tags/12345

2. git reset
     git reset xxxx --hard         →  強制恢復到某一版本
     git reset --soft HEAD^     →  執行 git commit，發現訊息寫錯想要修改，可以使用。
                                                      會刪掉 commit，在執行一次 commit 就可。

3. git branch & git checkout
     local 端產生新的 branch
     git branch                                    → 列出目前有多少 branch
     git branch -r                                → 列出所有 Repository branch
     git branch -a                               → 列出所有 branch
     git branch new-branch               → 產生新的 branch (名稱: new-branch), 若沒有特別指定,
                                                               會由目前所在的 branch / master 直接複製一份
     git branch new-branch master  → 由 master 產生新的 branch(new-branch)
     git branch new-branch v1          → 由 tag(v1) 產生新的 branch(new-branch)
     git branch -d new-branch           → 刪除 new-branch
     git branch -D new-branch           → 強制刪除 new-branch
     git checkout -b new-branch test → 產生新的 branch, 並同時切換過去 new-branch

     local 端切換 branch
     git checkout branch-name          → 切換到 branch-name
     git checkout -b new-branch test → 產生新的 branch, 並同時切換過去 new-branch
     git checkout filename                  → 還原檔案到 Repository 狀態
     git checkout HEAD                      → 將所有檔案都還原到上一版(最後一次 commit 的版本).
                                                                 (git checkout -f 亦可)
     git checkout xxxx                          → 將所有檔案都還原到 xxxx commit 的版本
     git checkout -- *                            → 恢復到上一次 Commit 的狀態
                                                                  (* 改成檔名, 就可以只恢復那個檔案)

     如何在 remote site 增加/移除一個 branch
     git push origin origin:refs/heads/branch_name
                                                           → 如果 branch_name 不存在的話
     git push origin local_branch_name:remote_branch_name
                                                           → 如果 branch 已經在 local 了，只是要推上去
or 
     git push origin HEAD                      → 如果 branch 已經在 local 了，只是要推上去

     如何移除 remote site 的 branch
     git push origin :heads/branch_name
                                                            → branch_name 是你想要移除的 remote branch 名稱

     開始追蹤 remote branch (當你下一次 pull時, 你會對那個新的 branch_name做 sync)
     git checkout --track -b branch_name origin/branch_name




4. git commit
     git commit -m "註解" -a
     git commit -F commit.txt -a



5. git pull & push
     git push origin master --tags
                                                     → master  是你想要推上的 branch, --tags 若有 tag 一起推上.
     git pull origin master
                                                     → master  是你想要 sync 的 branch.

6. git blame
     git blame 是一個看誰在哪一版修改了什麼的工具。
     git blame hello.c


7. git rm filename
    Git 刪除檔案 →





