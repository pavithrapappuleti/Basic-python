PROGRAM 1: FIND THE TOTAL AND AVERAGE OF STUDENT MARKS

marks1 = int(input())
marks2 = int(input())
marks3 = int(input())
total=marks1+marks2+marks3
print("total:",total)
average = (marks1+marks2+marks3)//3
print("Average:",average)
if average >= 40:
    print("Result:Pass")
else:
    print("Result:Fail")

PROGRAM 2: FIND THE ELECTRICITY BILL THROUGH USER INPUT

data = int(input("Enter units: "))
if data<= 100:
    bill = data * 5
else:
    if data <= 200:
        bill = (100 * 5) + ((data - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((data - 200) * 10)

print("Electricity Bill =", bill)

PROGRAM 3: WITHDRAW AMOUNT AND SHOWING INSUFFICIENT BLANCE

acutalamount = int(input())
removeamount = int(input())
if removeamount <= acutalamount:
    availableamount = acutalamount - removeamount
    print("Available amount:",availableamount)
else:
    print("Insufficient Balance")

PROGRAM 4: DISPLAYING STUDENT GRADES

mark = list(map(int,input().split()))
total =0
for i in mark:
    total = total + i
average = total//len(mark)
print("Total;",total)
print("Average:",average)
if average>=90:
    print("Grade:A")
elif average >=75:
    print("Grade:B")
elif average >=75:
    print("Grade:B")
elif average >=60:
    print("Grade:C")
elif average >=60:
    print("Grade:D")
else:
    print("Fail") 

PROGRAM 5 : REVERSE OF A NUMBER

n = int(input()) 
rev = 0 

while (n>0):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)


PROGRAM 6 : COUNT NO.OF DIGITS AND COUNT OF EVEN AND ODD
n = input()
even = 0
odd = 0

for i in n:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Digits:", even)
print("Odd Digits:", odd)

PROGRAM 7 : USER LOGIN AND CREDENTIALS

un=input()
pwd=int(input())
if un == "admin" and pwd ==1234:
    print("Login succesful")
else:
    print("Invalid credentials")

PROGRAM 8 : SECRET NUMBER 

n = int(input())

if n == 25:
    print("correct")
elif n > 25:
    print("Too High")
else:
    print("Too Low")

PROGRAM 9 : PRODUCT DISCOUNT PROBLEM

p = input(" product : ")
q = int(input(" quantity: "))
price = int(input(" price: "))
d = int(input(" discount : "))

total = price * q

print("==== BILL ====")
print("Total:", total)
if total > 5000:
    dis = total * (d / 100)
else:
    dis = 0
    print("No discount")

print("Discount:", dis)

final = total - dis
print("Final Amount:", final)


PROGRAM 10 : ATM PROBLEM

balance = int(input("Enter Balance: "))
key = int(input("Press key value:"))

if key == 3:
    print("Balance:", balance)

elif key == 2:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Updated Balance:", balance)

elif key == 1:
    amount = int(input("Enter withdraw amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance")

elif key == 4:
    print("Exit")

else:
    print("Invalid Key")

PROGRAM 11 : PALINDROME CHECK

def palindrome(a):
    original = a
    reverse = 0

    while a > 0:
        digit = a % 10
        reverse = reverse * 10 + digit
        a = a // 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")

a = int(input("Enter a number: "))
palindrome(a)

PROGRAM 12 : FIND WHETHER LEAP YEAR OR NOT 

def leap_year(year):
    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not a Leap Year")
    elif year % 4 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")

year = int(input("Enter a year: "))
leap_year(year)
