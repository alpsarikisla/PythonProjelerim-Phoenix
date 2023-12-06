# Konsoldan alınan 2 sınav ve 1 sözlü notunun ortalamasını hesaplayınız
# Ortalama 50 üstü ise geçtiniz Değilse Kaldınız yazdırınız
print("Lütfen 1. sınav notunuzu giriniz")
not1Str = input()
not1 = int(not1Str)

print("Lütfen 2. sınav notunuzu giriniz")
not2Str = input()
not2 = int(not2Str)

print("Lütfen sözlü notunuzu giriniz")
sozluStr = input()
sozlu = int(sozluStr)

toplam = not1 + not2 + sozlu
ortalama = toplam / 3

print("Ortalamanız = " + str(ortalama))

if ortalama >= 50:
    print("Tebrikler. Geçtiniz")
else:
    print("Üzgünüm. Kaldınız")