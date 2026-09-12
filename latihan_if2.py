nilai = float(input("Masukkan nilai (0-100): "))

if nilai >= 80:
    print("Grade A")
elif nilai >= 70:
    print("Grade B")
elif nilai >=60:
    print("Grade C")
elif nilai >=50:
    print("Grade D")
else:
    print("Grade: E (Tidak Lulus)")