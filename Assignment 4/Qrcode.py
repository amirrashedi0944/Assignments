import qrcode
text = input("Enter the text: ")
address = input("Enter the address: ")
qr = qrcode.make(f'{text} \n{address}')
qr.save("UserQrcode.jpg")
