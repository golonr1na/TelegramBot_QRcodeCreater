import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer

typeiscircle = False
def create_qr(txt):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2,
    )
    qr.add_data(txt)
    qr.make(fit=True)
    if typeiscircle:
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
    else:
        img = qr.make_image(fill_color="black", back_color="white")
    qr.clear()
    img.save('qr-code.png')
