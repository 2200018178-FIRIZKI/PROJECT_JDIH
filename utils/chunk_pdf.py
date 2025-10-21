

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def chunk_pdf_ocr(pdf_path, chunk_size=500):
    """
    Extract text from a scanned PDF using OCR, split into chunks.
    Returns a list of strings (chunks).
    """
    from pdf2image import convert_from_path
    import pytesseract
    from PIL import Image

    images = convert_from_path(pdf_path)
    all_text = ""
    for img in images:
        text = pytesseract.image_to_string(img, lang='eng')
        all_text += text + "\n"

    # Split text into chunks
    chunks = []
    current = ""
    for line in all_text.splitlines():
        if len(current) + len(line) < chunk_size:
            current += line + " "
        else:
            chunks.append(current.strip())
            current = line + " "
    if current.strip():
        chunks.append(current.strip())
    return [c for c in chunks if c]

if __name__ == "__main__":
    pdf_path = "data/view.pdf"
    chunks = chunk_pdf_ocr(pdf_path)
    print(f"Jumlah chunk yang dihasilkan: {len(chunks)}")
    if len(chunks) > 0:
        print("Contoh chunk:", chunks[0])
    else:
        print("Tidak ada chunk yang dihasilkan dari PDF!")
