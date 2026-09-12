nilai = []


for i in range(1, 6):
    add_data = int(input(f"Masukkan nilai ke-{i}: "))
    nilai.append(add_data)
    

total = 0
for n in nilai:
    total = total + n

print(f"Nilai: {nilai}")
print(f"Total = {total}")
print(f"Rata-rata: {total / len(nilai)}")
print(f"Tertinggi: {max(nilai)}")
print(f"Terendah: {min(nilai)}")

