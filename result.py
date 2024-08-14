from elements.barcode import barcode
from elements.text import extract_ticket_info, extract_title, extract_notes
from path import pdf_path

try:
    result = {
        "title": extract_title(),
        "ticket_info": extract_ticket_info()[0],
        'barcodes': barcode(),
        extract_notes(): None
    }

    # Вывод результата
    print(result)

except FileNotFoundError:
    print(f"Файл {pdf_path} не найден.")
except Exception as e:
    print(f'Произошла ошибка: {e}')