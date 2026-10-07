import tkinter as tk

# Membuat window
window = tk.Tk()
window.title("Login")
window.geometry("400x300")
window.resizable(False, False)

# Judul
judul = tk.Label(
    window,
    text="LOGIN",
    font=("Arial", 24, "bold")
)
judul.pack(pady=30)

# Username
label_username = tk.Label(
     window,
        text="Username",
        font=("Arial", 11)
    if username == "admin" and password == "python123":
        print("LOGIN BERHASIL")
    else:
        print("LOGIN GAGAL")
    
)
   

label_username.pack()

username = tk.Entry(
    window,
    width=30,
    font=("Arial", 11)
    if username == "admin" and password == "python123":
    print("LOGIN BERHASIL")
else:
    print("LOGIN GAGAL")

)
username.pack(pady=5)

# Password
label_password = tk.Label(
    window,
    text="Password",
    font=("Arial", 11)
)
label_password.pack()

password = tk.Entry(
    window,
    width=30,
    show="*",
    font=("Arial", 11)
)
password.pack(pady=5)

# Tombol Login
tombol_login = tk.Button(
    window,
    text="Login",
    width=20
)
tombol_login.pack(pady=20)

# Menjalankan aplikasi
window.mainloop()