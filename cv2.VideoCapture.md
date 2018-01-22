https://ccw1986.blogspot.tw/2017/05/opencv-tutorial.html

https://chtseng.wordpress.com/2016/12/05/opencv-more-on-contours-2/

Open Webcam using OpenCV on Python
By Marc Wang 下午5:06 1 comment
Open Webcam using OpenCV on Python
# encoding: utf-8
import cv2

print "OpenCV Version : " + cv2.__version__

video_capture = cv2.VideoCapture(0)

if video_capture.isOpened():
    print "Camera was opened"
else:
    video_capture.open(0)
    print "Restart camera"

# 顯示所有視訊相關參數
for i in range(0,18):
    print video_capture.get(i)

# 重新設定解析度
ret = video_capture.set(3,320)
ret = video_capture.set(4,240) 

while True:
    # 擷取即時串流影像
    ret, frame = video_capture.read()

    # 顯示擷取影像
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放記憶體
video_capture.release()
cv2.destroyAllWindows()
cv2.VideoCapture(filename) →
開啟指定影片中的串流影像( eg. video.avi )，或指定圖片序列( eg. img_00.jpg、 img_01.jpg… )

cv2.VideoCapture(device) →
開啟指定即時串流裝置

cv2.VideoCapture.isOpened() → retval
檢查VideoCapture是否初始化成功

cv2.VideoCapture.open(param) → retval
開啟指定即時串流裝置、指定影片中的串流影像、指定圖片序列

cv2.VideoCapture.read([image]) → retval, image
從指定串流來源擷取單張影像，該函式會有兩個回傳值，retval表示擷取是否成功，image是擷取回來的影像資料

cv2.VideoCapture.get(propId) → retval
查詢視訊參數，詳細列舉如下 
- CV_CAP_PROP_POS_MSEC . 
- CV_CAP_PROP_POS_FRAMES 
- CV_CAP_PROP_POS_AVI_RATIO 
- CV_CAP_PROP_FRAME_WIDTH 
- CV_CAP_PROP_FRAME_HEIGHT 
- CV_CAP_PROP_FPS 
- CV_CAP_PROP_FOURCC 
- CV_CAP_PROP_FRAME_COUNT 
- CV_CAP_PROP_FORMAT 
- CV_CAP_PROP_MODE 
- CV_CAP_PROP_BRIGHTNESS 
- CV_CAP_PROP_CONTRAST 
- CV_CAP_PROP_SATURATION 
- CV_CAP_PROP_HUE 
- CV_CAP_PROP_GAIN 
- CV_CAP_PROP_EXPOSURE 
- CV_CAP_PROP_CONVERT_RGB 
- CV_CAP_PROP_WHITE_BALANCE_U 
- CV_CAP_PROP_WHITE_BALANCE_V 
- CV_CAP_PROP_RECTIFICATION 
- CV_CAP_PROP_ISO_SPEED 
- CV_CAP_PROP_BUFFERSIZE

cv2.VideoCapture.set(propId, value) → retval
設定視訊參數，參數如get，並不是所有參數都有用，必須視訊裝置有支援

cv2.imshow(winname, mat) → None
顯示影像於視窗中，winname視窗名稱、mat影像物件

cv2.destroyWindow(winname) → None
關閉指定視窗並釋放記憶體

cv2.destroyAllWindows() → None
關閉所有視窗並釋放記憶體

cv2.moveWindow(winname, x, y) → None
移動指定視窗位置

cv2.resizeWindow(winname, width, height) → None
調整指定視窗大小

cv2.waitKey([delay]) → retval
設定delay時間，有點像thread sleep
