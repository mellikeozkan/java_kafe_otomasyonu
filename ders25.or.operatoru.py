data_sifre=123
data_isim="Melike"

isim=input("lütfen isminizi giriniz:")
sifre=int(input("lütfen şifrenizi giriniz:"))

kontrol = data_sifre==sifre or data_isim==isim
print(kontrol)  # burada OR operatörü kullanıldığı için sadece birinin doğru olması çıktıda doğru ifadesini verecektir 

