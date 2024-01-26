# Question 1 : Write a Python code that prints the numbers from 1 to 10 on the screen
# Soru 1 : 1'den 10'a kadar olan sayıları ekrana yazdıran bir Python kodu yazınız.

i = 1

while i <= 10:
  print(i)
  i += 1

# Question 2 : Take input from the user and write a Python program that prints even numbers up to that input. Do this first using a 'for' loop and then using a 'while' loop.
# Soru 2 : Kullanıcıdan bir sayı girişi alın ve bu sayıya kadar olan çift sayıları ekrana yazdıran bir Python programı yazın. Bunu once 'for' ile sonra 'while' donguleri ile yapiniz. 

#FOR LOOP
number = int(input("Please enter a positive number:"))

if number <= 0:
  print("Sorry, you entered a negative number")
else:
  print(f"Even Numbers with a For Loop (0-{number}):")
  for i in range(0, number+1):
    if i %2 == 0:
      print(i)

#WHILE LOOP
number = int(input("Please enter a positive number:"))

if number <= 0:
  print("Sorry, you entered a negative number")
else:
  print(f"Even Numbers with a For Loop (0-{number}):")
  i=0
  while i<= number:
    if i %2 == 0:
      print(i)
    i += 1

# Question 3 : Write a Python code that takes starting and ending values from the user and prints all the numbers between these values (including the ending value) on the screen.
# Soru 3 : Kullanıcıdan bir başlangıç ve bitiş değeri alan ve bu değerler arasındaki tüm sayıları ekrana yazdıran bir Python kodu yazınız(bitis degeri dahil).
    
first_number = int(input("Enter the starting number"))
last_number = int(input("Enter the ending number"))

if first_number > last_number:
  i = -1 #decreasing order
else:
  i = 1 #ascending order

print(f"All numbers between {first_number} to {last_number}")
x = first_number
while x != last_number + i:
  print(x)
  x += i

# Question 4 : Take input from the user and write a Python code that prints whether the given number is odd or even on the screen.
# Soru 4 : Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir Python kodu yazınız.

number = int(input("Enter a number: "))

if number %2 == 0:
  print(f"{number} is an EVEN NUMBER.")
else:
  print(f"{number} is an ODD NUMBER.")

#Question 5 : Take input from the user for a positive integer and write a Python program that calculates its factorial. Factorial is the product of all positive integers from 1 to the given number, inclusive.
# Soru 5 : Kullanıcıdan pozitif bir tam sayı girişi alın ve faktöriyelini hesaplayan bir Python programı yazın. Faktöriyel, bir sayının kendisi ile 1 arasındaki tüm pozitif tam sayıların çarpımıdır.
  
while True:
  #Take input for a positive integer from the user
  number = input("Enter a number:")

  #Check if the input is a positive integer
  while not number.isdigit() or int(number) <= 0:
    print("Invalid input. Please enter a positive integer.")
    number = input("Enter a number:")

  #The entered value is a positive integer
  x = int(number)

  #Create a variable to calculate the factorial and initialize it to 1
  factorial = 1

  #Multiply positive integers from 1 to the number to calculate the factorial
  for i in range(1, x+1):
    factorial *= i

  #Print the result
  print(f"Factorial: {factorial}")

  #Exit the loop
  break

# Question 6 : Write a Python code that takes input from the user and checks whether the given number is prime or not.
# Soru 6 : Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazınız.

def is_prime(x):
  if x < 2:
    return False
  for i in range (2, x):
    if x %i == 0:
      return False
  return True

x = int(input("Enter a number: "))
if  is_prime(x):
  print(f"{x} is A PRIME NUMBER.")
else:
  print(f"{x} is NOT A PRIME NUMBER.")

# Question 7 : How can a loop be created to calculate the Fibonacci sequence and return the result as a list containing numbers up to a specific limit?
# Soru 7 : Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları içeren bir liste olarak döndüren bir döngü nasıl oluşturulur? 
  
