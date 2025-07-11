#1 Task
def isyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

year = int(input("Yilni kiriting: "))
print(isyear(year))


#2 task
n = int(input("son kirirting: "))
if n<=0:
    print("Son manfiy bolishi kerak")
else:
    if n%2 !=0 :
        print("wierd")
    elif 2<n<5 :
        print("Not wierd")
    elif 6<n<20:
        print("Weird")
    elif n>20:
        print("Not Weird")
     
#3 task
a = int(input("a sonni kiriting: "))
b = int(input("b sonni kiriting: "))
# solution-1
if a > b:
    a, b = b, a

evens = list(range(a + (a % 2), b + 1, 2)) if a % 2 == 0 else list(range(a + 1, b + 1, 2))
print(evens)

#solution 2
print([x for x in range(min(a, b), max(a, b) + 1) if x % 2 == 0])
