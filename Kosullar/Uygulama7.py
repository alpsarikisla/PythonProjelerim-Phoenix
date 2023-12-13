# konsoldan alınan sayı 0 - 100 arasındaysa kabul edildi
# değilse kabul edilmedi yazılacak

print("Lütfen 0 - 100 arasında bir sayı giriniz")
sayiStr = input()
sayi = int(sayiStr)
# sayi = int(input("Lütfen 0 - 100 arasında bir sayı giriniz"))
# sayi >= 0 and sayi <= 100:
if 0 <= sayi <= 100:
    print("Kabul edildi")
else:
    print("Reddedildi")
