import json
import os

SALDO_FILE = "saldo.json"

# coba muat saldo dari file saat program dimulai
def load_saldo():
    if os.path.exists(SALDO_FILE):
        try:
            with open(SALDO_FILE, "r") as f:
                data = json.load(f)
                return data.get("saldo", 0)
        except Exception:
            return 0
    return 0

saldo = load_saldo()

def simpan_saldo():
    try:
        with open(SALDO_FILE, "w") as f:
            json.dump({"saldo": saldo}, f)
    except Exception as e:
        print("Gagal menyimpan saldo:", e)

def tambah_pemasukan():
    global saldo
    try:
        jumlah_str = input("Masukkan jumlah pemasukan: ")
        jumlah = float(jumlah_str)
        if jumlah <= 0:
            print("Masukkan angka positif.")
            return
        saldo += jumlah
        simpan_saldo()
        print(f"Pemasukan sebesar {jumlah:.2f} berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah_str = input("Masukkan jumlah pengeluaran: ")
        jumlah = float(jumlah_str)
        if jumlah <= 0:
            print("Masukkan angka positif.")
            return
        if jumlah > saldo:
            print("Saldo tidak cukup.")
            return
        saldo -= jumlah
        simpan_saldo()
        print(f"Pengeluaran sebesar {jumlah:.2f} berhasil dikurangi.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def lihat_saldo():
    print("=== Saldo Saat Ini ===")
    print("Rp {0:,.2f}".format(saldo))

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")