import qrcode


# List of texts to be converted to QR codes
def generate_qr_codes(texts):
    for text in texts:
        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image as a PNG file with filename same as input text
        img.save("qr11.png")


input_texts = ["https://verify.ssg.secure-smart-guard.com?qrCode=QR00011"]
generate_qr_codes(input_texts)
