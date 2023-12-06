# Koşullar
# Koşullar programlamada akış kontrol mekanizması olarak kullanılır
# Bir koşulun oluşması için kullanılan operatörler boolean türünde veri üretmek zorundadır.
# Karşılaştırma ve mantık operatörleri tercih edilmelidir
sayi = -5

sonuc = sayi >= 0
print("Pozitif mi = ", end="")
print(sonuc)

# koşul ile oluşturalım
sonuc = sayi >= 0
if sonuc == True:
    print("Sayı pozitiftir")
else: #sonuç değişkeni içindeki veri true değil ise
    print("Sayı negatiftir")
