import numpy as np

matris = np.array([[1,2,3],[4,5,6],[7,8,9]])  #en dışarda 2 tane köşeli parantez var bu 2 boyutlu olduğu anlamına gelir.
eleman = matris[1,2]    # 2.satırdaki 3. sutünda elemanı istiyor yani 6 (saymaya 0 dan başladığımız için böyle oluyor )
print(eleman)