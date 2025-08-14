import math

# ----------------- math_operations -----------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# ----------------- string_utils -----------------
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# ----------------- geometry.circle -----------------
def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

# ----------------- file_operations.file_reader -----------------
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."

# ----------------- file_operations.file_writer -----------------
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    return "File written successfully."

# ----------------- MAIN PROGRAM -----------------
if __name__ == "__main__":
    # Math operations
    print("Add:", add(5, 3))
    print("Subtract:", subtract(5, 3))
    print("Multiply:", multiply(5, 3))
    print("Divide:", divide(5, 3))

    # String utils
    print("Reverse:", reverse_string("Hello"))
    print("Vowel count:", count_vowels("Hello World"))

    # Geometry
    print("Circle Area:", calculate_area(5))
    print("Circle Circumference:", calculate_circumference(5))

    # File operations
    print(write_file("test.txt", "Hello from Python modules!"))
    print("File content:", read_file("test.txt"))
