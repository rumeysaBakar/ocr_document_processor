import pymupdf as fitz
from PIL import Image


class DocumentProcessor:
    def __init__(self, input_path):
        self.input_path = input_path

    def convert_pdf_to_images(self):
        images = []
        try:
            doc = fitz.open(self.input_path)
            for i in range(len(doc)):
                page = doc.load_page(i)
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                images.append(img)
            print(f" {len(images)} sayfa başarıyla görüntüye dönüştürüldü.")
        except Exception as e:
            print(f"PDF'den görüntüye dönüştürme sırasında hata oluştu: {e}")
        return images
