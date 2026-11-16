
# ==========================================
# APLIKASI KAS DIGITAL
# ABSEN 12
# KELAS XI TKJ 2
# ==========================================

from datetime import datetime


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
# DATA TRANSAKSI
# ==========================================

data_pembayaran = []
data_pengeluaran = []


# ==========================================
# FUNGSI BANTUAN
# ==========================================

def garis():
    print("=" * 45)


def format_rupiah(angka):
    return "Rp" + format(angka, ",").replace(",", ".")


def total_pembayaran():
    return sum(
        transaksi["nominal"]
        for transaksi in data_pembayaran
    )


def total_pengeluaran():
    return sum(
        transaksi["nominal"]
        for transaksi in data_pengeluaran
    )


def hitung_saldo():
    return total_pembayaran() - total_pengeluaran()


# ==========================================
# MENU UTAMA
# ==========================================

def menu_utama():
    garis()
    print("          KAS DIGITAL")
    print("             XI TKJ 2")
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
# DASHBOARD SALDO
# ==========================================

def dashboard_saldo():
    garis()
    print("         DASHBOARD SALDO")
    garis()

    print("Total Uang Masuk :",
          format_rupiah(total_pembayaran()))

    print("Total Pengeluaran:",
          format_rupiah(total_pengeluaran()))

    print("Saldo Kas        :",
          format_rupiah(hitung_saldo()))

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
# TAMBAH SISWA
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
# LIHAT SISWA
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
# HAPUS SISWA
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

                for i, item in enumerate(data_siswa):
                    item["nomor"] = i + 1

                print("Data berhasil dihapus!")
                return

        print("Nomor siswa tidak ditemukan!")

    except ValueError:
        print("Masukkan nomor berupa angka!")


# ==========================================
# MENU PEMBAYARAN KAS
# ==========================================

def menu_pembayaran():
    while True:
        garis()
        print("        PEMBAYARAN KAS")
        garis()
        print("1. Tambah Pembayaran")
        print("2. Riwayat Pembayaran")
        print("3. Total Uang Masuk")
        print("0. Kembali")
        garis()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pembayaran()

        elif pilihan == "2":
            riwayat_pembayaran()

        elif pilihan == "3":
            tampilkan_total()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia!")

        input("\nTekan ENTER untuk lanjut...")


# ==========================================
# TAMBAH PEMBAYARAN
# ==========================================

def tambah_pembayaran():
    garis()
    print("TAMBAH PEMBAYARAN KAS")
    garis()

    if len(data_siswa) == 0:
        print("Belum ada data siswa!")
        return

    lihat_siswa()

    try:
        nomor = int(input("\nPilih nomor siswa: "))

        siswa_dipilih = None

        for siswa in data_siswa:
            if siswa["nomor"] == nomor:
                siswa_dipilih = siswa
                break

        if siswa_dipilih is None:
            print("Nomor siswa tidak ditemukan!")
            return

        print("Nama siswa:", siswa_dipilih["nama"])

        nominal = int(input("Nominal pembayaran: Rp"))

        if nominal <= 0:
            print("Nominal harus lebih dari 0!")
            return

        tanggal = input("Tanggal (DD-MM-YYYY): ")

        datetime.strptime(tanggal, "%d-%m-%Y")

        data_pembayaran.append({
            "nomor": len(data_pembayaran) + 1,
            "nama": siswa_dipilih["nama"],
            "nominal": nominal,
            "tanggal": tanggal
        })

        print("\nPembayaran berhasil dicatat!")

    except ValueError:
        print("Input angka atau tanggal tidak valid!")


# ==========================================
# RIWAYAT PEMBAYARAN
# ==========================================

def riwayat_pembayaran():
    garis()
    print("RIWAYAT PEMBAYARAN")
    garis()

    if len(data_pembayaran) == 0:
        print("Belum ada pembayaran.")
        return

    for transaksi in data_pembayaran:
        print("Nomor   :", transaksi["nomor"])
        print("Nama    :", transaksi["nama"])
        print("Nominal :", format_rupiah(transaksi["nominal"]))
        print("Tanggal :", transaksi["tanggal"])
        garis()

    print("Total:", format_rupiah(total_pembayaran()))


def tampilkan_total():
    garis()
    print("TOTAL UANG KAS MASUK")
    garis()
    print("Jumlah transaksi:", len(data_pembayaran))
    print("Total pembayaran:", format_rupiah(total_pembayaran()))
    garis()


# ==========================================
# MENU PENGELUARAN KAS
# ==========================================

