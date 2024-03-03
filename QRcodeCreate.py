import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer

typeiscircle = False # проверка типа qr-кода
def create_qr(txt):
    # параметры изображения QR-кода
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=30,
        border=2,
    )
    # созание кода
    qr.add_data(txt)
    qr.make(fit=True)
    # Проверка на тип QR-кода
    if typeiscircle:
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
    else:
        img = qr.make_image(fill_color="black", back_color="white")

    qr.clear()
    img.save('qr-code.png')
