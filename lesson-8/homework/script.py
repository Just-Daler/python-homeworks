#1. Handle ZeroDivisionError
try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
#2. Raise ValueError for Invalid Integer
try:
    num = input("Enter an integer: ")
    if not num.isdigit():
        raise ValueError("Invalid integer input.")
    num = int(num)
    print("You entered:", num)
except ValueError as e:
    print("Error:", e)
#4. Raise TypeError for Non-Numeric Input
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.replace(".", "", 1).isdigit() and b.replace(".", "", 1).isdigit()):
        raise TypeError("Inputs must be numeric.")
    result = float(a) + float(b)
    print("Sum:", result)
except TypeError as e:
    print("Error:", e)
#5. Handle PermissionError
try:
    with open("/root/protected.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Error: Permission denied.")
#6. Handle IndexError
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")

#7. Handle KeyboardInterrupt
try:
    num = input("Enter a number (Ctrl+C to cancel): ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

#8. Handle ArithmeticError
try:
    x = 1 / 0
except ArithmeticError:
    print("Error: Arithmetic operation failed.")
#9. Handle UnicodeDecodeError
try:
    with open("some_file.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Cannot decode file content with ASCII encoding.")
#10. Handle AttributeError
my_list = [1, 2, 3]
try:
    my_list.push(4)  # push() doesn't exist for lists
except AttributeError:
    print("Error: This attribute/method does not exist for the object.")
#11. Read an entire text file
with open("sample.txt", "r") as f:
    print(f.read())
#12. Read first n lines of a file
n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")
#13. Append text to a file and display it
with open("sample.txt", "a") as f:
    f.write("\nNew line added.")
with open("sample.txt", "r") as f:
    print(f.read())
#14. Read last n lines of a file
n = 2
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))
#15. Read line by line into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)
#16. Read line by line into a variable
content = ""
with open("sample.txt", "r") as f:
    for line in f:
        content += line
print(content)
#17. Read file into an array (same as list in Python)
with open("sample.txt", "r") as f:
    arr = f.readlines()
print(arr)
#18. Find the longest words
with open("sample.txt", "r") as f:
    words = f.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
#19. Count number of lines
with open("sample.txt", "r") as f:
    print("Number of lines:", sum(1 for _ in f))
#20. Count frequency of words
from collections import Counter
with open("sample.txt", "r") as f:
    words = f.read().split()
print(Counter(words))
#21. Get file size
import os
print("File size:", os.path.getsize("sample.txt"), "bytes")
#22. Write a list to a file
data = ["apple", "banana", "cherry"]
with open("list.txt", "w") as f:
    for item in data:
        f.write(item + "\n")
#23. Copy file contents
with open("sample.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())
#24. Combine each line from two files
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for a, b in zip(f1, f2):
        print(a.strip(), b.strip())
#25. Read a random line
import random
with open("sample.txt", "r") as f:
    print(random.choice(f.readlines()))
#26. Check if file is closed
f = open("sample.txt", "r")
print(f.closed)
f.close()
print(f.closed)
#27. Remove newline characters
with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)
#28. Count words in a file
with open("sample.txt", "r") as f:
    text = f.read().replace(",", " ")
print("Word count:", len(text.split()))
#29. Extract characters from files into a list
files = ["file1.txt", "file2.txt"]
chars = []
for filename in files:
    with open(filename, "r") as f:
        chars.extend(list(f.read()))
print(chars)
#30. Generate A.txt to Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is {letter}.txt\n")
#31. Write alphabet with N letters per line
import string
n = 5
letters = string.ascii_lowercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write(letters[i:i+n] + "\n")
