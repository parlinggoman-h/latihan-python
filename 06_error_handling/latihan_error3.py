buah = ["apel", "jeruk", "mangga"]

try:
    index = int(input(f"Pilih index (0-{len(buah)-1}): "))
    print(f"Buah pilihan: {buah[index]}")
except ValueError:
    print("Index harus berupa angka!")
except IndexError:
    print(f"Index tidak valid! Pilih antara 0-{len(buah)-1}.")