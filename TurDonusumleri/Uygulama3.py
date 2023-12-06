# Konsoldan Alınan 2 sayının ortalamasını hesaplayınız
print("Lütfen 1. sayıyı giriniz")
sayi1Str = input()

sayi2Str = input("Lütfen 2. sayıyı giriniz ")

sayi1 = int(sayi1Str)
sayi2 = int(sayi2Str)

# 1. yol
# toplam = sayi1 + sayi2
# ortalama = toplam / 2

# 2. yol
ortalama = (sayi1 + sayi2) / 2
# parantez ile işlem önceliği belirtilmelidir.

print("Girdiğiniz sayıların ortalaması = ", end="")
print(ortalama)