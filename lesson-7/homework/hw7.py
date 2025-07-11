#1 task
def is_prime(n):
    if 2>n:
        return False
    for i in range(2,n):
        if n %i ==0:
            return False
    return True
print(is_prime(int(input("son kirirting: "))))


#2 task
def digit_sum(i):
    total =0
    while i > 0:   # looping till i's ends number
        total += i%10 # summarize all i nums in to total
        i //=10
    return total
#3 
def daraj(i):
    k =1
    my_list = []
    while (2**k)< i:
        my_list.append(2**k)
        k +=1       
    return my_list
print(daraj(10))
