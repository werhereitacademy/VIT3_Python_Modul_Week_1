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
