def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa bagi dengan 0"
    return a / b


while True:
    print("\n=== Kalkulator ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Pilih (1-5): ")

    if pilihan == "5":
        print("Terimakasih!")
        break

    if pilihan not in ("1", "2", "3", "4"):
        print("Pilihan tidak valid!")
        continue

    try:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
    except ValueError:
        print("Input harus angka! Balik ke menu.")
        continue
        
    if pilihan == "1":
        print(f"Hasil: {tambah(a, b)}")
    elif pilihan == "2":
        print(f"Hasil: {kurang(a, b)}")
    elif pilihan == "3":
        print(f"Hasil: {kali(a, b)}")
    elif pilihan == "4":
        print(f"Hasil: {bagi(a, b)}")
    else:
        print("Error internal: seharusnya tidak sampai di sini!")





    