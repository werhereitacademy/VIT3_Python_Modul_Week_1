#Soru 8 : Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazınız.
while True:
    kelime = input("Bir kelime giriniz:")
    ters_kelime = kelime[: : -1]
    harf_sayisi = len(kelime)
    print("kelimenin tersi:",ters_kelime)
    print("kelimenin harf sayisi:",harf_sayisi)
    

    
