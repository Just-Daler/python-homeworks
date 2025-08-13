"""1- Given a string txt, insert an underscore (_) after every third character.
 If a character is a vowel or already has an underscore after it, shift 
 the underscore placement to the next character. No underscore should be added at the end."""

a = "abcabcabcdeabcdefabcdefg"
vowels = "aeiou"
my_txt = ""
i = 0

while i < len(a):
    chunk = a[i:i+3]
    if any(ch in vowels for ch in chunk) or (i > 0 and my_txt[-1] == "_"):
        # shift underscore after next char instead
        if i + 4 <= len(a):
            my_txt += chunk + a[i+3] + "_"
            i += 4
        else:
            my_txt += chunk
            break
    else:
        if i + 3 < len(a):
            my_txt += chunk + "_"
        else:
            my_txt += chunk
        i += 3
print(my_txt)



#2-The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
def square(n):
    return[i**2 for i in range(n)]

print(square(5))


#3-Print first 10 natural numbers using a while loop
i = 0
while i<10:
    print(i+1)
    i+=1

#4- Print the following pattern
a = []
for val in range(1,6):
    a.append(val)
    print(*a)

#5-Calculate sum of all numbers from 1 to a given number
a = int(input("enter the number:  "))
out = 0
for i in range(1,a+1):
    out+=i
print(f'sum is  {out}')

#6-Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

#7-Count the total number of digits in a number
number =  input("input a number: ").lstrip('-')
print(len(number))


#8-Print reverse number pattern
a = []
for i in range(5,0,-1):
    row = list(range(i,0,-1))
    a.append(row)
    print(row)

#9- Print list in reverse order using a loop


list1 = [10, 20, 30, 40, 50]

print(list1[::-1])

#10-Display numbers from -10 to -1 using a for loop
for i in range(-10,0):
    print(i)

#11-Display message “Done” after successful loop execution
number = int(input("input a number: "))
for i in range(0,number):
    print(i)
else: print('Done!')


#12- Print all prime numbers within a range
a = int(input("input first number: "))
b = int(input("input second number: "))
primes = []

for i in range(a, b + 1):
    if i > 1:  # primes are greater than 1
        for e in range(2, i):
            if i % e == 0:
                break
        else:
            primes.append(i)

print(primes)

#13-Display Fibonacci series up to 10 terms
fibonachi = [0,1,1,2]
first = fibonachi[-1]
second = fibonachi[-2]
while len(fibonachi)<10:
    fibonachi.append(fibonachi[-1]+fibonachi[-2])
print(fibonachi)

#14-Find the factorial of a given number
number = int(input("enter a number: "))
numbers =0
for i in range(1,number):
    number = number*i
print(number)
