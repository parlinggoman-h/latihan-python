def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return f"{angka} adalah bilangan GENAP"
    else:
        return f"{angka} adalah bilangan GANJIL"

print(cek_ganjil_genap(8))
print(cek_ganjil_genap(7))
print(cek_ganjil_genap(0))
