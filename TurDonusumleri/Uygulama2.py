# Konsoldan 1. sayıyı isteyin
# konsoldan 2. sayıyı isteyin
# Girilen sayıların Toplam, Fark, Çarpım, Bölüm, Mod, Üs Alma, Tam bölüm
# sonuçlarını ayrı ayrı yazdırınız

# Veri alma
print("Lütfen 1. sayıyı giriniz")
sayi1Str = input()
print("Lütfen 2. sayıyı giriniz")
sayi2Str = input()
# tür dönüşümü
sayi1 = int(sayi1Str)
sayi2 = int(sayi2Str)

# hesaplama
toplam = sayi1 + sayi2
print("Toplam = " + str(toplam))
fark = sayi1 - sayi2
print("Fark = ", end="")
print(fark)
carpim = sayi1 * sayi2
print("Çarpım = " + str(carpim))
bolum = sayi1 / sayi2
print("Bölüm = " + str(bolum))
mod = sayi1 % sayi2
print("Mod = " + str(mod))
us = sayi1 ** sayi2
print(str(sayi1) + "'in " + str(sayi2) + ". kuvveti = " + str(us))
tambolum = sayi1//sayi2
print("Tam Bölüm = " + str(tambolum))
