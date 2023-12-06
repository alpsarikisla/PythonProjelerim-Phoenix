# Konsoldan alınan 2 sınav notunun ortalaması 50 üstü ise geçtiniz
# değilse kaldınız yazılacak
print("Lütfen 1. sınav notunuzu giriniz")
not1Str = input()
not1 = int(not1Str)

not2Str = input("Lütfen 2. sınav notunuzu giriniz")
not2 = int(not2Str)

toplam = not1 + not2
ortalama = toplam / 2
print("Ortalamanız = " + str(ortalama))

if ortalama >= 50:
    print("Geçtiniz")
else:
    print("Kaldınız")
