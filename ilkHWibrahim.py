#Soru1:
for i in range(1,11):
    print(i)


#Soru2:
#a)
a=int(input("Bir sayı giriniz:"))

for i in range(1,a):
   if i%2==0 :
       print(i)

#b)
a=int(input("Bir sayı giriniz:"))
i=0
while a>i :
    if i%2==0:
        print(i)
    i = i + 1


#Soru3:


#Bir küçük bir de büyük sayı girmeniz gerekiyor


a=int(input("Bir küçük sayı giriniz:"))
b=int(input("Bir büyük sayı giriniz:"))

for i in range(a,b+1):
   print(i)

#Soru4:

while True:
   a = int(input("Bir sayı giriniz:"))
   if a%2==0 :
       print("Girdiğiniz sayı çift sayıdır.")
   else:
       print("Girdiğiniz sayı tek sayıdır.")

#Soru5:
faktr = 1
while True:
   sayı = int(input("faktöriyelini hesaplamak istediğiniz pozitif tamsayıyı giriniz: "))


   for i in range(1,sayı+1):
       faktr=faktr*i
   print(f"{sayı} sayısının faktöriyeli:", faktr)



#Soru6:
#Girilen sayının asal olup olmadığını anlamak
a= int(input("bir pozitif tamsayı giriniz:"))
i=2
if a>i:
   for i in range(2,a+1):
       if a%i==0:
           print("Girilen sayı asal değildir")
           break
       else:
           print("Girilen sayı asaldır")
           break
if a==2:
   print("Girilen sayı asaldır")


#Soru7:
#100 sayısına kadarki Fibonacci sayılarını sıralayan kod
c=0
b=1
for a in range(2,100):
    a = b + c
    b = c
    c = a
    if a>100:
        break
    print(a, end=",")

#Soru8:
#girilen kelimeyi ters yazma
a=input("bir kelime yazın:")
txt = a[::-1]
print(txt)


#Soru9:
#girilen kelimeyi palindrommu kontrol etme
kelime=input("bir kelime yazın:")
tersi = kelime[::-1]


if kelime==tersi:
   print("Bu kelime palindromdur")
else:
   print("Bu kelime palindrom değildir")



#Soru10:
#Vücut kitle endeksi


boy = float(input("Boy (m):"))
kilo = float(input("Ağırlık (kg):"))


endeks = kilo / (boy**2)




if endeks < 25:
   print("\nZayıfsınız.\nVücut kitle endeksiniz:{}".format(endeks))




elif endeks >= 25 and endeks <= 30:
   print("\nNormalsiniz \nVücut kitle endeksiniz:{}.".format(endeks))




elif endeks > 30 and endeks <=40:
   print("\nKilolusunuz.\nVücut kitle endeksiniz:{}".format(endeks))
elif endeks > 40:
   print("\nAşırı kilolusunuz.\nVücut kitle endeksiniz:{}".format(endeks))




#Soru11:
#girilen 3 sayıdan büyük olanı bastırmak




a=int(input("1. sayıyı girin:"))
b=int(input("2. sayıyı girin:"))
c=int(input("3. sayıyı girin:"))




if a>b and a>c:
   print("Büyük sayı {}".format(a))
if b>a and b>c:
   print("Büyük sayı {}".format(b))
if c>b and c>a:
   print("Büyük sayı {}".format(c))


#Soru12:
#Ders notlarının hesaplanması
i=1
for i in range(1,5):
   vize= float(input("Vize notunuzu girin:"))
   final= float(input("Final notunuzu girin:"))
   ortalama= vize*0.4+final*0.6
   print("Ders puanınız:", ortalama)




   if ortalama<50:
       print("BAŞARISIZ")




   else:
       print("BAŞARILI")
i=i+1







