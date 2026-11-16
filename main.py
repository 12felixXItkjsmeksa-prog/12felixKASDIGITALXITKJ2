
# ==========================================
# APLIKASI KAS DIGITAL
# ABSEN 12
# KELAS XI TKJ 2
# ==========================================


# ==========================================
# DATA SISWA
# ==========================================

nama_siswa = [
    "Adifian Hafeez Noufal Maulana",
    "Aldrich Frederica Purnama Putra",
    "Alvin Fiqih Pangestu",
    "Arya Wirananta",
    "Aura Nissrina Aliya Ziskind",
    "Chelvin Ayub Syah Putra",
    "Debby Queena Putri Htun",
    "Desta Aulya Hela Abdila",
    "Fahima Izzul Fikri",
    "Fardan Cahyo Sugiarto",
    "Fareel Andhika Pratama",
    "Felix Reviano Pratama Putra",
    "Gio Putra Fajar Antonio",
    "Handy Dio Ferdinand",
    "Hilwa Azwa Amaliyah",
    "Hobart Fazailya Musthofa",
    "Javier Zufar Byakta",
    "Keysa Gresilda Syafabila",
    "M. Daffa Adliansyah",
    "Moch. Zaidan Helmi Fataska",
    "Moh. Zainal Arifin Mustopa",
    "Muhamad Rafif Alvis Maulana Putra",
    "Muhammad Baihaqi Kayzan",
    "Muhammad Gilang Rahmana",
    "Muhammad Rizqi Al-Rayyan Irawan",
    "Nur'aini Libna Zulfahmi",
    "Oscar Yeremia",
    "Purwadika Surya Albasit",
    "Ranjib Toyib Aljabar",
    "Salsabila Syifa Az-Zahra",
    "Sukma Dwi Nur Indasah",
    "Syahmi Ezhar Febriano",
    "Tangguh Darwisy Muhammad",
    "Vano Dwiki Ardelon",
    "Virly Aprilia Wardani",
    "Zazkia Arum Zalina",
    "Zilbian Dianorhas"
]

data_siswa = []

for i, nama in enumerate(nama_siswa):
    data_siswa.append({
        "nomor": i + 1,
        "nama": nama
    })


# ==========================================
# FUNGSI GARIS
# ==========================================

def garis():
    print("=" * 40)


# ==========================================
# MENU UTAMA
# ==========================================

def menu_utama():
    garis()
    print("          KAS DIGITAL")
    garis()
    print("1. Dashboard Saldo")
    print("2. Data Siswa")
    print("3. Pembayaran Kas")
    print("4. Pengeluaran Kas")
    print("5. Riwayat Transaksi")
    print("6. Laporan Keuangan")
    print("0. Keluar")
    garis()


# ==========================================
# MENU DATA SISWA
# ==========================================

def menu_siswa():
    while True:
        garis()
        print("          DATA SISWA")
        garis()
        print("1. Tambah Siswa")
        print("2. Lihat Data Siswa")
        print("3. Hapus Siswa")
        print("0. Kembali")
        garis()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_siswa()

        elif pilihan == "2":
            lihat_siswa()

        elif pilihan == "3":
            hapus_siswa()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia!")

        input("\nTekan ENTER untuk lanjut...")


# ==========================================
# MENAMBAH SISWA
# ==========================================

def tambah_siswa():
    garis()
    print("TAMBAH DATA SISWA")
    garis()

    nama = input("Masukkan nama siswa: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong!")
        return

    siswa = {
        "nomor": len(data_siswa) + 1,
        "nama": nama
    }

    data_siswa.append(siswa)

    print("Data siswa berhasil ditambahkan!")


# ==========================================
# MELIHAT DATA SISWA
# ==========================================

def lihat_siswa():
    garis()
    print("DAFTAR SISWA")
    garis()

    if len(data_siswa) == 0:
        print("Belum ada data siswa.")
        return

    for siswa in data_siswa:
        print(
            str(siswa["nomor"]) + ". " +
            siswa["nama"]
        )

    garis()
    print("Jumlah siswa:", len(data_siswa))


# ==========================================
# MENGHAPUS SISWA
# ==========================================

def hapus_siswa():
    lihat_siswa()

    if len(data_siswa) == 0:
        return

    try:
        nomor = int(input("Masukkan nomor siswa: "))

        for siswa in data_siswa:
            if siswa["nomor"] == nomor:
                data_siswa.remove(siswa)

                # Atur ulang nomor siswa
                for i, item in enumerate(data_siswa):
                    item["nomor"] = i + 1

                print("Data berhasil dihapus!")
                return

        print("Nomor siswa tidak ditemukan!")

    except ValueError:
        print("Masukkan nomor berupa angka!")


# ==========================================
# PROGRAM UTAMA
# ==========================================

while True:
    menu_utama()

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Dashboard Saldo")

    elif pilihan == "2":
        menu_siswa()

    elif pilihan == "3":
        print("Pembayaran Kas")

    elif pilihan == "4":
        print("Pengeluaran Kas")

    elif pilihan == "5":
        print("Riwayat Transaksi")

    elif pilihan == "6":
        print("Laporan Keuangan")

    elif pilihan == "0":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia!")

    input("\nTekan ENTER untuk kembali...")
