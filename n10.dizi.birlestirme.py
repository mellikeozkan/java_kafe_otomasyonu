import numpy as np

# dizi1=np.array([1,2,3])
# dizi2=np.array([4,5,6])

#TEK BOYUTLU DİZİYİ BİRLEŞTİRME CONCATENATE

# birlesik_dizi=np.concatenate((dizi1,dizi2))
# print("Diziler birleştirildi ",birlesik_dizi)

#İKİ BOYUTLU DİZİ NİRLEŞTİRME 

# dizi1=np.array([[1,2,3],[4,5,6]])
# dizi2=np.array([[7,8,9],[10,11,12]])

# birlesik_dizi=np.hstack((dizi1,dizi2))
# print("İki boyutlu dizi birleştirme ",birlesik_dizi )  #İki boyutlu dizi birleştirme  [[ 1  2  3  7  8  9]
# [ 4  5  6 10 11 12]] çıktısı bu yatayda birleşimi  H HARFİ YATAY

dizi1=np.array([[1,2,3],[4,5,6]])
dizi2=np.array([[7,8,9],[10,11,12]])

birlesik_dizi=np.vstack((dizi1,dizi2))
print("İki boyutlu dizi birleştirme ",birlesik_dizi )  # V HARFİ DİKEY 