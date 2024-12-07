import qrcode as qr
qr_image = qr.make(input("Enter the data to save in qrcode: "))
qr_image.save(input("Enter the Filename to save: "))
print("qrcode created successfully")