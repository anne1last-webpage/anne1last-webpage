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

python performance_test.py
