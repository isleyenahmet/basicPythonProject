import qrcode

data = 'Don\'t forget to subscribe'

img = qrcode.make(data)

img.save('C:/Users/VICTUS/Desktop/projeler/newQRCode.png')
