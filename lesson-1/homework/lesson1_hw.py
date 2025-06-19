#--1_Given a side of square. Find its perimeter and area.
x = int(input('Eni:'))
y = int(input('bo"yi:'))
z = int(2 * (x+y))
print(z)

#--2_Given diameter of circle. Find its length.
import math
d = int(input('Diameterni kiriting:'))
l = int(math.pi * d)
print('bu aylana uzunligi:',l)

#--3_Given two numbers a and b. Find their mean
a = float ( input( 'a qiymatini kiriting:' ) )
b = float ( input( 'b qiymatini kiriting:' ) )
mean = float((a+b)/2)
print(mean)

#--4_Given two numbers a and b. Find their sum, product and square of each number.
a = float ( input( 'a qiymatini kiriting:' ) )
b = float ( input( 'b qiymatini kiriting:' ) )
sum = ('bu a va b ning yigindisi:',float(a+b))
kopaytma = ('bu a va b ning kopaytmasi:',float(a*b))
kvadrat = ('bu a va b ning kvadrati:',a**2,b**2)
print(sum,kopaytma,kvadrat)
