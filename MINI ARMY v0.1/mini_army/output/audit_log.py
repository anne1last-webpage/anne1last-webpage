สำหรับ MINI ARMY v0.1
ใช้สำหรับบันทึก audit log (เช่น การตรวจสอบ, การ flag, หรือการบันทึกเหตุการณ์สำคัญ) 
# output/audit_log.py

import json
from datetime import datetime

def write_audit_log(path: str, log_entries: list):
    """
    บันทึก audit log เป็นไฟล์ JSON
    log_entries: list ของ dict เช่น
      [
        {"timestamp": "2026-04-12T17:45:00Z", "event": "violation", "session_id": "abc123", "delta": 0.0023},
        {"timestamp": "2026-04-12T17:46:00Z", "event": "summary", "records": 1000}
      ]
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(log_entries, f, ensure_ascii=False, indent=2)

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

วิธีใช้งาน:
•สะสม log_entries เป็น list แล้วเรียก write_audit_log("audit_log.json", log_entries)
•ใช้ log_violation() หรือ log_summary() เพื่อสร้าง entry
ตัวอย่างการบันทึก:from output.audit_log import write_audit_log, log_violation, log_summary

logs = []
logs.append(log_violation("abc123", 0.0023))
logs.append(log_summary(1000))

write_audit_log("audit_log.json", logs)

