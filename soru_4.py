#Soru 4 : Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir Python kodu yazınız.


sayi = int(input("Bir sayi giriniz:"))


if sayi % 2 == 0:
    print("Sayi cift sayidir.")
else:
    print("Sayi tek sayidir.")
