import numpy as np

# dizi = np.array([1,2,3,4,5])
# print(dizi) bunun çıktısı [1 2 3 4 5] olur

# dizi = np.arange(0,10,2) # arange belli bir dizide veri oluşturur.parantez içindekiler 0 dan 10 a kadar 2 2 aratacak sekılde diziyi yazmzak istediğimidendir .
# print(dizi)   bunu çıktısı [0 2 4 6 8] olacak

# dizi = np.linspace(0,1,5) bu 0 dan 1 e kadar 5 eşit parçaya böl demek .
# print(dizi)

dizi = np.array([1,2,3,4,5])
print(dizi)

boyut =dizi.ndim
veri_turu=dizi.dtype
print("Dizinin boyutu :",boyut)  
print("Dizinin tipi : ",veri_turu)


