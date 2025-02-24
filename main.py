from modules.call_detector import detect_incoming_call
from modules.outgoing_call_detector import detect_outgoing_call

if __name__ == "__main__":
    print("📞 Aplikasi Pelacakan Panggilan Siap!")
    print("1. Deteksi panggilan masuk")
    print("2. Melakukan panggilan keluar")
    pilihan = input("Pilih (1/2): ")

    if pilihan == "1":
        detect_incoming_call()
    elif pilihan == "2":
        nomor_tujuan = input("Masukkan nomor tujuan: ")
        detect_outgoing_call(nomor_tujuan)
    else:
        print("❌ Pilihan tidak valid.")