limit = int(input("Enter a limit for the Fibonacci sequence: "))
fibonacci_list = [0, 1]

while True:
  new_term = fibonacci_list[-1] + fibonacci_list[-2]
  if new_term <= limit:
    fibonacci_list.append(new_term)
  else:
    break

print(f"Fibonacci sequence (0 to {limit}):")
print(fibonacci_list)

# Question 8 : Write a Python code that takes a word from the user and prints its reverse on the screen.
# Soru 8 : Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazınız.

word = input("Enter a word: ")

reversed_word = ""
for i in range(len(word)-1, -1, -1):
  reversed_word += word[i]

print(f"Reverse of the entered word: {reversed_word}")

# Question 9 : How can a loop and a combination of conditional expressions be created to take input of a word from the user and check if the word is a palindrome (reads the same backward as forward)?
# Soru 9 : Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom (tersten okunduğunda aynı olan) olup olmadığını kontrol eden bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?

word = input("Enter a word: ")
reversed_word = word[::-1]

if word == reversed_word:
  print(f"{word} is A PALINDROME.")
else:
  print(f"{word} is NOT A PALINDROME.")

# Question 10 : Write a code that calculates an individual's body mass index (BMI) and returns the result as underweight, normal, overweight, or obese based on the BMI value. To do this, ask the user for weight and height measurements. Use the following BMI categories:
# If BMI is below 25, classify as "Underweight."
# If BMI is between 25 and 30, classify as "Normal."
# If BMI is greater than or equal to 30 and less than 40, classify as "Overweight."
# If BMI is greater than or equal to 40, classify as "Obese."
  
#Soru 10 : Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.(kilo indeks hesabı için internete bakabilirsiniz) 
#Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz. Kilo indeksi 
#25’in altında ise zayıf, 
#25-30 arasında ise normal, 
#30-40dan büyük ise kilolu, 
#40tan büyük ise aşırı kilolu sonuçlarına varsın.
  
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

n = weight / ((height ** 2) / 10000)
print(f"Body Mass Index: {n:.1f}")

if n < 25:
  print("Underweight")
elif n < 30:
  print("Normal")
elif n < 40:
  print("Overweight")
else:
  print("Obese")

# Question 11 : How can a Python program be written to find the largest of three numbers entered by a user?
# Soru 11 : Bir kullanıcının girdiği üç sayının en büyüğünü bulan bir Python programı nasıl yazılır?
  
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

largest_number = n1

if n2 > largest_number:
  largest_number = n2

if n3 > largest_number:
  largest_number = n3

print(f"The largest number is: {largest_number}")

# Question 12 : Take midterm and final grades from a student for any course. The sum of 40% of the midterm grade and 60% of the final grade will give the year-end average. If the average is below 50, print "UNSUCCESSFUL" on the screen; if 50 or above, print "SUCCESSFUL". This printing process will be repeated for 4 courses, and the results will be displayed one after another.
# Soru 12 : Bir ogrenciden herhangi bir ders icin Vize ve Final notlarıni alin. Ara sınav notunun %40'ı ile final notunun %60'ının toplamı yıl sonu ortalamasını verecektir. Ortalama 50'nin altında ise ekranda “BAŞARISIZ”, 50 ve üzerinde ise “BAŞARILI” çıktısı ekrana gelecektir. Bu baskı işlemi 4 derstir. yapılacak ve dersler birbiri ardına yazılacaktır.

for lesson in range (1, 5):
  print(f"\n Lesson {lesson}")

  midterm_grade = float(input("Enter the midterm grade: "))
  final_grade = float(input("Enter the final grade: "))

  year_end_average = (midterm_grade * 0.4) + (final_grade * 0.6)

  if year_end_average >= 50:
    status = "SUCCESSFUL"
  else:
    status = "UNSUCCESSFUL"
  
  print(f"Year-End Average: {year_end_average:.1f}")
  print(f"Success Status: {status}")