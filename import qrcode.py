import qrcode

# wifi details
ssid = "Ra"
password = "D9C43717"
security = "WPA"

# format the wifi qr string (no spaces)
wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

# generate qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(wifi_data)
qr.make(fit=True)

# image (use make_image)
img = qr.make_image(fill_color="black", back_color="white")

# save
img.save("wifi_qrcode.png")
print("wifi QR code saved as wifi_qrcode.png")
