data_password=123
data_isim="Melike"

isim=input("LÜtfen isminizi giriniz:")
password = int(input("Lütfen şifrenizi giriniz:"))

kontrol = data_password == password and data_isim== isim
print(kontrol)   # eğer bir tanesi bile yanlış çıkarsa false dönecek 