#halo word
print("halo")
print("aku bosen")

#input
nama = "hana"
usia = "21"

print(nama)
print(usia)

nama = input("namanya siapa?")

print("helo,", nama)

#pertambahan sederhana
angka1 = float(input("masukin angka pertama: "))
angka2 = float(input("masukin angka kedua "))

hasil = angka1 + angka2

#perkurangan sederhana 
print("hasil:", hasil)

angka1 = float(input("masukin angka pertama: "))
angka2 = float(input("masukin angka kedua "))

hasil = angka1 - angka2

print("hasil:", hasil)

#if
usia = int(input("usia kamu berapa? "))

if usia >= 20:
    print("sudah cukup umur")
else:
    print("belum cukup umur")

#pengulangan atau for
for i in range (1,2):
    print("angka", i)