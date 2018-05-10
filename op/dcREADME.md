# python與OpenCV  人臉辨識  
請使用python2.x  
本篇所附的檔案只是整個OpenCV的一小部分，本篇所附的cv2.pyd是針對python2.x的，要使用python3.x請自行到OpenCV官網下載  
本篇所附上的xml同樣也是其中之二而已，只針對正臉及眼睛做辨識，想做其他辨識也請自行至OpenCV官網下載  


##首先安裝numpy與matplotlib還有Jupyter
*NumPy*：Python語言的一個擴充程式庫。支援高階大量的維度陣
列與矩陣運算，此外也針對陣列運算提供大量的數學函式函式
庫。  
*matplotlib*：python著名的繪圖庫，當中的pyplot子庫提供了與
matlab類似的繪圖API，官網gallery提供了許多的圖樣可供使
用。  
*Jupyter*:是python網頁編輯器ipython的改版，核心皆與ipython相同  
<pre><code>pip install numpy
pip install matplotlib
pip install "ipython[notebook]"</code></pre>  
  
最後在cmd輸入ipython notebook運行Jupyter  
<pre><code>ipython notebook</code></pre>  
  
最後jupyter應該會自己開啟網頁，沒有的話自己輸入網址localhost:8888  
  
  
##上傳檔案及放置檔案  
將cv2.pyd放到 C:\Python27\Lib\site-packages\資料夾當中(python安裝位置有可能不一樣)  
然後在Jupyter首頁中右上角點upload，選擇兩個XML檔及要做人臉辨識的圖片，記得按下upload才會上傳  
  
  
##開始實作人臉及眼睛辨識  
在Jupyter首頁的右上角New一個Notebook  
然後可以開始貼程式碼囉~~  
註解寫在程式碼裡  
<pre><code>
import sys,cv2
import matplotlib.pyplot as plt
%matplotlib inline
image= cv2.imread('sample.jpg')#會用cv2讀取圖片是因為圖片是jpg，matplotlib只能讀取png
#plt.imshow(image) #matplotlib圖片的顏色編碼是BGR
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#在這邊要將BGR轉成RGB才是我們一般看到的顏色
plt.title('Original') #設定圖片的標題
</code></pre>  
  
<pre><code>
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #匯入臉部辨識的方法
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml') #匯入眼睛辨識的方法
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #轉灰階讓系統做判斷
faces = faceCascade.detectMultiScale(
    grayImage,
    scaleFactor=1.1,
    minNeighbors=5, #依照圖片大小調整
    minSize=(30, 30), 
    flags = cv2.CASCADE_SCALE_IMAGE)
#印出辨識到的臉部位置，值分別是 x:x軸起始點，y:y軸起始點，w:x到結束點的寬度，h:y到結束點的高度
#人臉辨識的範圍建議寬高超過70像素
print faces

#在這裡將辨識到的臉依據位置用方框標示出來
for (x, y, w, h) in faces:
    #畫方框(圖片,起始值,結束值,方框顏色RGB(與matplotlib相反),粗細)
    cv2.rectangle(image, (x,y), (x+w, y+h), (14, 201, 255), 2)

    #將臉部區域轉成灰色再繼續做眼睛辨識
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    #print(roi_color)
    eyes = eyeCascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) #畫出眼睛的方框

#plt.imshow(image)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
</code></pre>  
  
<pre><code>
import random
#設定字型
font = cv2.FONT_HERSHEY_SIMPLEX

#隨機加上數字
for (x, y, w, h) in faces:
    cv2.putText(image,str(random.randrange(18, 25)),(x+(w/2)-18,y-10), font, 1, (255,201,14),4) #寫文字
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
</code></pre>  
如果三段程式碼都寫在不同區段的話，在畫框時開始重新RUN就要從第一個區段重新執行  
附上的pythonCV2.ipynb是Jupyter的Notebook檔  
上面的程式碼儲存就是這種檔案，可以直接將這個檔案一樣在Jupyter首頁上傳，並直接開啟就是上面的程式碼了  
