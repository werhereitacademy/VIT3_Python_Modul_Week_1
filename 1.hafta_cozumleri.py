#Soru 1'in cevabi:

for i in range(1,10):
    print(i)

# Soru 2'nin cevabi:

sayi = int(input('Bir sayi girin: '))
for i in range(0, sayi):
    if i % 2 == 0:
        print(i)

sayi = int(input('Bir sayi girin: '))
i = 0
while i <= sayi:
        print(i)
        i += 2

#Soru 3'un cevabi:

sayi1 = int(input('Baslangic sayisini girin: '))
sayi2 = int(input('Bitis sayisini girin: '))
for i in range(sayi1, sayi2+1):
    print(i)

#Soru 4'un cevabi:

sayi = int(input('Bir sayi girin: '))
if sayi % 2 == 0:
    print(f'{sayi} sayisi cift sayidir')
else:
    print(f'{sayi} sayisi tek sayidir')

#Soru 5'in cevabi:

sayi = int(input('Bir pozitif tam sayi girin: '))
i = 0
toplam = 1
while i < sayi:
    i += 1
    toplam *= i
print(f'Girilen sayi: {sayi} faktoriyel: {toplam}')


sayi = int(input('Bir pozitif tam sayi girin: '))
toplam = 1
for i in range(1, sayi+1):
    toplam *= i
print(toplam)
    
#Soru 6'nin cevabi:

sayi = int(input('Bir pozitif tam sayi girin: '))
if sayi % 2 != 0 and sayi % 3 != 0 and sayi % 5 != 0 and sayi % 7 != 0:
    print('Asal')
elif sayi == 2 or sayi == 3 or sayi == 5 or sayi == 7:
    print('Asal')
else:
    print('Asal Degil')
    
sayi = int(input('Bir pozitif tam sayi girin: '))
liste = [2,3,5,7]
for i in liste:
    if sayi % i != 0:
        print('Asal')
        break
    elif sayi in liste:
        print('Asal')
        break
    else:
        print('Asal degil')
        break
    
#Soru 7'nin cevabi:

sayi = int(input('Bir sayi girin: '))
liste = []
a, b = 0, 1
while a < sayi:
    liste.append(a)   
    a, b = b, a+b
print('Fibonacci dizisi', liste) 
    

# Soru 8'in cevabi:

kelime = input('Bir kelime girin: ')
ters_kelime = kelime[::-1]
print('Kelimenin tersi: ', ters_kelime)

kelime = input('Bir kelime girin: ')
uzunluk = len(kelime)
i = uzunluk - 1
while i >=0:
    print('Kelimenin tersi: ', kelime[i], end= ' ')
    i -= 1


kelime = input('Bir kelime girin: ')
uzunluk = len(kelime)
ters_kelime = ''
for i in range(uzunluk-1,-1,-1):
    ters_kelime += kelime[i]
print('Kelimenin tersi: ', ters_kelime)

#Soru 9'un cevabi: 

kelime = input('Bir kelime girin: ')
uzunluk = len(kelime)
i = uzunluk - 1
ters_kelime = ''
for harf in range(i, -1, -1):
    ters_kelime += kelime[harf]
if ters_kelime == kelime:
    print('Girilen kelime Palindrom')
    
else:
    print('Girilen kelime Palindrom degil')
    
kelime = input('Bir kelime girin: ')
uzunluk = len(kelime)
i = uzunluk - 1
ters_kelime = ''
while i >= 0:
    ters_kelime += kelime[i]
    i -= 1
if ters_kelime == kelime:
    print('Girilen kelime Palindromdur')
    
else:
    print('Girilen kelime Palindrom degildir')

#Soru 10'nun cevabi:

boy = float(input("Boyunuzu metre cinsinden girin: "))
kilo = float(input('Kilonuzu kilogram cinsinden girin: '))
VKI = kilo / (boy**2)
if VKI < 25:
    print('Zayif')
elif 25 <= VKI <= 30:
    print('Normal')
elif 30 < VKI <= 40:
    print('Kilolu')
elif VKI > 40:
    print('Asiri kilolu')
else:
    print('Gecersiz veri girdin')    

#Soru 11'in cevabi: 

sayi1 = int(input('Birinci sayiyi girin: '))
sayi2 = int(input('Ikinci sayiyi girin: '))
sayi3 = int(input('Ucuncu sayiyi girin: '))

if sayi3 < sayi1 > sayi2:
    print(f'Birinci sayi {sayi1} en buyuk sayidir')
elif sayi3 < sayi2 > sayi1:
    print(f'Ikinci sayi {sayi2} en buyuk sayidir')
else:
    print(f'Ucuncu sayi {sayi3} en buyuk sayidir')

sayi1 = int(input('Birinci sayiyi girin: '))
sayi2 = int(input('Ikinci sayiyi girin: '))
sayi3 = int(input('Ucuncu sayiyi girin: '))

En_buyuk_sayi = max(sayi1, sayi2, sayi3)
print('Girilen sayilardan en buyugu: ', En_buyuk_sayi)


sayilar = []
for i in range(3):
    sayi = int(input(f'{i+1}. sayiyi girin: '))
    sayilar.append(sayi)

En_buyuk_sayi = sayilar[0]
for sayi in sayilar:
    if sayi > En_buyuk_sayi:
        En_buyuk_sayi = sayi
print(f"Girilen sayilardan {sayi} en buyuk sayidir")
    
#Soru 12'nin cevabi: 

dersler = []
for i in range(4):
    vize = int(input(f'{i+1}. ders icin vize notunu girin: '))
    final = int(input(f'{i+1}. ders icin final notunu girin: '))
    ortalama = vize * 0.4 + final * 0.6
    dersler.append(ortalama)

    if ortalama >= 50:
        print(f"{i+1}. ders BASARILI")
    else:
        print(f'{i+1}. ders BASARISIZ')
