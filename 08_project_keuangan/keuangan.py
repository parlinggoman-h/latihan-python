"""
Aplikasi Keuangan Sederhana
Dibuat oleh: Parlinggoman Hutauruk
Deskripsi: Aplikasi CLI untuk mencatat pemasukan dan pengeluaran
"""


def tampilkan_menu():
    """Menampilkan menu utama aplikasi keuangan"""
    print("\n=== APLIKASI KEUANGAN ===")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Semua Transaksi")
    print("4. Lihat Ringkasan")
    print("5. Hapus Transaksi")
    print("6. Keluar")


def format_rupiah(angka):
    """Format angka jadi 'Rp 5.000.000'"""
    return f"Rp {angka:,.0f}".replace(",", ".")


def tambah_transaksi(transaksi, jenis):
    """Minta input, tambah transaksi ke list"""
    from datetime import date

    print(f"\n=== TAMBAH {jenis.upper()} ===")

    # Tanggal (default: hari ini)
    hari_ini = date.today().isoformat()
    tanggal = input(f"Tanggal (YYYY-MM-DD) [{hari_ini}]: ").strip()
    if not tanggal:
        tanggal = hari_ini

    # Kategori
    kategori = input("Kategori: ").strip()
    if not kategori:
        print("Error: Kategori tidak boleh kosong")
        return

    # Jumlah
    try:
        jumlah = float(input("Jumlah: "))
        if jumlah <= 0:
            print("Error: Jumlah harus lebih dari 0!")
            return
    except ValueError:
        print("Error: Jumlah harus berupa angka!")
        return

    # Keterangan (opsional)
    keterangan = input("Keterangan (opsional): ").strip()
    if not keterangan:
        keterangan = "-"

    # Tambah ke list
    transaksi.append({
        "tanggal": tanggal,
        "jenis": jenis,
        "kategori": kategori,
        "jumlah": jumlah,
        "keterangan": keterangan
    })


    print(f"✅ {jenis.capitalize()} '{kategori}' sebesar {format_rupiah(jumlah)} berhasil ditambahkan!")


def lihat_transaksi(transaksi):
    """Menampilkan semua transaksi"""
    if not transaksi:
        print("Belum ada transaksi.")
        return

    print("\n=== SEMUA TRANSAKSI ===")
    print(f"{'No':<3} {'Tanggal':<12} {'jenis':<12} {'Kategori':<12} {'Jumlah':<15} {'Keterangan'}")
    print("-" * 80)

    for i, t in enumerate(transaksi, start=1):
        print(f"{i:<3} {t['tanggal']:<12} {t['jenis']:<12} {t['kategori']:<12} {format_rupiah(t['jumlah']):<15} {t['keterangan']}")


def lihat_ringkasan(transaksi):
    """Menampilkan total pemasukan, pengeluaran, dan saldo"""
    if not transaksi:
        print("Belum ada transaksi.")
        return
    
    total_pemasukan = sum(t["jumlah"] for t in transaksi if t["jenis"] == "pemasukan")
    total_pengeluaran = sum(t["jumlah"] for t in transaksi if t["jenis"] == "pengeluaran")
    saldo = total_pemasukan - total_pengeluaran

    print("\n=== RINGKASAN KEUANGAN ===")
    print(f"Total Pemasukan: {format_rupiah(total_pemasukan)}")
    print(f"Total Pengeluaran: {format_rupiah(total_pengeluaran)}")
    print("-" * 30)
    print(f"Saldo: {format_rupiah(saldo)}")


def hapus_transaksi(transaksi):
    """Hapus transaksi dari list"""
    # Guard clause: kalau list kosong, keluar lebih awal
    if not transaksi:
        print("Belum ada transaksi.")
        return

    # Tampilkan daftar dulu supaya user tahu nomor
    lihat_transaksi(transaksi)

    try:
        nomor = int(input("\nPilih nomor transaksi yang mau dihapus: "))

        # Validasi range nomor
        if nomor < 1 or nomor > len(transaksi):
            print(f"Nomor tidak valid! Pilih antara 1-{len(transaksi)}.")
            return

        # Simpan info untuk konfirmasi
        kategori = transaksi[nomor - 1]["kategori"]
        jumlah = transaksi[nomor - 1]["jumlah"]

        # Hapus dari list
        transaksi.pop(nomor - 1)
        print(f"✅ Transaksi '{kategori}' sebesar {format_rupiah(jumlah)} berhasil dihapus!")
    except ValueError:
        print("Error: Input harus berupa angka!")


def main():
    """Program utama aplikasi keuangan"""
    transaksi = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih (1-6): ")

        if pilihan == "6":
            print("Terima kasih! Sampai jumpa.")
            break
        elif pilihan == "1":
            tambah_transaksi(transaksi, "pemasukan")
        elif pilihan == "2":
            tambah_transaksi(transaksi, "pengeluaran")
        elif pilihan == "3":
            lihat_transaksi(transaksi)
        elif pilihan == "4":
            lihat_ringkasan(transaksi)
        elif pilihan == "5":
            hapus_transaksi(transaksi)
        else:
            print("Pilihan tidak valid!")


# Jalankan program
main()
