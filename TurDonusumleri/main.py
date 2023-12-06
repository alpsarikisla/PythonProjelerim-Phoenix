isim = "Alp"
soyisim = "Sarıkışla"
yas = 20
# print(isim + " " + soyisim + " " + yas)
# string(metinsel)  alanlara integer değer eklemez

# TÜR DÖNÜŞÜMÜ
# integer türünde olan yas değişkeninin içindeki veriyi
# str() parantezi ile string türüne döndürdük
metinselyas = str(yas)
print("Yaş = " + str(yas))

# Konsoldan Veri Almak
# Kullanıcıların girmesini istediğimiz verileri konsoldan almak için
# input() komutu kullanılır.
print("Lütfen adınızı giriniz")
gelenveri = input()#input ile alınan veri değişkene atıldı
print("Merhaba = " + gelenveri)
