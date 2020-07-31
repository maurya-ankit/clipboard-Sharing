import qrcode


def qr_img(data):
    img = qrcode.make(data)
    return img
