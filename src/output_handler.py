import os
import pandas as pd

class OutputHandler:
    def __init__(self, output_path="outputs"):
        self.output_path = output_path
        os.makedirs(self.output_path, exist_ok=True)

    def save_texts(self, texts):
        if texts:
            output_file = os.path.join(self.output_path, 'extracted_texts.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                for text in texts:
                    f.write(text + '\n')
            print(f"Metinler {output_file} dosyasına kaydedildi.")
        else:
            print("Kaydedilecek metin bulunamadı.")

    def save_tables(self, tables):
        if tables:
            for i, table in enumerate(tables):
                output_file = os.path.join(self.output_path, f'table_{i + 1}.csv')
                table.to_csv(output_file, index=False)
            print("Tüm tablolar CSV formatında kaydedildi.")
        else:
            print("Kaydedilecek tablo bulunamadı.")
