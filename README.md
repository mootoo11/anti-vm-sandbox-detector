
# 🕵️‍♂️ Anti-VM & Sandbox Detection Script

## English

### 🎯 Overview:
This script is designed to detect if it's running inside a virtualized or monitored environment (e.g., VirtualBox, VMware, Sandbox, malware analysis tools). If such an environment is detected, it immediately exits.

---

### ⚙️ How it Works:
The script runs a series of checks:

- 🔍 Detects hardware manufacturer (looking for VM indicators).
- 📋 Scans running processes for analysis tools or VM services.
- 📁 Checks for known sandbox directories.
- ⏱️ Sleep timing to detect time skipping.
- 🧠 Checks RAM capacity.
- 🧮 Verifies number of CPU cores.
- 💾 Checks disk space.
- 🌐 Inspects MAC address prefixes.
- 👤 Analyzes username and hostname.
- ⌛ Verifies system uptime.

If 2 or more checks are suspicious, the script exits.

---

### 🛡️ Purpose:
- **Evade analysis tools like VirusTotal.**
- **Avoid running in virtualized or sandboxed environments.**
- **Only execute when on a real system.**

---

### 🔄 What to Do After Check?
In the final line:
```python
print("✅ OK")
```
You can replace it by running your main program or performing any sensitive operation.
Example:
```python
os.system("start my_program.exe")
```
---

### ✅ Requirements:
- Python 3
- Modules: `psutil`, `requests`

---

### 🔧 Installation:
```bash
pip install -r requirements.txt
```
--
--

## بالعربية

### 🎯 الفكرة العامة:
هذا السكربت صُمم لاكتشاف ما إذا كان البرنامج يعمل في بيئة وهمية أو مراقبة (مثل VirtualBox، VMware، SandBox، أو أدوات تحليل البرامج الضارة). إذا اكتشف ذلك، يقوم بإيقاف نفسه مباشرة.

---

### ⚙️ آلية العمل:
يقوم السكربت بتنفيذ سلسلة من الفحوصات، منها:

- 🔍 التحقق من اسم الشركة المصنعة للوحة الأم أو الجهاز.
- 📋 فحص العمليات النشطة التي قد تدل على بيئة تحليل أو وهمية.
- 📁 البحث عن مجلدات مشبوهة مثل مجلدات الفحص.
- ⏱️ اختبار تأخير (sleep) للتأكد من عدم تخطي الوقت.
- 🧠 قياس حجم الذاكرة العشوائية (RAM).
- 🧮 عدد أنوية المعالج.
- 💾 مساحة القرص.
- 🌐 عنوان MAC.
- 👤 اسم المستخدم واسم الجهاز.
- ⌛ مدة تشغيل النظام (Uptime).

إذا تم رصد علامتين أو أكثر، يعتبر النظام مشبوهاً ويتم إيقاف البرنامج.

---

### 🛡️ الهدف من الكود:
- **التخفي من أدوات التحليل مثل VirusTotal.**
- **منع تشغيل الكود في بيئة مراقبة أو وهمية.**
- **تشغيل الكود فقط إذا تأكد أنه في نظام حقيقي.**

---

### 🔄 ماذا تفعل بعد الكشف؟
في آخر سطر من الكود:
```python
print("✅ OK)
```
يمكنك استبداله بتشغيل برنامجك الأساسي أو تنفيذ أي عملية حساسة.
مثال
```python
os.system("start my_program.exe")
```
---
