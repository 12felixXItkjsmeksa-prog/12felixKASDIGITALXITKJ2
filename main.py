# APLIKASI KAS DIGITAL - XI TKJ 2 - ABSEN 12
from database import buat_tabel
from siswa import menu_siswa
from transaksi import menu_pembayaran, menu_pengeluaran, menu_riwayat
from laporan import dashboard_saldo, laporan_keuangan

def menu_utama():
    print("\n" + "=" * 42)
    print("             KAS DIGITAL")
    print("               XI TKJ 2")
    print("=" * 42)
    print("1. Dashboard Saldo")
    print("2. Data Siswa")
    print("3. Pembayaran Kas")
    print("4. Pengeluaran Kas")
    print("5. Riwayat Transaksi")
    print("6. Laporan Keuangan")
    print("0. Keluar")
    print("=" * 42)

def jalankan():
    buat_tabel()
    while True:
        menu_utama()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            dashboard_saldo()
        elif pilihan == "2":
            menu_siswa()
        elif pilihan == "3":
            menu_pembayaran()
        elif pilihan == "4":
            menu_pengeluaran()
        elif pilihan == "5":
            menu_riwayat()
        elif pilihan == "6":
            laporan_keuangan()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan Kas Digital.")
            break
        else:
            print("Pilihan tidak tersedia.")
        input("\nTekan ENTER untuk kembali...")

if __name__ == "__main__":
    jalankan()
