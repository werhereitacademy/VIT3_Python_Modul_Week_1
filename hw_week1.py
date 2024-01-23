
print('1) Answer:\n_________')

for i in range(10):
    print(i + 1)

print('\n2) Answer:\n_________')

number = int(input('Enter a number!'))

print('2.1) \'for loop\' solution:\n')

for i in range(number + 1):
    if i % 2 == 0:
        print(i)

print('2.2) \'while loop\' solution:\n')

i = 0
while i <= number:
    if i % 2 == 0:
        print(i)
    i += 1

print('\n3) Answer:\n_________')

i = int(input('Input a starting value(Integer please!): '))
end_val = int(input('Input an ending value(Integer please!): '))
print(f'Numbers between {i} - {end_val} are: ')
if i < end_val:
    while i <= end_val:
        print(i)
        i += 1
elif i > end_val:
    while end_val <= i:
        print(i)
        i -= 1
else:
    print('The starting and ending values are the same and are ', i)

print('\n4) Answer:\n_________')

x = int(input('Write a number: '))
if x%2 != 0:
    print('The number you wrote is odd.')
else:
    print('The number you wrote is even.')

print('\n5) Answer:\n_________')

x = int(input('Write a positive number please: '))

while x < 0:
    x = (int(input('The number you entered is a NEGATIVE NUMBER!\nPlease enter a positive number!: ')))
    if x > 0:
         break

result = 1
i = 2
while i <= x:
    result *= i
    i += 1
print(f'Factorial of number {x} is: ', result)

print('\n6) Answer:\n_________')

x = int(input('Write a number: '))

if x < 0:
    print('Hello user, the number you entered is a NEGATIVE NUMBER! Prime numbers are counting numbers that have only two positive integer divisors. They are positive integers greater than 1 that can only be divided by themselves and 1 without remainder. Since prime numbers are defined this way, there cannot be a negative prime number.')
else:
    i = 2
    while i <= int(x//2 + 1):
        if x % i != 0 and i != int(x//2+1):
            i += 1
            continue
        elif i == int(x//2+1):
            print('Congratulations! you find a prime number!')
            i += 1
        else:
            print('The number you wrote is not a prime number!')
            break

print('\n7) Answer:\n_________')

entry = 1
limit = int(input("Enter the number that determines the upper limit in the Fibonacci sequence: "))
fibonacci =[0, 1]

while entry <= limit:
    fibonacci += [entry]
    entry = fibonacci[-1] + fibonacci[-2]

if limit != 0:
    print(f'The Fibonacci sequence, whose upper limit is determined by the number {limit}, is as follows:\n',fibonacci)
else:
    print('The Fibonacci sequence consists of at least 3 elements, so the upper bound should have been at least 1!') # Fibonacci dizisi en az 3 elemandan olusur, bu nedenle ust sinir en dusuk 1 olmaliydi!

print('\n8) Answer:\n_________')

string1 = input('Write a string: ')
string2 =''
for i in string1:
    string2 = i + string2
print(f'Opposite of your word is: \'{string2}\'')

print('\n9) Answer:\n_________')

string1 = input('Write a string: ')
j = -1
result = ''
for i in range(len(string1) // 2):
    if string1[i] == string1[j]:
        j -= 1
        result = f'The entered text \'{string1}\' is a palindrome text. :)'
    else:
        result = f'The entered text \'{string1}\' is not a palindrome text! :('
        break
print(result)

print('\n10) Answer:\n__________\n')

'Body Mass Index Calculation'
height = int(input('Enter your height as centimeters (cm): '))
weight = int(input('Enter your weight as kilogram (kg): '))

bmi = float(format(weight / (height/100)**2, '.2f'))
print(f'Result:\n_______\nYour BMI is {bmi}')
if bmi < 25:
    print('Under-weight')
elif 25 <= bmi < 30:
    print('Normal-weight')
elif 30 <= bmi < 40:
    print('Fat')
else:
    print('Over-weight')

print('\n11) Answer:\n__________\n')
numbers = []

for i in range(3):
    numbers.append(int(input('Enter a number: ')))
    print(f'Number {i+1}: ', numbers[i])

print(f'The biggest number in this list is {max(numbers)}')

print('\n12) Answer:\n__________\n')
ogrenci = []
course = {}
courses = ['Math', 'Science', 'Culture', 'English']
midterm = final = 0

for i in range(4):
    while True:
        midterm = int(input(f'Enter your midterm grade for the \"{courses[i]}\" course: '))
        if 0 <= midterm <= 100:
            break
    while True:
        final = int(input(f'Enter your final grade for the \"{courses[i]}\" course: '))
        if 0 <= final <= 100:
            break
    if (0.4 * midterm + 0.6 * final) < 50:
        result = 'Unsuccesful'
    else:
        result = 'Succesful'
    course = {'name':courses[i], 'midterm': midterm, 'final': final, 'result': result}
    ogrenci.append(course)

# Show them all
print('\n\n\nDetailed Results:\n_________________\n')

for i in range(len(ogrenci)):
    print(ogrenci[i]['name'] + ': ' + ogrenci[i]['result'] + '\nDetails:\nMidterm: ' + str(ogrenci[i]['midterm']) + ', Final: ' + str(ogrenci[i]['final']) + ', Average:' + str((ogrenci[i]['midterm']*0.4 + ogrenci[i]['final']*0.6)) + '\n')
