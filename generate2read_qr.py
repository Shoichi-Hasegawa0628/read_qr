#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 以下のモジュールが必要 (QRコード作成用)
# pip install pyzbar
# pip install qrcode
# apt-get install python3-zbar


import qrcode
import cv2
from PIL import Image
from pyzbar.pyzbar import decode

# QRコードの作成
qr = qrcode.QRCode(box_size=15)
qr.add_data('Hello')
qr.make()
img_qr = qr.make_image()
img_qr.save('./data/test.png')
#cv2.imwrite('./data/test.png', img_qr)

#QRコードを読み込む
im = cv2.imread('./data/test.png')
data = decode(im)
input=data[0][0].decode('utf-8', 'ignore')
print(input)

