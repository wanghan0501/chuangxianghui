# -*- coding: utf-8 -*-  

"""
Created by Wang Han on 2017/12/28 13:12.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All Rights Reserved.
"""

import qrcode
from PIL import Image

ip_address = "http://112.74.50.182:5000/comment"
qr = qrcode.QRCode(version=2,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=1,
                   )
qr.add_data(ip_address)
qr.make(fit=True)
img = qr.make_image()
img = img.convert("RGBA")

# center icon
icon = Image.open("shuzhifenxiang_favicon.png")
img_w, img_h = img.size

factor = 3.5
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
img.paste(icon, (w, h), icon)

img.save('shuzhifenxiang_qr_code.png')
