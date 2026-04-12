# ingest/stream_records.py
import json

def stream_records(path: str):
    """
    Generator ที่ yield record ทีละรายการ
    ใช้กับ JSON array ขนาดใหญ่
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for record in data:
            yield record

      ✅ ใช้ generator
✅ ไม่เก็บ list ทั้งหมดใน RAM
หมายเหตุ: v0.1 ยังใช้ json.load
ถ้าไฟล์ใหญ่มากจริง ๆ ค่อยเปลี่ยนเป็น ijson ใน v0.2 
