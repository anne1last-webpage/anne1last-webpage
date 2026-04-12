หน้าที่: คำนวณ billing ใหม่ (ไม่เชื่อ input)
# validate/billing.py
from .units import bytes_to_mib

def recompute_billing(bytes_total: int, rate_per_mib_usd: float) -> float:
    usage_mib = bytes_to_mib(bytes_total)
    return usage_mib * rate_per_mib_usd

def billing_delta(input_billing: float, recomputed: float) -> float:
    return abs(input_billing - recomputed)

✅ ตรงกับแนวคิด “ต่อต้านการโจมตีจาก upstream billing”
🦸🦸🦸🦸🦸🦸🦸🦸🦸🦸
