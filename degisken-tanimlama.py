# 2000 in yüzde 18 ini hesaplayıp ekrana yazdırma 

urunAFiyat = 2000
urunBFiyat = 3000
kdvOrani = 0.20
print(urunAFiyat + (urunAFiyat * kdvOrani))    # Ürün A
print(urunBFiyat + (urunBFiyat * kdvOrani))    # Ürün B

urunToplami = urunAFiyat + urunBFiyat
print(urunToplami + (urunToplami * kdvOrani))
