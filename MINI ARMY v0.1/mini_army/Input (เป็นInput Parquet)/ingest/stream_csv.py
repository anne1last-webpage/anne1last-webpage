รูปแบบ CSV ที่คาดหวัง
session_id,origin_country,bytes_total,duration_seconds,billing_amount_usd,billing_rate_per_mib_usd,timestamp
abc123,TH,1048576,120,0.01,0.01,2026-01-01T00:00:00Z

ingest/stream_csv.py
# ingest/stream_csv.py
import csv

def stream_csv(path: str):
    """
    Generator อ่าน CSV ทีละแถว
    ใช้ RAM ต่ำมาก
    """
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {
                "session_id": row["session_id"],
                "origin_country": row["origin_country"],
                "bytes_total": int(row["bytes_total"]),
                "duration_seconds": int(row["duration_seconds"]),
                "billing_amount_usd": float(row["billing_amount_usd"]),
                "billing_rate_per_mib_usd": float(row["billing_rate_per_mib_usd"]),
                "timestamp": row["timestamp"]
}

✅ อ่านทีละ record
✅ เหมาะกับไฟล์ใหญ่หลาย GB
ใช้กับ main_chunk.py
เปลี่ยนแค่บรรทัดเดียว:
from ingest.stream_csv import stream_csv as stream_records
และเปลี่ยน path:
DATASET_PATH = "data/sample.csv"
✅ logic ที่เหลือ ไม่ต้องแก้เลย
