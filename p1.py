import qrcode
data = "https://www.example.com"
qr = qrcode.QRCode (
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="Black", back_color="White")
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")