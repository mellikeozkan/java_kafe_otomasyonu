ateş_durumu=int(input("Ateş derecenizi yazınız:"))  #lower yapma amacımız cevabın küçük harflerle istemek 
öksürük_durumu=input("Öksürük durumunuz var mı : E/H :").lower
gün_sayısı=int(input("kaç gündür var :"))
baş_ağrısı=input("Baş ağrınız var mı :").lower

if ateş_durumu>=39:
    if gün_sayısı>=3:
        print("**** Lütfen hastaneye gidiniz")
else:
    print("Şikayetleriniz devam ederse sağlık kuruluşuna gidiniz")

if (ateş_durumu>=39) and (öksürük_durumu=="e") and (gün_sayısı>=3) and (baş_ağrısı=="e"):
    print("**** ACİL OLARAK HASTANEYE GİTMENİZ GEREKMEKTEDİR")

elif (ateş_durumu>=39) or (öksürük_durumu=="e") or (gün_sayısı>=3) or (baş_ağrısı=="e"):
    print("rahatsızlığınız devam ederse bir sağlık kuruluşuna gitmelisiniz ")

else:
    print("Ateş durumunuz 39 'un üzerine çıkarsa lütfen sağlık kuruluşuna gidiniz")