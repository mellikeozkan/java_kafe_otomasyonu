import numpy as np

# örneğin elimizdeki verilerden 50 olanı bana göster dediğinde veya 98 üstünü bana göster dediğimizde işimize yarar

dizi=np.array([10,20,30,40,50,68,98,74,25,11,33])
boolean_mask=(dizi>50) & (dizi <70) #ve 
#secilmis=dizi[boolean_mask] # bunu yazmasaydık 50 den büyük olanlar true false seklinde sıra sıra yazılmış olup karmaşıklığa sebebiyet verecekti

print("50 ile 70 arasında olan elemanlar :",dizi[boolean_mask])