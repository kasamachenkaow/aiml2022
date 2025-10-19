import qrcode
from pathlib import Path

folder = "psg_psg"
area_id = "psg_hq"

Path(folder).mkdir(parents=True, exist_ok=True)

# List of texts to be converted to QR codes
def generate_qr_codes(texts):
    for text in texts:
        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text["url"])
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image as a PNG file with filename same as input text
        filename = folder + "/" + text["name"] + ".png"
        img.save(filename)


input_texts = [{
    "url": "https://verify-psg.secure-smart-guard.com?areaId={:s}&qrCode=QR{:05d}".format(area_id, i),
    "name": "QR{:05d}".format(i),
} for i in range(1, 51)]
generate_qr_codes(input_texts)
