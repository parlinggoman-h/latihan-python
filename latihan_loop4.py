angka_rahasia = 42

while True:
    tebak_angka = int(input("Tebak angka (1 - 100): "))

    if tebak_angka > angka_rahasia:
        print("Terlalu besar!")
    elif tebak_angka < angka_rahasia:
        print("Terlalu kecil!")
    else: 
        print("Selamat! Kamu menebak dengan benar!")
        break
    
