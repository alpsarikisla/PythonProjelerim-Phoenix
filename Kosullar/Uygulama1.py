# Konsoldan alınan sayı tek mi çift mi?
print("Lütfen Kontrol edilecek sayıyı giriniz")
sayi1str = input()
sayi1 = int(sayi1str)
kalan = sayi1 % 2
if kalan == 0:
    print("Girdiğiniz sayı çifttir")
else:
    print("Girdiğiniz sayı tektir")