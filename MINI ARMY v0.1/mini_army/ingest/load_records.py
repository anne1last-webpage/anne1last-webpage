หน้าที่: รับข้อมูลเข้า (Ingest)
# ingest/load_records.py
import json

def load_records(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
      ✅ แยกการโหลดไฟล์ออกมา
✅ เปลี่ยนแหล่งข้อมูลในอนาคตได้ (HTTP / Kafka)
 
