#soru 1
#1`den 10`a kadar olan sayilari ekrana yazdiriniz.

for i in range(1,11):
  print(i)


#soru 2
#kullanicidan bir girisi alin ve bu sayiya kadar olan cift sayilari ekrana yazdiran bir Python prgrami yazin.
#Once `for` sonra ` while` dongusu ile yapin.

sayi = int(input("Bir sayı girin: "))

print(f"{sayi}'e kadar olan çift sayılar :")
for i in range(0, sayi+1, 2):
    print(i)


sayi = int(input("Bir sayı girin: "))

print(f"{sayi}'e kadar olan çift sayılar :")
i = 0
while i <= sayi:
    print(i)
    i += 2

#soru3
#Kullanicidan bir baslangic ve bir bitis degeri alan bu degerler arasinda olan tum sayilari ekrana basan bir Python kodu yazin.(Bitis dahil.)
baslangic = int(input("Başlangıç değerini girin: "))
bitis = int(input("Bitiş değerini girin: "))
print(f"{baslangic} ile {bitis} arasındaki tüm sayılar :")

while baslangic <= bitis:
    print(baslangic)
    baslangic += 1

#soru4
#Kullanicadan bir sayi alin ve bu sayinin cift mi tek mi oldugunu ekrana yazdiran bir program yaziniz.

s = int(input("Sayinizi girin:"))
while s >= 0:
   if s % 2 == 0:
       print("Girilen sayi cifttir")
       break
   else:
       print("Girilen sayi tektir")
       break

#soru 5
#Kullanicidan pozitif bir tam sayi girisi alin ve faktoriyeline alan bir Python programi alin.

pozitif_sayi = int(input("Pozitif bir sayi girin:"))
faktoriyel = 1
for i in range(1, pozitif_sayi+1):
   faktoriyel *= i
print(faktoriyel)


#soru 6
#Kullanicadan bir sayi alin ve bu sayinin asal olup olmadigini kontrol eden bir Pythin kodu yazin.
while True:
    sayi = int(input("Bir sayi giriniz:"))
    if sayi < 2:
        print(sayi, "Asal degildir.")

    else:
        asal = True

        for i in range(2, sayi):
            if sayi % i == 0:
                print(sayi, "Asal degildir.")
                asal = False
                break

        if asal == True:
            print(sayi, "Asaldir.")

#Soru 7
#Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları içeren bir liste olarak döndüren bir döngü nasıl oluşturulur?
#Orn [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

sinir = int(input("Fibonacci dizisini hangi sınıra kadar hesaplamak istiyorsunuz? "))

fibonacci_dizisi = [0, 1]

while fibonacci_dizisi[-1] + fibonacci_dizisi[-2] <= sinir:
    yeni_terim = fibonacci_dizisi[-1] + fibonacci_dizisi[-2]
    fibonacci_dizisi.append(yeni_terim)

print(f"{sinir}'e kadar Fibonacci dizisi : {fibonacci_dizisi}")


#Soru 8
#Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazınız.
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




#Soru 10
#Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.
#(kilo indeks hesabı için internete bakabilirsiniz agirlik / boy(metre)karesi) Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz.
#Kilo indeksi 25’in altında ise zayıf, 25-30 arasında ise normal, 30-40dan büyük ise kilolu, 40tan büyük ise aşırı kilolu sonuçlarına varsın.

kilo = int(input("Lutfen kilonuzu giriniz:"))
boy= float(input("Lutfen cm cinsinden boyunuzu giriniz:"))

boy= boy/100
kitle_endeksi = kilo /( boy * boy)
print(kitle_endeksi)
if kitle_endeksi < 25:
    print("Sonucunuz'Zayif'")
elif kitle_endeksi >=25 and kitle_endeksi <30:
    print("Sonucunuz'Normal'")
elif kitle_endeksi >=30 and kitle_endeksi <=40:
    print("Sonucunuz'Kilolu")
else:
    print("Sonucunuz'Asiri Kilolu'")


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
