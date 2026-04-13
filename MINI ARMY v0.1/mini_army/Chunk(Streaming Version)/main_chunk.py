# main_chunk.py
from ingest.stream_records import stream_records
from aggregate.chunk_processor import process_chunk
from aggregate.reducer import init_global_state, reduce, finalize
from output.report_json import write_report

CHUNK_SIZE = 10_000
DATASET_PATH = "sample_dataset_one_batch.json"

def run_chunk_pipeline():
    global_state = init_global_state()
    buffer = []

    for record in stream_records(DATASET_PATH):
        buffer.append(record)

        if len(buffer) >= CHUNK_SIZE:
            summary, by_country = process_chunk(buffer)
            global_state = reduce(global_state, summary, by_country)
            buffer.clear()

    # process remaining
    if buffer:
        summary, by_country = process_chunk(buffer)
        global_state = reduce(global_state, summary, by_country)

    result = finalize(global_state)
    write_report("daily_report_chunk.json", result)

    print("MINI ARMY v0.1 (chunk mode) finished")


if __name__ == "__main__":
    run_chunk_pipeline()

