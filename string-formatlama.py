# string concat Birleştirme 
ad = "Melike"
soyad = "Özkan"
yas = 22

# msj ="My name is " + ad + " " + soyad +"." + "I'm " + str(yas)+ " years old." My name is Melike Özkan.I'm 22 years old.Çıktısını verir.
# print(msj)


# STRİNG FORMAT
# msj = "My name {0} {1}. I'm {2} years old .".format(ad,soyad,yas)
# print(msj)   # formattan sonraki sıraya 0-1-2 verdik .parantezle  istediğimiz gibi sıralayabiliriz .bunun yeine şunu da yapabilirdik .
# msj = "My name {a} {s}. I'm {y} years old .".format(a=ad,s=soyad,y=yas)


# F-STRİNG
msj = f"My name {ad} {soyad} . I'm {yas} years old."
print(msj)  # Burada direkt olarak üstte yazılan parametreleri kullanabiliriz.
