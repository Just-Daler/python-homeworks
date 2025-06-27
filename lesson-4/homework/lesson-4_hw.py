#1 -Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict ={"num1":10,"num2":7,"num3":3,"num4":5,"num5":1}
print(sorted(my_dict.values(),reverse=True))  #descending
print(sorted(my_dict.values()))  #ascending
# 2-Write a Python script to add a key to a dictionary.
my_dict2 = {0: 10, 1: 20}
my_dict2.update([(2,30),(3,40)]) #first method
print(my_dict2)
my_dict2[4]=50 #second method
print(my_dict2)
#3-Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print(dic1|dic2|dic3)
#4- Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = int(input("number: "))
my_dic_n = {}

for i in range(1, n+1):
    my_dic_n[i] = i * i

print(my_dic_n)
#5-Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

my_task5 = {}

for i in range(1,16):
    my_task5[i]=i**2

print(my_task5)

# 6-Write a Python program to create a set.
my_set = {3,5,'joker',(7,8,9,0)}
print(my_set)
# 7-Write a Python program to iterate over sets.
for iterated in my_set:
    print(iterated)
#8 Write a Python program to add member(s) to a set.
my_set.update([5,4,6,7])
print(my_set)

#9 Write a Python program to remove item(s) from a given set.
my_set.discard(5) #third way to remove
print(my_set)
removing_elements={4,6,7}
my_set=my_set-removing_elements # 4 way to remove
print(my_set)

#10 Write a Python program to remove an item from a set if it is present in the set.
my_set.discard(5)
print(my_set)
