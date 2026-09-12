kontak = {}

while True:
    nama = (input(f"Nama (atau 'keluar'): "))
    if nama == "keluar":
        break
    else:
        nomor = (input("Masukkan nomor: "))
        kontak[nama] = nomor

print("Daftar Kontak:")
for nama, nomor in kontak.items():
    print(f"{nama}:{nomor}")

