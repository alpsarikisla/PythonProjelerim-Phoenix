# Sayı aralığı kontrol
# konsoldan sayı alalım
# alınan sayı;
# 10 - 40 arasında ise sayı 1. aralıkta
# 60 - 90 arasında ise sayı 2. aralıkta
# yazsın.

print("Lütfen sayı giriniz")
sayiStr = input()
sayi = int(sayiStr)

if sayi >= 10 and sayi <= 40:
    print("Sayı 1. aralıktadır.")
elif sayi >= 60 and sayi <= 90:
    print("Sayi 2. aralıktadır")
else:
    print("Sayı tanımlı aralıklarda değildir")
# elif üsetteki if değilse eğer anlamında kullanılır
# bu kullanım ile if, elif ve else birbirine bağlanmış olur
