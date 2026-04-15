report_json.py
หน้าที่: ส่งออกผลลัพธ์
# output/report_json.py
import json

def write_report(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

