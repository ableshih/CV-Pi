"""
如果指定目錄不存在就建立目錄
要不然的話就直接開檔案
"""
import os
path = "d:\\123"
if not os.path.isdir(path):
    os.mkdir(path)
file = open(path + "\\" + "我要開檔案.txt", "w")
