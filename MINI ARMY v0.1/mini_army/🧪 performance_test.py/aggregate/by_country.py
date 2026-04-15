หน้าที่: รวมข้อมูลตามประเทศต้นทาง
# aggregate/by_country.py
from statistics import mean

def aggregate_by_origin(records: list):
    grouped = {}
    for r in records:
        c = r['origin_country']
        grouped.setdefault(c, []).append(r)

    result = {}
    for c, lst in grouped.items():
        result[c] = {
            "sessions": len(lst),
            "total_bytes": sum(x['bytes_total'] for x in lst),
            "avg_duration_sec": mean(x['duration_seconds'] for x in lst),
            "avg_billing_usd": mean(x['billing_amount_usd'] for x in lst)
        }
    return result

✅ นี่คือ aggregation พื้นฐานที่คุณทำไว้เดิม
✅ แต่ตอนนี้แยกหน้าที่ชัด 

