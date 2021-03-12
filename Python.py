#Group Member Names: Yasser, Ali, Yazed
#Emails: yassergithub1@gmail.com, aligithub1@gmail.com, yazedgithub1@gmail.com 


# a) Write a program containing a function to reverse a user inputted string.

string=input()
stringlength = len(string)
reversedString = string[stringlength::-1] 
print(slicedString)

# b) Write a program containing a function to check if a user inputted number is prime

num = int(input())
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")

# c) Write a program containing a function to convert the current time, into military time. 

import datetime
def timeconvert(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]
dt=datetime.datetime.now()
print("Conversion Of Time ::",timeconvert(dt.strftime("%H:%M:%S")))

# d) Write a program containing a function to output the fibonacci sum up to a user inputted number.

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# e) Write a program containing a function to check if a user inputted string is a good
#    password or not, if not have them try again. A password is considered good if it
#    contains at least 7 characters and 2 of those are either a number or special
#    character(by special character I mean any one of the characters on the numbers
#    1-8, i.e. !@#$%^&*).


import re
p= input("Input your password")
x = True
count = 0
if(len(p)>7):
    for i in range(len(p)):  
        if re.search("[0-9]",p):
            count += 1
        if re.search("[!@#$%^&*]",p):
            count += 1

    if(count >= 2):
        print("Valid Password")
        x = False
if x:
    print("Not a Valid Password")



