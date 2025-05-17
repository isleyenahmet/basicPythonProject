#projeden önce pip install qrcode ve pip install Pillow
#Bu projede qr kodumuzu özelleştirdik
import qrcode

data = 'Who am i?'

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)

qr.make(fit=True) #uygun boyutta oluşturmayi saglar
img = qr.make_image(fill_color = 'blue', back_color = 'white') #qr ve arka plan renkleri

img.save('C:/Users/VICTUS/Desktop/projeler/newQRCode2.png')