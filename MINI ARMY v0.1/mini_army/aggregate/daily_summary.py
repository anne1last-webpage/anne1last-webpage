MINI ARMY v0.1
(ใช้สรุปข้อมูลรวมทั้ง batch แบบง่าย ๆ)
# aggregate/daily_summary.py

def daily_totals(records: list):
    """
    รับ list ของ record แล้วคืนค่า summary พื้นฐาน
    """
    return {
        "records": len(records),
        "total_bytes": sum(r['bytes_total'] for r in records),
        "total_billed": sum(r['billing_amount_usd'] for r in records)
    }

วิธีใช้:from aggregate.daily_summary import daily_totals

summary = daily_totals(records)
print(summary)

ผลลัพธ์ตัวอย่าง:{
  "records": 3,
  "total_bytes": 3670016,
  "total_billed": 0.035
}

