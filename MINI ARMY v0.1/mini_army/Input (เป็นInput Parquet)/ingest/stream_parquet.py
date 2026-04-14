# ingest/stream_parquet.py
import pyarrow.parquet as pq

def stream_parquet(path: str, batch_size: int = 10_000):
    """
    อ่าน Parquet แบบ batch
    เร็ว + ใช้ RAM ต่ำ
    """
    parquet_file = pq.ParquetFile(path)

    for batch in parquet_file.iter_batches(batch_size=batch_size):
        table = batch.to_pydict()
        size = len(table["session_id"])

        for i in range(size):
            yield {
                "session_id": table["session_id"][i],
                "origin_country": table["origin_country"][i],
                "bytes_total": table["bytes_total"][i],
                "duration_seconds": table["duration_seconds"][i],
                "billing_amount_usd": table["billing_amount_usd"][i],
                "billing_rate_per_mib_usd": table["billing_rate_per_mib_usd"][i],
                "timestamp": table["timestamp"][i]
            }

      ✅ เร็วกว่า CSV
✅ เหมาะกับ stress test / production
ใช้กับ main_chunk.py
from ingest.stream_parquet import stream_parquet as stream_records

DATASET_PATH = "data/sample.parquet"
