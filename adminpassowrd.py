import turtle

# Membuat layar
layar = turtle.Screen()
layar.bgcolor("black")


username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin" and password == "python123":
    print("LOGIN BERHASIL")
else:
    print("LOGIN GAGAL")


# Selesai
turtle.done()