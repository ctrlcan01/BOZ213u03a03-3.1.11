gelir = float(input("Yıllık gelirinizi giriniz: "))

if gelir <= 85528:
    vergi = gelir * 0.18 - 556.02
else:
    vergi = 14839.02 + (gelir - 85528) * 0.32

if vergi < 0:
    vergi = 0

vergi = round(vergi, 0)

print("Ödenecek vergi:", vergi, "taler")
