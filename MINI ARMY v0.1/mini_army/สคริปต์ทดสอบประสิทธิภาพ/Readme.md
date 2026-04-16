ได้เลยค่ะ ✅
ด้านล่างคือ สคริปต์ทดสอบประสิทธิภาพ (Performance / Stress Test Script)

ออกแบบมาให้ ใช้กับ MINI ARMY v0.1 แบบ Minimal Run ได้ทันที
ไม่ต้องพึ่งไลบรารีภายนอก 


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


