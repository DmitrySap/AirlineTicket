from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from PIL import Image
from path import pdf_path, output_path


def barcode():
    try:
        images = convert_from_path(pdf_path)
        image = images[0]
        image.save(output_path)
        image = Image.open(output_path)
        decoded = decode(image)

        if len(decoded) < 2:
            raise ValueError("Недостаточно декодированных штрих-кодов")

        decode_sn = decoded[0].data
        decode_pn = decoded[1].data
        barcodes = decode_pn, decode_sn
        return barcodes

    except Exception as e:
        print(f"Произошла ошибка при декодировании баркодов: {e}")
        return None