# Konsoldan isim, soyisim ve doğum yılı alınız
# yaşı hesaplatınız
# eğer yaş 12'den büyük ise "sayın isim soyisim yaş değeri uygundur" yazdırınız
# değil ise "sayın isim soyisim yaş değeri uygun değildir" yazdırınız
print("Lütfen isminizi giriniz")
isim = input()

print("Lütfen soyisminizi giriniz")
soyisim = input()

print("Lütfen doğum yılınızı giriniz")
dogumyilStr = input()
dogumyil = int(dogumyilStr)

yas = 2023 - dogumyil
print("Sayın " + isim + " " + soyisim + " Yaşınız = " + str(yas))

if yas >= 12:
    print("Yaş değeri uygundur")
else:
    print("Yaş değeri uygun değildir")
