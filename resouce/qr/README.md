# GENERATE QR CODE

Generate QR code, and you can scan this to visit your website.

## Custom QR CODE
If you want to generate qr code with your own favicon, you can add following code to **generate_qrcode.py** 
```python
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
```
