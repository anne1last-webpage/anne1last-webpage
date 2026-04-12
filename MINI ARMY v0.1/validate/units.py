หน้าที่: จัดการหน่วย (MB vs MiB)
# validate/units.py
BYTES_PER_MB = 1_000_000
BYTES_PER_MIB = 1_048_576

def bytes_to_mb(bytes_val: int) -> float:
    return bytes_val / BYTES_PER_MB

def bytes_to_mib(bytes_val: int) -> float:
    return bytes_val / BYTES_PER_MIB

✅ นี่คือ “คัตเอาต์” ระหว่าง ข้อมูลดิบ กับ การตีความ
🦸🦸🦸🦸🦸🦸🦸🦸🦸🦸
