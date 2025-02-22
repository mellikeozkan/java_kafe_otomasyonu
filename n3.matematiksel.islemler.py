import numpy as np

dizi1=np.array([1,2,3,4,5]) 
dizi2=np.array([11,12,13,14,15])

# toplam = dizi1 + dizi2
# cıkarma = dizi1 - dizi2
# çarpma = dizi1 * dizi2
# bölme = dizi1 / dizi2

# print(toplam)   # 1.sayıyla 1. ayı toplanır ,2.sayıyla 2. sayı toplanır 
# print(cıkarma)
# print(çarpma)
# print(bölme)    

toplam = np.sum(dizi1)
çarpma =np.prod(dizi1)  # çarpma
karekök= np.sqrt(dizi1)  # karekök alma

ort= np.mean(dizi1)  # ortralama hesaplama

medyanal= np.median(dizi1)

starndartsapma=np.std(dizi2)


print(starndartsapma)