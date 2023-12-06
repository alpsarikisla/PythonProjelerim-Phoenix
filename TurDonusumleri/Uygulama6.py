# Konsoldan alınan 3 sayının ortalaması çift mi?
# Çift ise true değilse false yazacak

print("1. sayıyı giriniz = ", end="")
sayi1Str = input()
sayi1 = int(sayi1Str)

sayi2Str = input("2. sayıyı giriniz = ")
sayi2 = int(sayi2Str)

sayi3 = int(input("3. sayıyı giriniz = "))

ortalama = (sayi1 + sayi2 + sayi3) / 3

kalan = ortalama % 2
ciftmi = kalan == 0
print("Ortalama = " + str(ortalama))
print("Ortalama Çift mi = " + str(ciftmi))