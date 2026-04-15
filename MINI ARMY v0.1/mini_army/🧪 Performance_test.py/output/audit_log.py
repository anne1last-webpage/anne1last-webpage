นี่คือโค้ด audit_log.py ที่บันทึกแบบ append (เพิ่มทีละบรรทัด)
เหมาะสำหรับการบันทึก log แบบต่อเนื่อง ไม่ต้องโหลดไฟล์ทั้งหมดเข้ามาใหม่
# output/audit_log.py

import json
from datetime import datetime

def append_audit_log(path: str, log_entry: dict):
    """
    บันทึก log แบบ append (เพิ่มทีละบรรทัด)
    log_entry: dict เช่น {"timestamp": "...", "event": "...", ...}
    """
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

def log_violation(session_id, delta):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "violation",
        "session_id": session_id,
        "delta": delta
    }

def log_summary(records):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "summary",
        "records": records
    }

วิธีใช้งาน:from output.audit_log import append_audit_log, log_violation, log_summary

append_audit_log("audit_log.jsonl", log_violation("abc123", 0.0023))
append_audit_log("audit_log.jsonl", log_summary(1000))

•ไฟล์จะเป็น JSON Lines (แต่ละบรรทัดคือ 1 log entry)
•ไม่ต้องโหลดไฟล์ทั้งหมดเข้ามาใหม่
•เหมาะกับระบบที่ต้องการ log ต่อเนื่องหรือ log ขนาดใหญ่
