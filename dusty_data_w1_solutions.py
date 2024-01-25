# question1

for i in range(1,10):
    print(i)

# question2

#for

number = int(input(f"Enter a number: "))

print(f"For loop even numbers till your choose:")
for i in range(number+1):
    if i % 2 == 0:
        print(i)

#while

number = int(input(f"Enter a number: "))

print(f"For loop even numbers till your choose:")
for i in range(number+1):
    if i % 2 == 0:
        print(i)

# question3

begin_number = int(input("Enter a begin number:"))
end_number = int(input("Enter an end number:"))

for i in range(begin_number+1,end_number):
    print(i)

# question4

number = int(input("Enter a number that you want to learn odd/even:" ))

if number % 2 == 0:
    print(f"The number that you entered is an even number.")
else:
    print(f"The number that you entered is an odd number.")


# question5

number = int(input("Enter a positive number:"))

faktorial = 1

for i in range(1,number+1):
    faktorial *= i
    
print (f"faktorial of {number} is {faktorial}")

# question 6

number = int(input("Enter a number that you want to check that is a prime number: "))

if number < 2:
    print(f"The number {number} that you enter is not a prime number.")

else:
    for i in range(2, number):
        if number % i == 0:
            print(f"The number {number} that you enter is not a prime number.")
            break

        else:
            print(f"The number {number} that you enter is a prime number.")
            break

# question 7

limit = int(input("How many fibonacci number do you want to see? "))
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(limit-2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

# question 8

word = str(input("Write a word that you want to see reversed: "))
print(word[::-1])

# question 9

word = input("Enter a word that you want to check that is same with the reversed or not: ")

reversed_word = word[::-1]

if reversed_word == word:
    print(f"The reversed of {word} is the same.")
else:
    print(f"Find another word. The {reversed_word} is different than {word}.")

# question 10

height = float(input("Enter your height(Ex:1.72): "))
weight = float(input("Enter your weight(Ex:74.4): "))
BMI = weight/height**2


if BMI >= 30:
    print(f"Your body mass index is {BMI}, you have obesity.")
elif BMI >= 25:
    print(f"Your body mass index is {BMI}, you are overweight.")
elif BMI > 18.5:
    print(f"Your body mass index is {BMI}, you have normal weight.")
else:
    print(f"Your body mass index is {BMI}, you are underwight.")


# question 11

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))

if n1 > n2 and n3:
    print(n1)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)

# question 12

for i in range(4):

    visa_grade = float(input(f"Enter {i + 1}. lesson visa grade(Ex.:71.5): "))
    final_grade = float(input(f"Enter {i + 1}. lesson final grade(Ex.:66.4): "))
    avg_end_grade = (visa_grade*0.4) + (final_grade*0.6)

    if final_grade <= 50:
        print(f"{i + 1}. ders BAŞARISIZ")
    else:
        print(f"{i + 1}. ders BAŞARILI")


