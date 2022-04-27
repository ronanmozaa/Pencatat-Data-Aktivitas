import csv
import datetime

nama_file = "data.csv"

def kembali():
    print("")
    input("tekan enter untuk kembali..")
    menu_aplikasi()

def baca_data():
    data_aktivitas = []
    print("NO\tWAKTU\t\tAKTIVITAS")
    with open(nama_file, "r") as filecsv:
        baca = csv.DictReader(filecsv, delimiter=",")
        for baris in baca:
            print(f"{baris['NO']}    {baris['WAKTU']}    {baris['AKTIVITAS']}")
    kembali()

def tambah_data():
    with open(nama_file, "a", newline="") as filecsv:
        tambah = csv.writer(filecsv, delimiter=",")
        NO = int(input("Masukkan no indeks : "))
        WAKTU = datetime.datetime.now().strftime("%c")
        AKTIVITAS = input("Nama Aktivitas: ")
        tambah.writerow([NO, WAKTU, AKTIVITAS])
    print("___________________________________")
    print("Data aktivitas berhasil ditambahkan")
    kembali()

def hapusData():
    data_aktivitas = []
    with open(nama_file, mode="r") as filecsv:
        csv_reader = csv.DictReader(filecsv)
        for baris in csv_reader:
            data_aktivitas.append(baris)
            print(f"{baris['NO']} {baris['WAKTU']} {baris['AKTIVITAS']}")


    no = input("\nPilih nomor yang ingin dihapus: ")

    indeks = 0
    for data in data_aktivitas:
        if (data['NO'] == no):
            data_aktivitas.remove(data_aktivitas[indeks])
        indeks = indeks + 1

    with open(nama_file, mode="w", newline="") as filecsv:
        header = ['NO', 'WAKTU', 'AKTIVITAS']
        writer = csv.DictWriter(filecsv, fieldnames=header)
        writer.writeheader()
        for dataBaru in data_aktivitas:
            writer.writerow({'NO': dataBaru['NO'], 'WAKTU': dataBaru['WAKTU'], 'AKTIVITAS': dataBaru['AKTIVITAS']}) 
       
    print("data berhasil dihapus")
    kembali()

def editData():
    data_aktivitas = []
    with open(nama_file, mode="r") as filecsv:
        csv_reader = csv.DictReader(filecsv)
        for baris in csv_reader:
            data_aktivitas.append(baris)
            print(f"{baris['NO']} {baris['WAKTU']} {baris['AKTIVITAS']}")

    no = input("\nPilih nomor yang ingin dirubah: ")
    waktu = datetime.datetime.now().strftime("%c")
    aktivitas = input("Nama aktivitas baru: ")

    indeks = 0
    for data in data_aktivitas:
        if (data['NO'] == no):
            data_aktivitas[indeks]['WAKTU'] = waktu
            data_aktivitas[indeks]['AKTIVITAS'] = aktivitas
        indeks = indeks + 1

    with open(nama_file, mode="w", newline="") as filecsv:
        header = ['NO', 'WAKTU', 'AKTIVITAS']
        writer = csv.DictWriter(filecsv, fieldnames=header)
        writer.writeheader()
        for dataBaru in data_aktivitas:
            writer.writerow({'NO': dataBaru['NO'], 'WAKTU': dataBaru['WAKTU'], 'AKTIVITAS': dataBaru['AKTIVITAS']})     
    kembali()

def menu_aplikasi():
    print("""
    -------------------------------------
    MENU APLIKASI PENCATAT DATA AKTIVITAS
    -------------------------------------
    [1] Baca Data Aktivitas
    [2] Tambah Data Aktivitas
    [3] Hapus Data Aktivitas
    [4] Edit Data Aktivitas
    [0] Keluar
    """)
    pilihan_menu = int(input("Masukkan pilihan menu : "))

    if pilihan_menu == 1:
        baca_data()
    elif pilihan_menu == 2:
        tambah_data()
    elif pilihan_menu == 3:
        hapusData()
    elif pilihan_menu == 4:
        editData()
    elif pilihan_menu == 0:
        print("terima kasih telah menggunakan aplikasi kami ^^")
        exit()
    else:
        print("Pilihan anda tidak terdapat dalam menu!")
        kembali()

if __name__ == "__main__":
    menu_aplikasi()