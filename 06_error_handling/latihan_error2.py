try:
    a = float(input("Angka pertama: "))
    b = float(input("Angka kedua: "))
    hasil = a / b
    print(f"Hasil: {hasil}")
except ValueError:
    print("Input harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa bagi dengan 0")