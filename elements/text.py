from pdfminer.high_level import extract_text
from path import pdf_path


def extract_ticket_info():
    ticket_info = {}
    text = extract_text(pdf_path)
    info = text.splitlines()
    for pair in info:
        if not pair.strip():
            continue
        if ':' in pair:
            key, value = pair.split(':', 1)
            ticket_info[key.strip()] = value.strip()
    notes = ticket_info.pop("NOTES")
    return ticket_info, notes


def extract_title():
    text = extract_text(pdf_path)
    info = text.splitlines()
    title = info[0] if info else ''
    return title


def extract_notes():
    pass
