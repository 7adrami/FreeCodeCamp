import qrcode

# Data to encode
data = "https://youtu.be/0e2J984t2lE?si=-416V3Tqmv5dSSPF"

# Create QR code
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR grid
    border=4,  # Border thickness
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode.png")

# Show the QR code
img.show()
