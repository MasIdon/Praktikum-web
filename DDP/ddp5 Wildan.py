kendaraan=["B 25605 DIO", "RX7", "1308cc", "kuning"]
harga=("460jt")
roda=("4 roda")
merk=("Mazda")
jenis=("Mobil")

kendaraan.append(harga)
kendaraan.append(roda)
kendaraan.insert(2, merk)
kendaraan.insert(3, jenis)

print("Kode Kendaraan  :", kendaraan[0])
print("Nama Kendaraan  :", kendaraan[1])
print("Merk Kendaraan  :", kendaraan[2])
print("Jenis Kendaraan :", kendaraan[3])
print("CC Kendaraan    :", kendaraan[4])
print("Warna Kendaraan :", kendaraan[5])
print("Harga Kendaraan :", kendaraan[6])
print("Roda Kendaraan  :", kendaraan[7])
print()

hitung = int(input("""pilih nomer dari pilihan yang tersedia
==============================
1. hitung luas persegi 
2. hitung luas lingkaran 
3. hitung luas segitiga 
==============================
"""))


match hitung:
    case 1:
        print("menghitung luas persegi")
        sisi = int(input("sisi = "))
        LuasPersegi = sisi * sisi
        print("Luas persegi untuk persegi dengan sisi", sisi, "adalah", LuasPersegi)
    case 2:
        print("menghitung luas lingkaran")
        r = int(input("jari jari = "))
        LuasL = 3.14 * r * r
        print("Luas lingkaran untuk lingkaran dengan jari jari", r, "adalah", LuasL)
    case 3:
        print("menghitung luas segitiga")
        alas = int(input("alas = "))
        tinggi = int(input("tinggi = "))
        LuasS = 0.5 * alas * tinggi
        print("Luas segitiga untuk segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", LuasS)
    case _:
        print("eror")    