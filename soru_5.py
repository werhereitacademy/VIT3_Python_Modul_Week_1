'''Soru 5 : Kullanıcıdan pozitif bir tam sayı girişi alın ve faktöriyelini hesaplayan bir Python programı yazın. Faktöriyel, bir sayının kendisi ile 1 arasındaki tüm pozitif tam sayıların çarpımıdır. 
 Örneğin: kullanıcı 5 girdiyse program şu çıktıyı vermeli:
 Kullanıcıdan bir sayı girin: 5 
 Faktöriyel: 120'''
 
 
sayi = int(input("Bir sayi giriniz: "))
deger = 1
for i in range(sayi):
    deger = deger * (i+1)
    
print("Faktoriyel:",deger)

 