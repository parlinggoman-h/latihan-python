while True:
    try:
        angka = int(input("Masukkan angka: "))
        print(f"Angka kamu: {angka}")
        break
    except ValueError:
        print("Itu bukan angka, coba lagi!")
        