Python 與 OpenCV 加入線條圖案與文字教學

##直線
若要圖片中加入直線，可以使用 cv2.line 函數：

cv2.line(影像, 開始座標, 結束座標, 顏色, 線條寬度)
以下是一個簡單的範例：
```
'''
import numpy as np
import cv2

# 建立一張 512x512 的 RGB 圖片（黑色）
img = np.zeros((256, 256, 3), np.uint8)

# 將圖片用淺灰色 (200, 200, 200) 填滿
img.fill(200)

# 在圖片上畫一條紅色的對角線，寬度為 5 px
cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# 顯示圖片
cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
```

方框
繪製方框可以使用 cv2.rectangle 函數：

cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
這裡的線條寬度參數若設定為正的值，則代表正常的線條寬度，而若設定為負的值，則代表畫實心的方框。

以下是接續上面的範例，再加上一個方框的程式碼：

import numpy as np
import cv2

img = np.zeros((256, 256, 3), np.uint8)
img.fill(200)

cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# 在圖片上畫一個綠色方框，線條寬度為 2 px
cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), 2)

# 綠色實心方框
cv2.rectangle(img, (40, 80), (100, 140), (0, 255, 0), -1)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




圓圈
繪製圓圈可以使用 cv2.circle 函數：

cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度)
這裡的線條寬度參數若設定為正的值，則代表正常的線條寬度，而若設定為負的值，則代表畫實心的圓圈。

以下是接續先前範例，加入圓圈的程式碼：

import numpy as np
import cv2

img = np.zeros((256, 256, 3), np.uint8)
img.fill(200)

cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), 2)
cv2.rectangle(img, (40, 80), (100, 140), (0, 255, 0), -1)

# 黃色圓圈，線條寬度為 3 px
cv2.circle(img,(90, 210), 30, (0, 255, 255), 3)

# 藍色實心圓圈
cv2.circle(img,(140, 170), 15, (255, 0, 0), -1)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




橢圓形
繪製圓圈可以使用 cv2.circle 函數：

cv2.ellipse(影像, 中心座標, 軸長, 旋轉角度, 起始角度, 結束角度, 顏色, 線條寬度)
中心座標參數就是橢圓的中心點座標，軸長這個參數可用來指定橢圓的半長軸與半短軸的長度，旋轉角度參數可以讓橢圓自由旋轉。

起始角度與結束角度兩個參數比較特別，它們是代表要繪製橢圓的那一個部份，如果要畫出一個完整的橢圓，就可以把起始角度設定為 0，結束角度設定為 360，而如果只要畫出一半的橢圓，就可以把起始角度設定為 0，結束角度設定為 180。

其餘的顏色與校條寬度參數的用法，都與先前介紹的函數相同。

以下是加入橢圓形的程式碼：

import numpy as np
import cv2

img = np.zeros((256, 256, 3), np.uint8)
img.fill(200)

cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), 2)
cv2.rectangle(img, (40, 80), (100, 140), (0, 255, 0), -1)
cv2.circle(img,(90, 210), 30, (0, 255, 255), 3)
cv2.circle(img,(140, 170), 15, (255, 0, 0), -1)

# 傾斜 45 度的紫色橢圓形
cv2.ellipse(img, (180, 200), (25, 55), 45, 0, 360, (205, 0, 255), 2)

# 傾斜 45 度的半個實心橢圓
cv2.ellipse(img, (180, 200), (20, 50), 45, 0, 180, (255, 0, 255), -1)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




折線
繪製折線可以使用 cv2.polylines 函數：

cv2.polylines(影像, 頂點座標, 封閉型, 顏色, 線條寬度)
其中頂點座標就是線段之間的頂點座標，這個參數必須要是一個形狀為 (頂點數量, 1, 2) 的陣列，所以通常在把資料放進 cv2.polylines 函數畫圖之前，會先用 reshape 調整一下（請參考下方的範例）。

封閉型參數是一個布林值，若設定為 True 的話，它就會自動把最後一個點座標跟第一個點座標連起來，反之就是不連這一條線段。

以下是使用折線的方式，畫出一個四邊形的程式碼：

import numpy as np
import cv2

img = np.zeros((256, 256, 3), np.uint8)
img.fill(200)

cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), 2)
cv2.rectangle(img, (40, 80), (100, 140), (0, 255, 0), -1)
cv2.circle(img,(90, 210), 30, (0, 255, 255), 3)
cv2.circle(img,(140, 170), 15, (255, 0, 0), -1)
cv2.ellipse(img, (180, 200), (25, 55), 45, 0, 360, (205, 0, 255), 2)
cv2.ellipse(img, (180, 200), (20, 50), 45, 0, 180, (255, 0, 255), -1)

# 設定多邊形頂點座標
pts = np.array([[170, 55], [165, 75], [220, 80], [200, 60]], np.int32)

# 將座標轉為 (頂點數量, 1, 2) 的陣列
pts = pts.reshape((-1, 1, 2))

# 繪製多邊形
cv2.polylines(img, [pts], True, (255, 255, 0), 4)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



文字
若要在圖片上加上文字，可以使用 cv2.putText 函數：

cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
這裡的座標是指文字的左下角座標點，而字型可使用 OpenCV 內建的幾種字型（請看以下範例），大小則是代表字型的縮放比例（例如 1.5 就代表放大 1.5 倍）。

最後一項線條種類參數可以指定如何繪製線條，若想要有反鋸齒（anti-aliasing）的效果，可設定為 cv2.LINE_AA。這項參數也可以省略不寫，若省略的話預設值為 cv2.LINE_8。

import numpy as np
import cv2

img = np.zeros((400, 400, 3), np.uint8)
img.fill(90)

# 文字
text = 'Hello, OpenCV!'

# 使用各種字體
cv2.putText(img, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 80), cv2.FONT_HERSHEY_PLAIN,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 120), cv2.FONT_HERSHEY_DUPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 160), cv2.FONT_HERSHEY_COMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 200), cv2.FONT_HERSHEY_TRIPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 240), cv2.FONT_HERSHEY_COMPLEX_SMALL,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 280), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 320), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




使用 TTF 字型檔
OpenCV 所內建的字體很少，如果需要使用到別的字體，可以靠著 PIL 模組，直接從 ttf 字型檔來讀取字體。以下是一個使用中文字型檔，顯示中文字的範例：

import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image

img = np.zeros((450, 450, 3), np.uint8)

# 將背景設定為大紅色
img[:] = (0, 0, 255)

# 文字
text = '招財\n進寶'

# 指定 TTF 字體檔
fontPath = "./康熙字典體.ttf"

# 載入字體
font = ImageFont.truetype(fontPath, 192)

# 將 NumPy 陣列轉為 PIL 影像
imgPil = Image.fromarray(img)

# 在圖片上加入文字
draw = ImageDraw.Draw(imgPil)
draw.text((30, 30),  text, font = font, fill = (0, 0, 0))

# 將 PIL 影像轉回 NumPy 陣列
img = np.array(imgPil)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