def menu_pengeluaran():
    while True:
        garis()
        print("        PENGELUARAN KAS")
        garis()
        print("1. Tambah Pengeluaran")
        print("2. Riwayat Pengeluaran")
        print("3. Total Pengeluaran")
        print("0. Kembali")
        garis()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pengeluaran()

        elif pilihan == "2":
            riwayat_pengeluaran()

        elif pilihan == "3":
            tampilkan_pengeluaran()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia!")

        input("\nTekan ENTER untuk lanjut...")


# ==========================================
# TAMBAH PENGELUARAN
# ==========================================

def tambah_pengeluaran():
    garis()
    print("TAMBAH PENGELUARAN KAS")
    garis()

    print("Saldo tersedia:", format_rupiah(hitung_saldo()))

    keterangan = input(
        "Keterangan pengeluaran: "
    ).strip()

    if keterangan == "":
        print("Keterangan tidak boleh kosong!")
        return

    try:
        nominal = int(input("Nominal pengeluaran: Rp"))

        if nominal <= 0:
            print("Nominal harus lebih dari 0!")
            return

        if nominal > hitung_saldo():
            print("Saldo kas tidak mencukupi!")
            return

        tanggal = input("Tanggal (DD-MM-YYYY): ")

        datetime.strptime(tanggal, "%d-%m-%Y")

        data_pengeluaran.append({
            "nomor": len(data_pengeluaran) + 1,
            "keterangan": keterangan,
            "nominal": nominal,
            "tanggal": tanggal
        })

        print("\nPengeluaran berhasil dicatat!")
        print("Keterangan:", keterangan)
        print("Nominal:", format_rupiah(nominal))
        print("Sisa saldo:", format_rupiah(hitung_saldo()))

    except ValueError:
        print("Input angka atau tanggal tidak valid!")


# ==========================================
# RIWAYAT PENGELUARAN
# ==========================================

def riwayat_pengeluaran():
    garis()
    print("RIWAYAT PENGELUARAN")
    garis()

    if len(data_pengeluaran) == 0:
        print("Belum ada pengeluaran.")
        return

    for transaksi in data_pengeluaran:
        print("Nomor      :", transaksi["nomor"])
        print("Keterangan :", transaksi["keterangan"])
        print("Nominal    :", format_rupiah(transaksi["nominal"]))
        print("Tanggal    :", transaksi["tanggal"])
        garis()

    print("Total pengeluaran:",
          format_rupiah(total_pengeluaran()))


# ==========================================
# TOTAL PENGELUARAN
# ==========================================

def tampilkan_pengeluaran():
    garis()
    print("TOTAL PENGELUARAN KAS")
    garis()

    print("Jumlah transaksi:", len(data_pengeluaran))
    print("Total pengeluaran:",
          format_rupiah(total_pengeluaran()))

    garis()


# ==========================================
# RIWAYAT TRANSAKSI
# ==========================================

def menu_riwayat():
    garis()
    print("       RIWAYAT TRANSAKSI")
    garis()

    if not data_pembayaran and not data_pengeluaran:
        print("Belum ada transaksi.")
        return

    semua_transaksi = []

    for transaksi in data_pembayaran:
        semua_transaksi.append({
            "jenis": "PEMASUKAN",
            "keterangan": transaksi["nama"],
            "nominal": transaksi["nominal"],
            "tanggal": transaksi["tanggal"]
        })

    for transaksi in data_pengeluaran:
        semua_transaksi.append({
            "jenis": "PENGELUARAN",
            "keterangan": transaksi["keterangan"],
            "nominal": transaksi["nominal"],
            "tanggal": transaksi["tanggal"]
        })

    for transaksi in semua_transaksi:
        print("Jenis      :", transaksi["jenis"])
        print("Keterangan :", transaksi["keterangan"])
        print("Nominal    :", format_rupiah(transaksi["nominal"]))
        print("Tanggal    :", transaksi["tanggal"])
        garis()


# ==========================================
# LAPORAN KEUANGAN
# ==========================================

def laporan_keuangan():
    garis()
    print("        LAPORAN KEUANGAN")
    garis()

    print("Jumlah Siswa     :", len(data_siswa))
    print("Jumlah Pembayaran:", len(data_pembayaran))
    print("Jumlah Pengeluaran:", len(data_pengeluaran))

    print("Uang Masuk       :",
          format_rupiah(total_pembayaran()))

    print("Uang Keluar      :",
          format_rupiah(total_pengeluaran()))

    print("Saldo Akhir      :",
          format_rupiah(hitung_saldo()))

    garis()


# ==========================================
# PROGRAM UTAMA
# ==========================================

while True:

    menu_utama()

    pilihan = input("Pilih menu: ")

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
        print("Terima kasih!")
        print("Program Kas Digital selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")

    input("\nTekan ENTER untuk kembali...")
