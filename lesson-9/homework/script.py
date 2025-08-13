#1. Circle Class

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
#2. Person Class

from datetime import date

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date  # format: (YYYY, MM, DD)

    def age(self):
        today = date.today()
        birth = date(*self.birth_date)
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

# Example
p = Person("Alice", "USA", (1995, 5, 20))
print(f"{p.name} is {p.age()} years old.")
#3. Calculator Class

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

# Example
calc = Calculator()
print(calc.add(10, 5))
print(calc.divide(10, 0))
#4. Shape and Subclasses

import math

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius**2
    def perimeter(self): return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side**2
    def perimeter(self): return 4 * self.side

# Example
shapes = [Circle(3), Triangle(3,4,5), Square(4)]
for s in shapes:
    print(f"{type(s).__name__} Area: {s.area()}, Perimeter: {s.perimeter()}")
#5. Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self): self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left: self._insert(node.left, value)
            else: node.left = Node(value)
        else:
            if node.right: self._insert(node.right, value)
            else: node.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node: return False
        if node.value == value: return True
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

# Example
tree = BST()
for val in [8, 3, 10, 1, 6]:
    tree.insert(val)
print(tree.search(6))
print(tree.search(7))
#6. Stack

class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None

# Example
s = Stack()
s.push(10)
s.push(20)
print(s.pop())
#7. Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example
ll = LinkedList()
ll.insert(3)
ll.insert(5)
ll.display()
ll.delete(3)
ll.display()
#8. Shopping Cart

class ShoppingCart:
    def __init__(self):
        self.items = {}  # {item: price}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# Example
cart = ShoppingCart()
cart.add_item("Book", 12.5)
cart.add_item("Pen", 1.5)
print(cart.total_price())
#9. Stack with Display

class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def display(self): print(self.items)

# Example
s = Stack()
s.push(5)
s.push(10)
s.display()
#10. Queue

class Queue:
    def __init__(self): self.items = []
    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None

# Example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
#11. Bank

class Bank:
    def __init__(self):
        self.accounts = {}  # {name: balance}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
            return True
        return False

    def check_balance(self, name):
        return self.accounts.get(name, "Account not found")

# Example
bank = Bank()
bank.create_account("Alice", 100)
bank.deposit("Alice", 50)
print(bank.check_balance("Alice"))
