# Konsoldan alınan 2 sınav ve 1 sözlü notunun ortalamasını hesaplayınız
# Ortalama 50 üstü ise geçtiniz Değilse Kaldınız yazdırınız
not1 = int(input("Lütfen 1. sınav notunuzu giriniz = "))
not2 = int(input("Lütfen 2. sınav notunuzu giriniz = "))
sozlu = int(input("Lütfen sözlü notunuzu giriniz = "))
ortalama = (not1 + not2 + sozlu) / 3
print("Ortalamanız = " + str(ortalama))
if ortalama >= 50:
    print("Geçtiniz")
else:
    print("Kaldınız")
