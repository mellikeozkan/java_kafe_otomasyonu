import numpy as np

dizi=np.array([1,2,3,4,56])

maks=np.max(dizi)

min=np.min(dizi)
print("Dizi içerisindeki en düşük değere sahip veri: ",min)
print("---------------------------------------------------")
print("Dizi içerisindeki en yüksek değere sahip veri: ",maks)
print("---------------------------------------------------")
toplam=np.sum(dizi)
kume_toplam=np.cumsum(dizi)
print("dizi içindeki sayıların toplamı:",kume_toplam) #hep bir öncekiyle toplayıp yazar  [ 1  3  6 10 66]

