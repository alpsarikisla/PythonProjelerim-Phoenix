# Konsoldan alınan sayı çift mi?
# çift ise true değilse false yazacak
print("Lütfen Bir Sayı Giriniz")
sayiStr = input()
sayi = int(sayiStr)

kalan = sayi % 2
sonuc = kalan == 0

print("Çift mi = ", end="")
print(sonuc)