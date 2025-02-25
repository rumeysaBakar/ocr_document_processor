
from ultralytics import YOLO

class TableExtractor:
    def __init__(self):
        # YOLO modelini doğru yükle
        self.model = YOLO("models/yolov8n.pt")  # Model dosyan bu dizinde olmalı


    def extract_tables(self, image_path):
        results = self.model(image_path)
        tables = []

        for result in results:
            for box in result.boxes:
                if box.conf[0] > 0.5:  # Güven eşiği
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    tables.append((x1, y1, x2, y2))

        return tables
