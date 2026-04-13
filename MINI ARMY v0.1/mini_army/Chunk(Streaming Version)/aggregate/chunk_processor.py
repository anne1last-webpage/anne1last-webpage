# aggregate/chunk_processor.py
from collections import defaultdict
from statistics import mean

def process_chunk(records: list):
    """
    ประมวลผลข้อมูล 1 chunk
    """
    summary = {
        "records": len(records),
        "total_bytes": sum(r["bytes_total"] for r in records),
        "total_billed": sum(r["billing_amount_usd"] for r in records)
    }

    by_country = defaultdict(list)
    for r in records:
        by_country[r["origin_country"]].append(r)

    agg_country = {}
    for c, lst in by_country.items():
        agg_country[c] = {
            "sessions": len(lst),
            "total_bytes": sum(x["bytes_total"] for x in lst),
            "avg_duration_sec": mean(x["duration_seconds"] for x in lst),
            "avg_billing_usd": mean(x["billing_amount_usd"] for x in lst)
        }

    return summary, agg_country

