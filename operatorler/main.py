# Python Operatörler
# Diğer tüm programlama dillerinde olduğu gibi
# Python programlama dilinde de operatörler, değişkenler ve
# değerler üzerinde işlem gerçekleştirmek için kullanılır

# 1 Aritmetiksel Operatörler
# Sayılar üzerinde matematiksel işlemler yapılırken kullanılır.
# + Toplama
# - Çıkarma
# * Çarpma
# % Mod Alma(Bölümünden kalan)
# ** Üs alma(sayının kuvveti)
# // Tam bölüm
# int
sayi1 = 11
# int
sayi2 = 3
# int
toplam = sayi1 + sayi2
print("Toplam =", end="")
print(toplam)
# toplam değişkeni tanımlandıktan sonra sayi1 değişkeninin
# içindeki veri ile sayi2 değişkeninin içindeki veriyi
# + operatörü ile toplayıp toplam değişkeninin içerisine attık
fark = sayi1 - sayi2
print("Fark = ", end="")
print(fark)
carpim = sayi1 * sayi2
print("Çarpım = ", end="")
print(carpim)
bolum = sayi1 / sayi2
print("Bölüm = ", end="")
print(bolum)
mod = sayi1 % sayi2
print("Mod = ", end="")
print(mod)
us = sayi1 ** sayi2
print("Üs Alma = ", end="")
print(us)
tambolum = sayi1 // sayi2
print("Tam Bölüm = ", end="")
print(tambolum)

# 2 Atama Operatörleri
# =     Atama Operatörü
# +=    Toplayarak ata
# -=    Çıkartarak ata
# *=    Çarparak ata
# /=    Bölerek ata
# %=    Modalarak ata
# **=   Üs Alarak ata
# //=   Tam Bölerek ata
sayi3 = 10
# 10 verisini sayi3 isimli değişkene ata
sayi3 += 2
print(sayi3)
sayi3 -= 2
print(sayi3)
sayi3 *= 2
print(sayi3)
sayi3 /= 2
print(sayi3)

# 3 Karşılaştırma Operatörleri
# karşılaştırma operatörleri boolean veri üretirler
# == eşit mi
# != eşit değil mi(eşit değilse true verir)
# > Büyük mü
# < Küçük mü
# >= Büyük eşit mi
# <= Küçük eşit mi
sayi4 = 10
sayi5 = 8
# sayi4 == sayi5 Sayı4 değişkeninin içindeki veri sayi5 değişkeninin içindeki veriye eşit mi
sonuc = sayi4 == sayi5
print("Eşit mi = ", end="")
print(sonuc)
sonuc = sayi4 != sayi5
print("Eşit değil mi = ", end="")
print(sonuc)
sonuc = sayi4 > sayi5
print("Büyük mü = ", end="")
print(sonuc)
sonuc = sayi4 < sayi5
print("Eşit mi = ", end="")
print(sonuc)
sonuc = sayi4 >= sayi5
print("Büyük eşit mi = ", end="")
print(sonuc)
sonuc = sayi4 <= sayi5
print("Küçük eşit mi = ", end="")
print(sonuc)
