import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer

img = ''


def create_circle_qr(txt):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=16,
        border=4,
    )
    qr.add_data(txt)
    qr.make(fit=True)
    # Преобразование в png
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer(), fill_color="black",
                        back_color="white")
    qr.clear()
    img.save('qr-code.png')


def create_regular_qr(txt):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=16,
        border=4,
    )
    qr.add_data(txt)
    qr.make(fit=True)
    # Преобразование в png
    img = qr.make_image(fill_color="black",
                        back_color="white")
    qr.clear()
    img.save('qr-code.png')
