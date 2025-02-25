
import tkinter as tk
from tkinter import filedialog, messagebox
from document_processor import DocumentProcessor
from ocr_processor import OCRProcessor
from table_extractor import TableExtractor
from output_handler import OutputHandler
from nlp_processor import NLPProcessor
from search_engine import SearchEngine
from logger import Logger

class PDFProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Destekli PDF İşleyici")
        self.root.geometry("600x400")

        self.input_path = tk.StringVar()
        self.output_path = "outputs"

        tk.Label(root, text="PDF Dosya Yolu:").pack(pady=5)
        tk.Entry(root, textvariable=self.input_path, width=50).pack()

        tk.Button(root, text="PDF Seç", command=self.browse_pdf).pack(pady=5)
        tk.Button(root, text="İşlemi Başlat", command=self.process_pdf).pack(pady=5)
        tk.Button(root, text="Akıllı Arama", command=self.search_query).pack(pady=5)
        tk.Button(root, text="Çıkış", command=root.quit).pack(pady=5)

    def browse_pdf(self):
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if filename:
            self.input_path.set(filename)

    def process_pdf(self):
        input_path = self.input_path.get()
        if not input_path:
            messagebox.showerror("Hata", "Lütfen bir PDF dosyası seçin.")
            return

        Logger.log("Belge işleme başlatıldı.")
        doc_processor = DocumentProcessor(input_path)
        images = doc_processor.convert_pdf_to_images()

        # OCR İşlemi
        Logger.log("OCR işlemi başlatıldı.")
        ocr = OCRProcessor()
        extracted_text = ""
        for img in images:
            extracted_text += ocr.extract_text(img)

        # Tablo Çıkarma
        Logger.log("Tablo çıkarma işlemi başlatıldı.")
        table_extractor = TableExtractor()
        for img in images:
            tables = table_extractor.extract_tables(img)
            print(f"{len(tables)} tablo bulundu.")

        # NLP Analizi
        nlp = NLPProcessor()
        summary = nlp.summarize_text(extracted_text)
        sentiment = nlp.analyze_sentiment(extracted_text)

        # Sonuçları Göster
        messagebox.showinfo("Özet", f"Metin Özeti:\n{summary}")
        messagebox.showinfo("Duygu Analizi", f"Metin Duygusu: {sentiment}")

        # Metni Kaydet
        with open("outputs/extracted_texts.txt", "w") as f:
            f.write(extracted_text)

        messagebox.showinfo("Başarılı", "Tüm işlemler tamamlandı!")

    def search_query(self):
        query = tk.simpledialog.askstring("Arama", "Aramak istediğiniz kelimeyi girin:")
        if query:
            search_engine = SearchEngine()
            result = search_engine.query(query)
            messagebox.showinfo("Arama Sonucu", result)
