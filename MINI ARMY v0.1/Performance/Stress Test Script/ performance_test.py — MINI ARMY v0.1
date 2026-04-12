🧪 performance_test.py — MINI ARMY v0.1
แนวคิด
สคริปต์นี้จะ:
•วัดเวลาแต่ละ stage
•วัด throughput (records/sec)
•วัด memory แบบคร่าว ๆ
•ใช้โค้ดจริงของ MINI ARMY
1️⃣ โครงสร้างไฟล์ที่ต้องมี
mini_army/
├── ingest/
├── validate/
├── aggregate/
├── fairness/
├── output/
├── main.py
├── performance_test.py   ✅
└── sample_dataset_one_batch.json
 
2️⃣ สคริปต์ performance_test.py
  # performance_test.py
import time
import tracemalloc

from ingest.load_records import load_records
from aggregate.daily_summary import daily_totals
from aggregate.by_country import aggregate_by_origin
from fairness.proportional_check import check_fairness

DATASET_PATH = "sample_dataset_one_batch.json"
RATE_PER_MIB_USD = 0.01
EPSILON = 1e-6


def run_performance_test():
    print("=== MINI ARMY v0.1 Performance Test ===")

    tracemalloc.start()
    start_total = time.perf_counter()

    # 1. Ingest
    t0 = time.perf_counter()
    records = load_records(DATASET_PATH)
    t1 = time.perf_counter()

    record_count = len(records)

    # 2. Aggregate
    t2 = time.perf_counter()
    summary = daily_totals(records)
    by_country = aggregate_by_origin(records)
    t3 = time.perf_counter()

    # 3. Fairness / Billing Validation
    t4 = time.perf_counter()
    violations = check_fairness(
        records,
        rate_per_mib_usd=RATE_PER_MIB_USD,
        epsilon=EPSILON
    )
    t5 = time.perf_counter()

    end_total = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    total_time = end_total - start_total
    throughput = record_count / total_time if total_time > 0 else 0

    print("\n--- Results ---")
    print(f"Records processed        : {record_count}")
    print(f"Ingest time (sec)        : {t1 - t0:.4f}")
    print(f"Aggregation time (sec)  : {t3 - t2:.4f}")
    print(f"Validation time (sec)   : {t5 - t4:.4f}")
    print(f"Total runtime (sec)     : {total_time:.4f}")
    print(f"Throughput (rec/sec)    : {throughput:,.0f}")
    print(f"Violations found        : {len(violations)}")
    print(f"Peak memory (MB)        : {peak / 1024 / 1024:.2f}")

    print("\n=== Test Finished ===")


if __name__ == "__main__":
    run_performance_test()

3️⃣ วิธีรันทดสอบ
python performance_test.py

4️⃣ การตีความผลลัพธ์ (สำคัญ)
ตัวอย่างผล:                                     Records processed        : 100000
Ingest time (sec)        : 0.12
Aggregation time (sec)  : 0.18
Validation time (sec)   : 0.31
Total runtime (sec)     : 0.64
Throughput (rec/sec)    : 156,250
Violations found        : 842
Peak memory (MB)        : 92.4

5️⃣ ใช้เป็น Stress Test ได้อย่างไร
วิธีง่ายที่สุด
1.คัดลอก dataset เดิมหลาย ๆ ครั้ง
2.รวมเป็นไฟล์ใหญ่ (100k / 1M)
3.รัน script เดิมซ้ำ
สัญญาณที่ต้องหยุด
•Peak memory พุ่งผิดปกติ
•Runtime โตแบบ exponential
•OS เริ่ม swap หนัก
6️⃣ เหตุผลที่สคริปต์นี้ “พอดี”
•ไม่ซับซ้อน
•ไม่บิดเบือนผล
•ใช้โค้ดจริง
•เหมาะกับ v0.1
นี่คือการทดสอบเพื่อ “ตัดสินใจ”
ไม่ใช่เพื่ออวดตัวเลข
