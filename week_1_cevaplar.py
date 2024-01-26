#Soru 1 : 1'den 10'a kadar olan sayıları ekrana yazdıran bir Python kodu yazınız.

for i in range(1,11):
    print(i)
    




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
    
    
    
    
    
    
   # Soru 3 : Kullanıcıdan bir başlangıç ve bitiş değeri alan ve bu değerler arasındaki tüm sayıları ekrana yazdıran bir Python kodu yazınız(bitis degeri dahil).

baslangic = int(input("baslangic: "))
bitis = int(input("bitis: "))

i = baslangic

while i <= bitis:
    print(i)
    i += 1
    
    
    
    
    
  #Soru 4 : Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir Python kodu yazınız.


sayi = int(input("Bir sayi giriniz:"))


if sayi % 2 == 0:
    print("Sayi cift sayidir.")
else:
    print("Sayi tek sayidir.")
    
    
    
    
    
    
'''Soru 5 : Kullanıcıdan pozitif bir tam sayı girişi alın ve faktöriyelini hesaplayan bir Python programı yazın. Faktöriyel, bir sayının kendisi ile 1 arasındaki tüm pozitif tam sayıların çarpımıdır. 
 Örneğin: kullanıcı 5 girdiyse program şu çıktıyı vermeli:
 Kullanıcıdan bir sayı girin: 5 
 Faktöriyel: 120'''
 
 
sayi = int(input("Bir sayi giriniz: "))
deger = 1
for i in range(sayi):
    deger = deger * (i+1)
    
print("Faktoriyel:",deger)









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
            
            
            
            
            
            
#Soru 7
#Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları içeren bir liste olarak döndüren bir döngü nasıl oluşturulur?
#Orn [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

sinir = int(input("Fibonacci dizisini hangi sınıra kadar hesaplamak istiyorsunuz? "))

fibonacci_dizisi = [0, 1]

while fibonacci_dizisi[-1] + fibonacci_dizisi[-2] <= sinir:
    yeni_terim = fibonacci_dizisi[-1] + fibonacci_dizisi[-2]
    fibonacci_dizisi.append(yeni_terim)

print(f"{sinir}'e kadar Fibonacci dizisi : {fibonacci_dizisi}")








#Soru 8 : Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazınız.
while True:
    kelime = input("Bir kelime giriniz:")
    ters_kelime = kelime[: : -1]
    harf_sayisi = len(kelime)
    print("kelimenin tersi:",ters_kelime)
    print("kelimenin harf sayisi:",harf_sayisi)
    
    
    
    

    
    
    
  #Soru9
#Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom (tersten okunduğunda aynı olan)
#olup olmadığını kontrol eden bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?

while True:
    kelime = input("Bir kelime giriniz:")
    ters_kelime = kelime[: : -1]

    if kelime == ters_kelime:
        print("Kelime palindromdur.")
    else:
        print("Kelime palindrom degildir.")
        
        
        
        
        
''' Soru 10 : Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.(kilo indeks hesabı için internete bakabilirsiniz) 
Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz. Kilo indeksi 
25’in altında ise zayıf, 
25-30 arasında ise normal, 
30-40dan büyük ise kilolu, 
40tan büyük ise aşırı kilolu sonuçlarına varsın.'''


print("Vucut Kitle Indeks Hesaplama ")
boy = float(input("Boy(m): "))
kilo = int(input("Kilo(kg): "))

endeks = kilo/(boy*boy)

if endeks < 25:
    print("Zayif")
elif endeks >25 and endeks < 30:
    print("Normal")
elif endeks >30 and endeks < 40:
    print("Kilolu")
elif endeks >40:
    print("Dikkat!OBEZSINIZ.")
    
    
    
    
    
    
 #Soru 11
#Bir kullanıcının girdiği üç sayının en büyüğünü bulan bir Python programı nasıl yazılır?
ilk_sayi = int(input("Lutfen ilk sayiyi giriniz:"))
ikinci_sayi = int(input("Lutfen ikinci sayiyi giriniz:"))
ucuncu_sayi = int(input("Lutfen ucuncu sayiyi giriniz:"))

liste = [ilk_sayi,ikinci_sayi,ucuncu_sayi]
liste.sort()
print("Girmis oldugunuz en yuksek sayi:",liste[-1])








#Soru 12
# Bir ogrenciden herhangi bir ders icin Vize ve Final notlarıni alin. Ara sınav notunun %40'ı ile final notunun %60'ının toplamı yıl sonu ortalamasını verecektir.
#Ortalama 50'nin altında ise ekranda “BAŞARISIZ”,
#50 ve üzerinde ise “BAŞARILI” çıktısı ekrana gelecektir. Bu baskı işlemi 4 derstir. yapılacak ve dersler birbiri ardına yazılacaktır.

liste = []

def nothesapla(vize, final):
   ortalama = (vize * 0.4) + (final * 0.6)
   print(ortalama)
   if ortalama >= 50:
       return "BASARILI"
   elif ortalama < 50:
       return "BASARISIZ"
while len(liste) <= 6:
   ders_adi = input("Dersin Adi:")
   vize_not = float(input("Vize Notu:"))
   final_not = float(input("Final Notu:"))
   liste.append(ders_adi)
   liste.append(nothesapla(vize_not, final_not))

print(liste)









   

  

           
          
   