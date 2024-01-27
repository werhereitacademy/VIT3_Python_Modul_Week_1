#Question 1:
#Write a Python code to print numbers from 1 to 10.

for i in range(1,11):
  print(i)



#Question 2
#Write a Python program that takes user input and prints all even numbers up to that input. Implement the program using both a for loop and a while loop.

#Code (using for loop):
number = int(input("Enter a number: "))

print(f"Even numbers up to {number}:")
for i in range(0, number+1, 2):
    print(i)

#Code (using while loop):
number = int(input("Enter a number: "))

print(f"Even numbers up to {number}:")
i = 0
while i <= number:
    print(i)
    i += 2

#Question 3
#Write a Python code that takes a starting and ending value from the user and prints all the numbers in between (inclusive).
start_value = int(input("Enter the starting value: "))
end_value = int(input("Enter the ending value: "))
print(f"All numbers between {start_value} and {end_value} (inclusive):")

while start_value <= end_value:
    print(start_value)
    start_value += 1


#Question 4
#Write a Python program that takes a number from the user and prints whether it is even or odd.

number = int(input("Enter your number:"))
while number >= 0:
   if number % 2 == 0:
       print("The entered number is even.")
       break
   else:
       print("The entered number is odd.")
       break



#Question 5
#Write a Python program that takes a positive integer input from the user and calculates its factorial.

positive_number = int(input("Enter a positive number:"))
factorial = 1
for i in range(1, positive_number + 1):
   factorial *= i
print(factorial)


#Question 6
#Write a Python code that takes a number from the user and checks whether it is a prime number.
while True:
    number = int(input("Enter a number:"))

    if number < 2:
        print(number, "is not a prime number.")

    else:
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                print(number, "is not a prime number.")
                is_prime = False
                break

        if is_prime == True:
            print(number, "is a prime number.")


#Question 7
#How can you create a loop that calculates the Fibonacci series and returns the result as a list containing numbers up to a certain limit?
#For example: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

limit = int(input("Up to which limit do you want to calculate the Fibonacci series? "))

fibonacci_series = [0, 1]

while fibonacci_series[-1] + fibonacci_series[-2] <= limit:
    new_term = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(new_term)

print(f"Fibonacci series up to {limit}: {fibonacci_series}")




#Question 8
#Write a Python code that takes a word from the user and prints its reverse.
while True:
    word = input("Enter a word:")
    reversed_word = word[::-1]
    letter_count = len(word)
    print("Reversed word:", reversed_word)
    print("Number of letters in the word:", letter_count)




#Question 9
#How can you create a loop and conditional statement combination to take a word input from the user and check whether it is a palindrome
#(reads the same backward as forward)?

while True:
    word = input("Enter a word:")
    reversed_word = word[::-1]

    if word == reversed_word:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")



#Question 10
#Write a code that calculates the body mass index (BMI) of a person and returns whether they are underweight, normal, overweight,
#or obese based on the BMI value. You can use the formula BMI = weight / (height in meters)^2. Ask the user for their weight and height in centimeters.

#If the BMI is below 25, it's considered underweight. If it's between 25 and 30, it's normal. If it's between 30 and 40,
#it's overweight. If it's above 40, it's considered obese.

weight = int(input("Please enter your weight in kilograms:"))
height = float(input("Please enter your height in centimeters:"))

height = height / 100
bmi = weight / (height * height)
print("Your BMI:", bmi)

if bmi < 25:
    print("Your result: 'Underweight'")
elif 25 <= bmi < 30:
    print("Your result: 'Normal'")
elif 30 <= bmi <= 40:
    print("Your result: 'Overweight'")
else:
    print("Your result: 'Obese'")



#Question 11
#How can a Python program be written to find the largest of three numbers entered by a user?
first_number = int(input("Please enter the first number:"))
second_number = int(input("Please enter the second number:"))
third_number = int(input("Please enter the third number:"))

number_list = [first_number, second_number, third_number]
number_list.sort()
print("The highest number you entered:", number_list[-1])


#Question 12
#Design a Python program to receive midterm and final grades from a student for any course. The final average will be calculated as 40% of the midterm grade
#and 60% of the final grade. If the average is below 50, it will display "FAIL", otherwise "PASS".
#This printing process will be repeated for 4 courses, and the courses will be written successively.

grades_list = []

def calculate_grade(midterm, final):
    average = (midterm * 0.4) + (final * 0.6)
    print(average)
    if average >= 50:
        return "PASS"
    elif average < 50:
        return "FAIL"

while len(grades_list) < 8:
    course_name = input("Course Name:")
    midterm_grade = float(input("Midterm Grade:"))
    final_grade = float(input("Final Grade:"))
    grades_list.append(course_name)
    grades_list.append(calculate_grade(midterm_grade, final_grade))

print(grades_list)












