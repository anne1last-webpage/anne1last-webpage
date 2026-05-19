Download Codespace

- *Download clone URL: https://github.com/anne1last-webpage/anne1last-webpage/anne1last-webpage(clone)

- download for: HotUpdateSearchPaths(var hotUpdateSearchPaths = localStorage.getItem('HotUpdateSearchPaths');
if (hotUpdateSearchPaths) {
    jsb.fileUtils.setSearchPaths(JSON.parse(hotUpdateSearchPaths));
}ตรงกับ -› 🔸 ตรวจสอบว่า key 'HotUpdateSearchPaths' มีค่าจริงใน localStorage  
   🔸 ถ้าไม่มีค่า ระบบจะไม่รู้ว่าจะโหลดไฟล์จาก path ไหน → เกมไม่ตอบสนอง)
>__ดาวน์โหลดทรัพยากรให้พร้อมสำหรับการตรวจสอบ__

- download for: SystemJS(require("src/system.bundle.js");
const importMapJson = jsb.fileUtils.getStringFromFile("src/import-map.json");ตรงกับ -›   🔸 ถ้าไฟล์ import-map.json หรือ system.bundle.js เสียหาย → เกมจะไม่เริ่มโหลด  
   🔸 ควรตรวจสอบว่าไฟล์เหล่านี้อยู่ในโฟลเดอร์ src และไม่ถูกลบ)

- download for: Application(System.import('./src/application.js')
.then(({ Application }) => new Application())ตรงกับ -› 🔸 ถ้า application.js มี error หรือไม่ส่งออก class Application → เกมจะไม่เริ่ม)


⚙️ จุดที่ควรตรวจสอบใน index.js
- ฟังก์ชัน checkHotUpdateVersion() และ checkUpdate()  
  🔸 ตรวจสอบว่า URL ของ manifest (project.manifest, version.manifest) ถูกต้อง  
  🔸 ถ้า _updateUrl ว่างหรือไม่ถูกตั้งค่า → ระบบจะไม่โหลดไฟล์ใหม่  

- ฟังก์ชัน _onUpdateFailed()  
  🔸 ถ้าเกิด error แล้วไม่มีการ retry → เกมจะหยุดนิ่ง  
  🔸 สามารถเพิ่ม retry logic เช่น: if (this._retryUpdateTimes <= 3) {
    this.checkHotUpdateVersion();

}

- *ดาวน์โหลดให้ครบตรงกับ: 💡 สรุปแนวทางแก้ไข
- เริ่มจากตรวจสอบว่า HotUpdateSearchPaths มีค่าใน localStorage  
- ตรวจสอบว่าไฟล์ system.bundle.js, import-map.json, และ application.js อยู่ครบ  
- ตรวจสอบว่า updateUrl ถูกตั้งค่าจาก native bridge (init)  
- หากยังไม่ตอบสนอง ให้เพิ่ม log ใน main.js และ index.js เพื่อดูว่าหยุดที่ขั้นตอนใด  


🔍 สรุปหน้าที่ของแต่ละไฟล์
| ไฟล์ | หน้าที่หลัก | ควรทบทวนไหม | หมายเหตุ |
|-----------|------------------|------------------|----------------|
| main.js | โหลดระบบหลักของเกม, ตั้งค่าเส้นทาง HotUpdate, เรียก application.js | ✅ ควรทบทวน | ตรวจสอบว่า HotUpdateSearchPaths ถูกตั้งค่าและอ่านได้จริงจาก localStorage |
| index.js | จัดการ event ของ HotUpdate เช่น ตรวจเวอร์ชัน, โหลด manifest, รีสตาร์ตเกม | ✅ ควรทบทวน | ตรวจสอบ callback เช่น OnUpdateFailed, OnUpdateSucceed, และ OnUpdateProgress ว่าทำงานครบหรือไม่ |
