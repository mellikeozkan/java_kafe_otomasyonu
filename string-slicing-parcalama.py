kurs = "python ile programlama"

print(kurs[0])  # p karakteri gelir 
print(kurs[-1]) # a karakteri gelir son karakter -1 den başlar .-2.karakter m harfidir.

adet = len(kurs)  # len fonksiyonu kaç adet olduğunu gösteren fonksiyondur .Boşluk karakterleri de sayılır .

print(adet)
print(kurs[adet-1])  # a karakterine erişilir.

print(kurs[0:5])  # ekrana pytho yazısı çıkar slicingde son sayı işleme dahil olmaz .
print(kurs[0:6])  # ekrana python yazısı çıkar.
print(kurs[:6])   # 0'ı yazmadan da yine aynı sonucu elde ederiz.python yazısı çıkar.
print(kurs[11:22]) # Programlama yazısı ekrana çıkar.
print(kurs[11:len(kurs)])  # Programlama yazısı ekrana çıkar.
print(kurs[11:])   # Programlama yazısı ekrana çıkar.bir önceki işlemle aynı olur.
print(kurs[0:20:2]) # dersek bir harfi alır bir harfi almaz .
print(kurs[::])  # Stringi sonuna kadar alır .
print(kurs[ ::-1]) # tamamen ters çevirir."amalmargorp eli nohtyp"