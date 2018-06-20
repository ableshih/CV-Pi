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
















