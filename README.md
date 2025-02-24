How to play :
- Pastikan kamu memiliki modem GSM yang mendukung Caller ID.
- Pastikan API Key Google Maps sudah diisi di config.py.
- pip install -r requirements.txt
- pip install serial phonenumbers requests googlemaps
- python main.py

✅ Rekomendasi Modem GSM dengan Caller ID
Huawei E160, E173, E220, E303
Support AT+CLIP (Caller ID)
USB Modem, kompatibel dengan Windows & Linux
Bisa digunakan dengan SIM Card operator seluler

📌 a. Cek Port di Windows
Tekan Win + R, ketik devmgmt.msc (Device Manager).
Cari bagian "Ports (COM & LPT)", akan muncul seperti:
graphql
Salin
Edit
Huawei Mobile Connect - 3G PC UI Interface (COM3)
Catat COM port-nya, misal COM3.

📌 Catatan:
Jika port tidak muncul, kamu mungkin perlu menginstal driver Huawei Mobile Connect.

🎯 Fitur yang Ada
✅ Mendeteksi panggilan keluar (kita yang menelpon ke nmor tujuan) via modem GSM
✅ Mendeteksi panggilan masuk via modem GSM
✅ Menampilkan nomor yang menelpon
✅ Melacak lokasi berdasarkan kode negara dan provider
✅ Menampilkan Google Maps link dari negara asal nomor telepon

🎯 Hasil yang Didapat
Tindakan	Output di Terminal
Ada panggilan masuk	    📞 Panggilan dari +628123456789
Menelepon nomor lain	📞 Menelepon 08123456789...
Panggilan tersambung	✅ Panggilan tersambung.
Panggilan ditutup	    ❌ Panggilan ditutup.



BY ICHAN LUTFI ADITAMA