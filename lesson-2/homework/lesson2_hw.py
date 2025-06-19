#1- Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
from datetime import datetime
a = int(input('your year of birth:'))
b = input('your name:')
c=datetime.now().year-a
z = 'Your name is {} and your age is {}'.format(b,c)
print(z)

#2-Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[1:2]+txt[7:9]+txt[4:5]+txt[-2:-3]+txt[-2:-1]+txt[-4:-3]+txt[-1:]+txt[4:5]+txt[-1:])
print(txt[-3:-2]+txt[6:7]+txt[4:6]+txt[2:3])
print(txt[4:5]+txt[6:7]+txt[2:3]+txt[-3:-2])

#3-Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[:1]+txt[2:3]+txt[-2:-1]+txt.lower()[-1:]+txt[2:3])
print(txt[-1:]+txt[2:3]+txt[4:5]+txt[1:2])




#4-Extract the residence area from the following text:
txt = "I'am John. I am from London"
print(txt[(txt.find('London')):])

#5-Write a Python program that takes a user input string and prints it in reverse order.
a=input('write word: ')
print(a[::-1])

#6-Write a Python program that counts the number of vowels in a given string.
a= input('write your word : ')
volves ='aeiou'
counted = sum(1 for char in a if char in volves)
print(counted)

#7-Write a Python program that takes a list of numbers as input and prints the maximum value.
a=input("input numbers with space between").split()
a= [int(num) for num in a]
print(max(a))

#8-Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
c=input('write anybody:')
if c[::-1]==c:
    print('palindrome')
else:
    print('not palindrome')

#9-Write a Python program that extracts and prints the domain from an email address provided by the user.
a=input('write email adress: ')
b=int(a.find('@')+1)
print('domen is: ', a[b:])

#10-Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string
password_length = 15
words = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(words) for _ in range(password_length))
print(' generated password is: ', password)
