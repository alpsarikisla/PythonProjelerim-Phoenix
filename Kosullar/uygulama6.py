# Konsoldan kullanıcı adı ve şifre alınız
# Kullanıcı adı admin şifre 1234 ise
# Hoşgeldiniz yazınız
# Değilse Geçersiz kullanıcı yazınız
kullaniciadi = input("Kullanıcı Adı = ")
sifre = input("Şifre = ")
if kullaniciadi == "admin" and sifre == "1234":
    print("Hoşgeldiniz")
else:
    print("Geçersiz Kullanıcı")