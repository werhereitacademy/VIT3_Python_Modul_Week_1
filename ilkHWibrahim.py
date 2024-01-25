# S1:
for i in range(1,11):
    print(i)

# S2/1:
a=int(input("Bir sayı giriniz:"))


for i in range(1,a):
   if i%2==0 :
       print(i)


# S2/2:
a=int(input("Bir sayı giriniz:"))
i=0
while a>i :
    if i%2==0:
        print(i)
    i = i + 1

# S3:

#Bir küçük bir de büyük sayı girmeniz gerekiyor


a=int(input("Bir küçük sayı giriniz:"))
b=int(input("Bir büyük sayı giriniz:"))


for i in range(a,b+1):
   print(i)

# S4:

while True:
   a = int(input("Bir sayı giriniz (Tek mı cıft mı soyleyım!:"))
   if a%2==0 :
       print("Girdiğiniz sayı çift sayıdır.")
   else:
       print("Girdiğiniz sayı tek sayıdır.")


