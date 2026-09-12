def input_nilai(jumlah):
    daftar = []
    for i in range(1, jumlah + 1):
        data = int(input(f"Masukkan nilai ke-{i}: "))
        daftar.append(data)
    return daftar

def hitung_total(nilai):
    return sum(nilai)

def hitung_rata_rata(nilai):
    return hitung_total(nilai) / len(nilai)

def tampilkan_hasil(nilai):
    print(f"Nilai: {nilai}")
    print(f"Total: {hitung_total(nilai)}")
    print(f"Rata-rata: {hitung_rata_rata(nilai)}")
    print(f"Tertinggi: {max(nilai)}")
    print(f"Terendah: {min(nilai)}")

nilai = input_nilai(5)
tampilkan_hasil(nilai)