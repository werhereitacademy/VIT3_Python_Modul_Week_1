#Soru 1 : 
print(*range(10))

#***********************************#
#Soru 2:
#version1
num = int(input("Type een getal:"))
print(*range(0,num,2)) 

#version2
num = int(input("Type een getal:"))
for i in range(0,num,2):
    print(i,end=" ") 
#version3
num = int(input("Type een getal:"))
i = 0
while(i < num):
    if i%2 == 0:
        print(i,end=" ")
    i+=1
  
#***********************************#
#Soru 3
num1 = int(input("Type een getal_1:"))
num2 = int(input("Type een getal_2:"))
num_min = min(num1,num2)
num_max = max(num1,num2)
print(*range(num_min,num_max+1))

#***********************************#
#Soru 4
num = int(input("Type een getal:"))
if num%2 == 0:
    print(f"Het nummer {num} is EVEN")
else: 
    print(f"Het nummer {num} is ONEVEN")

#***********************************#
#Soru 5
import math
num = int(input("Type een getal:"))
print(f"{num}!={math.factorial(num)}")

#***********************************#
#Soru 6
while(True):
    num = int(input("Type een getal:"))
    if num == 1:
            print(f"{num}= Geen priemgetal")
            break     
    for i in range(2,num):
        if num%i == 0 :
            print(f"{num}= Geen priemgetal")
            break
    else:
        print(f"{num}= Priemgetal")

#***********************************#
#Soru 7
new_s1 = 0
new_s2 = 1
new_s3 = new_s2
i = 0
fib_list = []
num = int(input("Type een getal:"))
while i <= num :
    fib_list.append(new_s3)
    new_s1 = new_s2
    new_s2 = new_s3
    new_s3 = new_s1 + new_s2
    i+=1 
fib_list.append(0)
fib_list.append(1)
print(sorted(fib_list))
#***********************************#
#Soru 8
woord = input("Type een woord:")
i = -1
y = (len(woord)+1)*(-1)
while(i > y ):
   print(woord[i],end="")
   i-=1

#***********************************#
#Soru 9
while(True):
    woord = input("Type een woord:")
    woord_len = (len(woord))-1
    for x in range(woord_len//2):
        if woord[x] != woord[(woord_len-x)]:
            print("Geen Palindrom") 
            break              
    else:
        print("Palindrom")

#***********************************#
#Soru 10
while(True):
    gewicht = float(input('Uw gewicht(kg) ='))
    lengte = float(input('Uw lengte(m) ='))
    result = gewicht / pow(lengte,2)
    if result < 25 :
        print('NORMAL')
    elif result < 30 :
        print('FAZLA KILOLU')
    elif result < 40 :
        print('OBEZ')
    elif result > 40 :
        print('ASIRI KILOLU')

#***********************************#
#Soru 11
cijfers = []
i = 1
while(i < 4):
    a = int(input(f'{i}.Cijfer='))
    cijfers.append(a)
    i += 1
print('Grooter cijfer:', max(cijfers))

#***********************************#
#Soru 12
num = 1
list_lessen = []
list_midterm = []
list_final = []
list_result = []
list_average = []

while(num < 5):
    les = input(str(num ) + ".Enter the name of course:")
    list_lessen.append(les)
    midterm_grade = float(input(str(les) + ' midterm test grade:'))
    list_midterm.append(midterm_grade)
    final_grade = float(input(str(les) + ' final test grade:'))
    list_final.append(final_grade)
    result = midterm_grade*0.4 + final_grade*0.6
    list_average.append(result)
    if result >= 50.00 :
        x = "PASSED"
        list_result.append(x)
    else:
        x = "FAILED"
        list_result.append(x)    
    num+=1 
print('*'*38)    
print("Lessen\tMidterm\tFinaal\tAverage\tResult")    
for i in range(4):
    print(f"{list_lessen[i]}\t{list_midterm[i]}\t{list_final[i]}\t{list_average[i]}\t{list_result[i]}")
print('*'*38)    
        



