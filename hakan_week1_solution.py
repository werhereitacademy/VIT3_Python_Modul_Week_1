#soru1 cevabı
for i in range (1,11):
    print(i)
#soru2 cevabı
sayi = int(input("Bir sayı giriniz:"))
i=0
for i in range (sayi):
    if i % 2 == 0:
        i+=2
        print(i)

sayi = int(input("Bir sayı giriniz:"))
i=0
while i<sayi:
    if i % 2 == 0:

        print(i)
        i += 2
#soru3 cevabı
sayı1=int(input("sayı1 gırın:"))
sayı2=int(input("sayı2 gırın:"))
for i in range (sayı1,sayı2+1):
    print(i)
#soru4 cevabı
sayı=int(input("sayı gırın:"))
if sayı%2==0 :
    print("sayı cıft")
else:
    print("sayı tek")
#soru5 cevabı
faktorıyel=1
while True:
    sayı=int(input("bır sayı gırın:"))
    if (sayı<=0):
        print("pozıtıf sayı gırın")
    else:
        for i in range(1,sayı+1):
            faktorıyel*=i
        print("Faktorıyelımız",faktorıyel)
#soru6 cevabı

num_to_check = int(input("Enter a number to check for primality: "))


if num_to_check > 1:
    
    for i in range(2, int(num_to_check**0.5) + 1):
        if (num_to_check % i) == 0:
            print(f"{num_to_check} is not a prime number.")
            break
    else:
        print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")
#soru7 cevabı
limit = int(input("Enter the limit for the Fibonacci sequence: "))

fib_sequence = [0, 1]


while fib_sequence[-1] + fib_sequence[-2] <= limit:
    next_fibonacci = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fibonacci)

print("Fibonacci sequence up to", limit, ":", fib_sequence)
#soru8 cevabı
# Get input from the user
user_input = input("Enter a word: ")

# Reverse the word
reversed_word = user_input[::-1]

# Print the reversed word
print("Reversed word:", reversed_word)

#soru9 cevabı


# Get input from the user
user_input = input("Enter a word: ")

# Initialize a flag to check if it's a palindrome
is_palindrome = True

# Check for palindrome using a loop and conditional statement
for i in range(len(user_input)//2):
    if user_input[i] != user_input[-(i + 1)]:
        is_palindrome = False
        break

# Display the result
if is_palindrome:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")


#soru10 cevabı

kilo=float(input("kılonuz"))
boy=float(input("boyunuz"))
vkı=kilo/(boy*boy)
if vkı<25:
    print("zayıf")
elif 25<=vkı<30:
    print("orta")
elif 30 <= vkı < 40:
    print("kılolu")
else:
    print("asırı sısman")
  
#soru11 cevabı
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers to find the largest
if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
else:
    largest_num = num3

# Display the result
print("The largest number is:", largest_num)

#soru12 cevabı
# Loop for four lessons
for lesson in range(1, 5):
    print(f"\nLesson {lesson}:")

    # Get input from the user for midterm and final grades
    midterm_grade = float(input("Enter the midterm grade: "))
    final_grade = float(input("Enter the final grade: "))

    # Calculate the year-end average
    year_end_average = 0.4 * midterm_grade + 0.6 * final_grade

    # Check if the student is successful or failed
    result = "SUCCESSFUL" if year_end_average >= 50 else "FAILED"

    # Display the result for the current lesson
    print(f"Year-end average: {year_end_average:.2f}")
    print(f"Result: {result}\n")

print("Grading for all lessons completed.")

