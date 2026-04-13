หน้าที่: ตรวจ “ความเป็นสัดส่วน”
# fairness/proportional_check.py
from validate.billing import recompute_billing, billing_delta

def check_fairness(records: list, rate_per_mib_usd: float, epsilon: float = 1e-6):
    violations = []

    for r in records:
        recalculated = recompute_billing(
            r['bytes_total'],
            rate_per_mib_usd
        )
        delta = billing_delta(r['billing_amount_usd'], recalculated)

        if delta > epsilon:
            violations.append({
                "session_id": r.get("session_id"),
                "delta": delta
            })

    return violations

✅ นี่คือ “รักษาความเป็นสัดส่วน” ในรูปแบบโค้ดจริง 

