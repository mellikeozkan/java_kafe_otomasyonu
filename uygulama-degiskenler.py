


#müşteri bilgilerini ve satın aldığı ürün bilgilrini değişkenler içerisinde saklayınız.
#toplam ödenen ücret,ödenen miktarın kdv oranı yazdır


isim = "Sadık Turan"
telNo = "05213657988"
mail = "info@sadikturan.com"
sehir = "Kocaeli"
print(isim)
print(telNo)
print(mail)
print(sehir)
 

fiyat = 550
urunadi = "Kablosuz maouse "
fiyat2 = 650 
urunadi2 = "Kablosuz Klavye "
fiyat3 = 55000
urunadi3 = "Dizüstü Bilgisayar "
kdvOrani = 0.18



toplamOdenenUcret = fiyat + fiyat2 + fiyat3 
print("Toplam Ödenen Miktar :" + str(toplamOdenenUcret))

print("Toplam Kdv Oranı :"+ str(toplamOdenenUcret * kdvOrani))






