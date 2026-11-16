
# ==========================================
# PROYEK AKHIR PYTHON
# APLIKASI KAS DIGITAL
# ABSEN 12
# ==========================================

def garis():
    print("=" * 40)


def menu_utama():
    garis()
    print("          KAS DIGITAL")
    print("       KEUANGAN KAS KELAS")
    garis()

    print("1. Dashboard Saldo")
    print("2. Data Siswa")
    print("3. Pembayaran Kas")
    print("4. Pengeluaran Kas")
    print("5. Riwayat Transaksi")
    print("6. Laporan Keuangan")
    print("0. Keluar")

    garis()


# PROGRAM UTAMA
while True:

    menu_utama()

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Dashboard Saldo")

    elif pilihan == "2":
        print("Data Siswa")

    elif pilihan == "3":
        print("Pembayaran Kas")

    elif pilihan == "4":
        print("Pengeluaran Kas")

    elif pilihan == "5":
        print("Riwayat Transaksi")

    elif pilihan == "6":
        print("Laporan Keuangan")

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")

    input("Tekan ENTER untuk kembali...")
