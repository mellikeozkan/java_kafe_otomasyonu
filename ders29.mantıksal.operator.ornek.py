vize_notu=int(input("Lütfen vize notunu giriniz:"))
final_notu=int(input("Lütfen final notunu giriniz:"))

ortalama=(final_notu+vize_notu)/2

if ortalama>=85:
    print("Tebrikler AA ile geçtiniz",ortalama)

elif ortalama >=65:                                     # işlem en üstten yapılmaya başlar üstteki if-elif koşulu olmadıkça aşağıya doğru işlem yapılmaya başlar 
    print("Tebrikler BB ile geçtiniz ",ortalama)

elif ortalama >=50 :
    print("Tebrikler CC ile geçtiniz",ortalama)

else:
    print("Üzgünüz ders tekrarı",ortalama)