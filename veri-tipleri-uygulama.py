#uygulama 1: yarı çapı verilen bir dairenin alan ve cevresini hesaplayınız
# alan : 3*r*r
# çevre : 2*3*r

pi = 3.14

r = float(input(" Yarı çap : "))

alan = pi * r * r
cevre = 2 * pi * r

print("Alan : " + str(alan))
print(" Çevre : " + str(cevre))
