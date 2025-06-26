# 1-Create a list containing five different fruits and print the third fruit.
fruits=['banana','apple','pineapple','watermelon','cherry']
print(fruits[2])  # Third fruit is at index 2

#2-Create two lists of numbers and concatenate them into a single list.
num1=[1,2,3,4]
num2=[5,6,7,8,9]
num1.extend(num2)  # 1- method to concatenate
print(num1)

num1=[1,2,3,4]
num2=[5,6,7,8,9]
combined=num1+num2  # 2- method to concatenate
print(combined)


#3-Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first = num1[0]
middle = num1[len(num1) // 2 - 1]
last = num1[-1]
stored_list = [first, middle, last]
print(stored_list)

# 4-Create a list of your five favorite movies and convert it into a tuple.
my_movies = ['interstellar','inception','fight club','breaking bad','john wick']
my_tuple = tuple(my_movies)
print(type(my_tuple))
# 5 Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["London", "New York", "Tokyo", "Berlin", "Paris", "Madrid"]
print(cities.index('Paris'))


#6 Create a list of numbers and duplicate it without using loops.
numbers = [1,2,3,4,5,6,7,8,9]
numbers_copy = numbers.copy()
print (numbers_copy)

#7 Given a list of numbers, swap the first and last elements.
numbers = [1,2,3,4,5,6,7,8,9]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)  # Output: [9, 2, 3, 4, 5, 6, 7, 8, 1]


#8 Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
tuple_numbers = (1,2,3,4,5,6,7,8,9,10)
print(tuple_numbers[3:7])

#9 Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "green", "blue", "yellow", "blue", "orange"]
print(colors.count("blue"))

#10 Given a tuple of animals, find the index of "lion".
animals = ("elephant", "tiger", "lion", "giraffe", "zebra")
print(animals.index("lion"))


#11 Create two tuples of numbers and merge them into a single tuple.
tup_num1 = (30,)
tup_num2 = (20,)
single_tup = tup_num1 + tup_num2
print(single_tup)


#12 Given a list and a tuple, find and print their lengths.
animals = ("elephant", "tiger", "lion", "giraffe", "zebra")
colors = ["red", "green", "blue", "yellow", "blue", "orange"]

print(len(animals))
print(len(colors))



#13 Create a tuple of five numbers and convert it into a list.
tuple_numbers = (1,2,3,4,5)
print(list(tuple_numbers))

#14 Given a tuple of numbers, find and print the maximum and minimum values.
random_nums = (40,50,23,10,3,99)
print(max(random_nums))
print(min(random_nums))


#15 Create a tuple of words and print it in reverse order.
animals = ("elephant", "tiger", "lion", "giraffe", "zebra")
print(animals[::-1])
