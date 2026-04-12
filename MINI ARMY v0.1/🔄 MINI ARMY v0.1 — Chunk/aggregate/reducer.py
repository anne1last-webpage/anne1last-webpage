# aggregate/reducer.py
from collections import defaultdict

def init_global_state():
    return {
        "records": 0,
        "total_bytes": 0,
        "total_billed": 0,
        "by_country": defaultdict(lambda: {
            "sessions": 0,
            "total_bytes": 0,
            "total_duration": 0,
            "total_billing": 0
        })
    }


def reduce(global_state, chunk_summary, chunk_by_country):
    global_state["records"] += chunk_summary["records"]
    global_state["total_bytes"] += chunk_summary["total_bytes"]
    global_state["total_billed"] += chunk_summary["total_billed"]

    for c, v in chunk_by_country.items():
        g = global_state["by_country"][c]
        g["sessions"] += v["sessions"]
        g["total_bytes"] += v["total_bytes"]
        g["total_duration"] += v["avg_duration_sec"] * v["sessions"]
        g["total_billing"] += v["avg_billing_usd"] * v["sessions"]

    return global_state


def finalize(global_state):
    result = {}
    for c, v in global_state["by_country"].items():
        result[c] = {
            "sessions": v["sessions"],
            "total_bytes": v["total_bytes"],
            "avg_duration_sec": v["total_duration"] / v["sessions"],
            "avg_billing_usd": v["total_billing"] / v["sessions"]
        }

    return {
        "summary": {
            "records": global_state["records"],
            "total_bytes": global_state["total_bytes"],
            "total_billed": global_state["total_billed"]
        },
        "by_origin_country": result
    }

✅ คำนวณค่าเฉลี่ยแบบถูกต้อง
✅ ไม่สูญเสียความแม่นยำ 
