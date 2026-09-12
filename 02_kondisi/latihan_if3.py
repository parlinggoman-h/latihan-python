user = "admin"
password = "12345"

user_name = input("Masukkan username: ")
user_password = input("Masukkan password: ")
if user_name == user and user_password == password:
    print(f"Login berhasil! Selamat datang, {user_name}")
elif user_name == user and user_password != password:
    print("Password salah!")
elif user_name != user:
    print("Username tidak ditemukan!")
else:
    print("Terjadi kesalahan!")