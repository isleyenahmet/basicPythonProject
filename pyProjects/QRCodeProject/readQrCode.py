#Projeden önce pip install pyzbar
#Bu proje qr kodu okumamizi sağlar

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/VICTUS/Desktop/projeler/newQRCode2.png')
result = decode(img)

print(result)