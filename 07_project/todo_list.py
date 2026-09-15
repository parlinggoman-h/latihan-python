"""
Aplikasi To-Do List Sederhana
Dibuat oleh: Parlinggoman Hutauruk
Deskripsi: Aplikasi CLI untuk mengelola daftar tugas
"""


def tampilkan_menu():
    """Menampilkan menu utama aplikasi to-do list"""
    print("\n=== TO-DO LIST ===")
    print("1. Lihat semua tugas")
    print("2. Tambah tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Keluar")

def lihat_tugas(tugas):
    """Menampilkan semua tugas dalam list"""
    # Guard clause: kalau list kosong, keluar lebih awal
    if not tugas:
        print("Belum ada tugas.") # Kalau list kosong, print "Belum ada tugas."
        return
    else:
        print("\n=== DAFTAR TUGAS ===")
        #enumerate(start=1) → nomor mulai dari 1, bukan 0
        for i, item in enumerate(tugas, start=1):
            # Ternary operator: pilih status berdasarkan nilai 'selesai'
            status = "[SELESAI]" if item["selesai"] else "[BELUM]"
            print(f"{i}. [{status}] {item['judul']}")
    

def tambah_tugas(tugas):
    """Minta input judul, tambahkan list"""
    # .strip() → hapus spasi di awal/akhir input
    judul = input("Masukkan judul: ").strip()

    # Guard clause: kalau input kosong, keluar lebih awal
    if not judul:
        print("Error: Judul tidak boleh kosong")
        return

    # Tambahkan tugas baru ke list sebagai dictionary
    tugas.append({"judul": judul, "selesai": False})
    print(f"Tugas '{judul}' berhasil ditambahkan!")

def tandai_selesai(tugas):
    """Menandai tugas sebagai selesai"""
    # Guard clause: kalau list kosong, keluar lebih awal
    if not tugas:
        print("Belum ada tugas.")
        return

    # Tampilkan daftar dulu supaya user tahu nomor tugas
    lihat_tugas(tugas)

    try:
        nomor = int(input("\nPilih nomor tugas: "))

        # Validasi range nomor
        if nomor < 1 or nomor > len(tugas):
            print(f"Nomor tidak valid! Pilih antara 1-{len(tugas)},")
            return

        # Simpan judul dulu untuk konfirmasi
        judul = tugas[nomor - 1]["judul"]

        # Update status tugas (index mulai 0, nomor mulai 1)
        tugas[nomor - 1]["selesai"] = True
        print(f"Tugas '{judul}' ditandai selesai!")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_tugas(tugas):
    """Menghapus tugas dari list"""
    # Guard clause: kalau list kosong, keluar lebih awal
    if not tugas:
        print("Belum ada tugas.")
        return

    lihat_tugas(tugas)

    try:
        nomor = int(input("\nPilih nomor tugas: "))
        if nomor < 1 or nomor > len(tugas):
            print(f"Nomor tidak valid! Pilih antara 1 - {len(tugas)}.")
            return

        # Simpan judul dulu untuk konfirmasi
        judul = tugas[nomor - 1]["judul"]

        # Hapus dari list berdasarkan index
        tugas.pop(nomor - 1)
        print(f"Tugas '{judul}' berhasil dihapus!")
    except ValueError:
        print("Input harus berupa angka!")

    

def main():
    """Program utama to-do list"""
    # list kosong untuk menyimpan tugas
    tugas = []

    # Loop utama program
    while True:
        tampilkan_menu()
        pilihan = input("Pilih (1-5): ")

        if pilihan == "5":
            print("Terimakasih! Sampai jumpa.")
            break
        elif pilihan == "1":
            lihat_tugas(tugas)
        elif pilihan == "2":
            tambah_tugas(tugas)
        elif pilihan == "3":
            tandai_selesai(tugas)
        elif pilihan == "4":
            hapus_tugas(tugas)
        else:
            print("Pilihan tidak valid!")

# Jalankan program
main()