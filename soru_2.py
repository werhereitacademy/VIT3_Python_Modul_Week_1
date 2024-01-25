#Soru 2 : Kullanıcıdan bir sayı girişi alın ve bu sayıya kadar olan çift sayıları ekrana yazdıran bir Python programı yazın. Bunu once 'for' ile sonra 'while' donguleri ile yapiniz. 

#for dongusu ile


sayi = int(input("Bir sayi giriniz:"))
for i in range(2,sayi+1,2):
    print(i)
    
    
#while dongusu ile

sayi = int(input("Bir sayi giriniz:"))
i = 2
while i <= sayi:
    print(i)
    i += 2
    
