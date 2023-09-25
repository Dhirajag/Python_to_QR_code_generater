import qrcode
import image
qr_img = qrcode.make("qr source")  
qr_img.save("qr code.jpg")
