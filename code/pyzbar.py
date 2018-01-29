

# https://ludusrusso.cc/2018/01/22/opencv-barcode-reader/
from pyzbar.pyzbar import decode
import cv2
import requests


def get_barcode_info(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray_img)

    if len(barcodes) == 1:
        code = barcodes[0].data
        url = "https://it.openfoodfacts.org/api/v0/product/{}.json".format(code)
        data = requests.get(url).json()
        if data["status"] == 1:
            product = data["product"]
            brand = product["brands"]
            return "produttore: {}    nome: {}".format(product["brands"], product["product_name"])
        else:
            return "Prodotto non trovato!"
    else:
        return "Codice a barre non trovato!"

cap = cv2.VideoCapture(0)
while(True):
  ret, frame = cap.read()
  info = get_barcode_info(frame)
  # cv2.putText(frame, info, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,255,0), 1)
  #print(info)

  test = decode(frame)
  cv2.putText(frame, str(test), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)
  #jjh = test[0]
  #cv2.putText(frame, format(int(test)), (230, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
  #cv2.putText(frame, test, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)
  #print(test)
  #print(jjh)

  cv2.imshow('Codice a Barre', frame)
  code = cv2.waitKey(30)
  if code == ord('q'):
      break







'''

from pyzbar.pyzbar import decode
import cv2

filename = "qrcode.png"
img = cv2.imread(filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

barcodes = decode(gray_img)
print(barcodes)

'''
