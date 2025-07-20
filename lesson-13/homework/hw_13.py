from datetime import datetime,date,timedelta

# 1----Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
b_date_inp =input("enter birth date:day/month/year: ")
d= datetime.strptime (b_date_inp, "%d/%m/%Y").date() # Strptime execute datetime from str
delta = date.today()-d # deltatime returns days and times
print(f"Your age is {delta.days//365} ,{delta.days//30} month, {delta.days} days") # prints age in years ,month, and days

# second solove way
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# Ask for birthdate
b_date_inp = input("Enter birth date (day/month/year): ")
d = datetime.strptime(b_date_inp, "%d/%m/%Y").date()

# Calculate difference using relativedelta
diff = relativedelta(date.today(), d)

# print(f"Your age is {diff.years} years, {diff.months} months, and {diff.days} days.")


#2--Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

today =date.today()     # return date today
ure_b1 =input("enter birth date:day/month/year: ")    # enter ur'e birthday 
ure_b2= datetime.strptime (ure_b1, "%d/%m/%Y").date() # Strptime execute datetime from str 
this_y = date(year = today.year, month=ure_b2.month,day=ure_b2.day) #return ur'e BD in this year

if this_y<today:
    next_b = date(year = today.year+1, month=ure_b2.month,day=ure_b2.day)
else: next_b = this_y

print(f"days remaining {next_b-today}")



today =date.today()     # return date today
ure_b1 =input("enter birth date:day/month/year: ")    # enter ur'e birthday 
ure_b2= datetime.strptime (ure_b1, "%d/%m/%Y").date() # Strptime execute datetime from str 
next_bd = date(year=(today.year),month=ure_b2.month,day=ure_b2.day)
if today>=ure_b2:
    next_bd = date(year=(today.year+1),month=ure_b2.month,day=ure_b2.day)
    print(next_bd-today)
else :  print(next_bd-today)
     
#3-Meeting Scheduler: Ask the user to enter the current date and time,
#  as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

curdatetime =input("enter curdate date:day/month/year/Hour/Min: ")    # enter current date time
duration_m = input("Enter duration of a meeting Hour/Min: ")      # Enter duration of a meeting
dt = datetime.strptime(curdatetime, "%d/%m/%Y/%H/%M")
ddt = datetime.strptime(duration_m,"%H/%M")
dif = timedelta(hours=ddt.hour,minutes=ddt.minute)
print(f"meeting will be ended at {dt+dif}")



"""4-Timezone Converter: Create a program that allows the user to enter a date and 
time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
"""
from datetime import datetime
import pytz

local = datetime.now()
print("local",local.srtftime("%m/%d/%Y,%H:%M:%S"))


"""5- Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, 
and then continuously print the time remaining until that point in regular intervals (e.g., every second).
"""
# time_out = input("enter future date and time: day/month/year/Hour/min/sec: ")
# c = datetime.strptime(time_out, "%d/%m/%Y/%H/%M/%S")
# delta_time = timedelta(hours=c.hour,minutes=c.minute,seconds=c.second)
# today = datetime.now()
# while today == (delta_time+today):
#     print(c)
#     c.second-1




    
# from datetime import datetime
# import time

# # Ask user for future date and time
time_out = input("Enter future date and time (day/month/year/hour/minute/second): ")
target = datetime.strptime(time_out, "%d/%m/%Y/%H/%M/%S")

while True:
    now = datetime.now()
    remaining = target - now

    if remaining.total_seconds() <= 0:
        print("Time's up!")
        break

    # Format remaining time as H:M:S
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Remaining: {remaining.days} days, {hours:02}:{minutes:02}:{seconds:02}", end="\r")
    
    time.sleep(1)  # wait 1 second

"""6-Email Validator: Write a program that validates email addresses.
 Ask the user to input an email address, and check if it follows a valid email format.
"""
import re 
in_email = input("Enter your email address:  " ) 
form = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(form,in_email):
    print("valid")
else: print("nonvalid")



"""7-Phone Number Formatter: Create a program that takes a phone number as input and formats
 it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
"""
import re 
numb = input("enter the tel number : ")
code = r"^(\d{3})(\d{3})(\d{4})"
match = re.match(code,numb)
print(f"({match.group(1)}) {match.group(2)}-{match.group(3)}")



"""8- Password Strength Checker: Implement a password strength checker. 
Ask the user to input a password and check if it meets certain criteria 
(e.g., minimum length, contains at least one uppercase letter, one lowercase letter, 
and one digit).
"""

import re
input_password = input("enter password: ")

if (
    len(input_password)>=8 and # checks min 8 length 
    re.search('[A-Z]',input_password) and  # searches uppercase letters
    re.search('[a-z]',input_password) and # serches lowercase letters
    re.findall('[0-9]',input_password) #searches digits
):
    print('your password acsepted!')
else : 
    print('Your password does not  follow the rules.')


"""9-Word Finder: Develop a program that finds all occurrences of a specific word in a given text. 
Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
"""
input_word = input("enter word to serch for: ")
input_text = input("enter your text: ")
cleaned = (f'\\b{input_word}\\b')
if True:
    print("there found words: ",len(re.findall(cleaned,input_text)))
else: print("no occurance word found")


"""10-Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, 
and then identify and print all the dates present in the text.
"""

from dateparser.search import search_dates

input_text = input("Enter text with dates: ")
results = search_dates(input_text)

if results:
    for match, dt in results:
        print(f"Found date: {match} ➤ {dt}")
else:
    print("No dates found.")

