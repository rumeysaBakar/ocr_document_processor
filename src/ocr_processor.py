import pytesseract
class OCRProcessor:
    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    def extract_text(self, image):
        try:
            text = pytesseract.image_to_string(image)
            print(" Metin başarıyla çıkarıldı.")
            return text
        except Exception as e:
            print(f"OCR işlemi sırasında hata oluştu: {e}")
            return ""