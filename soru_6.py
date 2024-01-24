#Soru 6 : Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazınız.


while True:
    sayi=int(input("Bir sayi giriniz:"))
    if sayi < 2:
        print(sayi,"Asal degildir.")
        
    else:
        asal=True
        
        for i in range(2,sayi):
            if sayi % i == 0:
                print(sayi,"Asal degildir.")
                asal=False
                break
            
        if asal == True:
            print(sayi,"Asaldir.")
        
        
