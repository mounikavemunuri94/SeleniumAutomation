# look for examples
# https://www.programiz.com/python-programming/examples


#Python Program to Find the Square Root
num=8
square_value=8**0.5
print("square_value-->{0:0.2f}".format(square_value))
# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# Python Program to Calculate the Area of a Triangle
#s = (a+b+c)/2
#area = √(s(s-a)*(s-b)*(s-c))
a= 5
b = 6
c = 7
s=(a+b+c)/2
area_triangle=((s*(s-a)*(s-b)*(s-c))**0.5)
print("area of triangle-->{0:0.2f}".format(area_triangle))

# Python Program to Solve Quadratic Equation
# The standard form of a quadratic equation is:
#(-b+-(b**b-4a*c)**0.5)/2*a

a = 1
b = 5
c = 6
d = (b**2)-(4*a*c)
print("aaa", d)
so1=(-b+(d))/2*a
so2=(-b-(d))/2*a
print("sol1", so1)
print("so2", so2)


#Python Program to Swap Two Variables using temp
x=10
y=20
temp = x
x = y
y = temp
print("x value-->", x)
print("y value-->", y)

# Python Program to Swap Two Variables without using the third variable
x=10
y=20
x=x+y
y=x-y
x=x-y
print("x value-->", x)
print("y value-->", y)

# Python Program to Swap Two Variables without using the third variable
x=10
y=20
x=x^y
y=x^y
x=x^y
print("x value-->", x)
print("y value-->", y)

# Python Program to Generate a Random Number
import random
print(random.randint(10,20))

# Python Program to Convert Kilometers to Miles
# Taking kilometers input from the user
# kilometers = float(input("Enter value in kilometers: "))
# conversion_factor=0.621371
# #calculate miles
# miles = kilometers * conversion_factor
# print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

#(0°C × 9/5) + 32 = 32°F
# change this value for a different result
# Python Program to convert temperature in celsius to fahrenheit

celsius = 37.5
fahrenheit = (celsius+(9/5))+32
print("celsius to fahrenheit-->", fahrenheit)

celsius = (fahrenheit-32)/(9/5)
print("fahrenheit  to celsius -->", celsius)


# # Python Program to Check if a Number is Positive, Negative or 0
# num = int(input("Enter the number to check which is postive or negative"))
# print("numberrrr->", num)
# if num>=0:
#     if num==0:
#         print("Zero")
#     else:
#         print("positve")
# else:
#     print("negative number")
#
# # Python Program to Check if a Number is Odd or Even
# num=int(input("Enter the number to check it is odd or even"))
# print("number-->", num)
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# # Python Program to Check Leap Year
# year=int(input("enter the number to check it is a leap year or normal year"))
# print("yearrr", year)
#
# if year>0:
#     if year%400==0 and year%100==0:
#         print("Leap year")
#     elif year%4==0 and year%100!=0:
#         print("leap year")
#     else:
#         print("Not leap year")
#
# # Python Program to Find the Largest Among Three Numbers
# num1=int(input("enter first number"))
# num2=int(input("enter first number"))
# num3=int(input("enter first number"))
# if num1>num2:
#     if num1>num3:
#         big=num1
#     else:
#         big=num3
# elif num2>num3:
#     big=num2
# else:
#     big=num3
# print("Big number is-->", big)

# def isPrime(num):
#     flag=0
#     if num>0:
#         for i in range(2, num):
#             if num%i==0:
#                 flag=1
#                 break
#     else:
#         print("Negative numbers")
#     return flag
#
# # Python Program to Check Prime Number
# num=int(input("Enter the number to check prime number"))
# print("number-->", num)
# flag=0
# if num>0:
#     for i in range(2, num):
#         if num%i==0:
#             flag=1
#             break
# if flag!=1:
#     print("It is prime number")
# else:
#     print("not a prime number")


# # Python Program to Print all Prime Numbers in an Interval
# lower=int(input("enter the minum interval"))
# upper=int(input("enter the maximum interval"))
# for num in range(lower, upper+1):
#     if(isPrime(num))!=1:
#         print(num)
#     # else:
#     #     print("Not a prime")
#
# # Python Program to Find the Factorial of a Number
# num=int(input("enter the number to find out the factorial of number"))
# fact = 1
# if num<0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num+1):
#         fact*=i
#     print("factorial of number--->", fact)
# # Factorial of a Number using Recursion
# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x*factorial(x-1)
# print(factorial(6))

# Python Program to Display the multiplication Table
# num=12
# for i in range(1, 10+1):
#     print(" {0} * {1} = {2}".format(num, i, num*i))
#
# # Python Program to Print the Fibonacci sequence
# a = 0
# b = 1
# num=int(input("enter the number for fibonassic"))
# print("fibonacci", num)
# print(a)
# print(b)
# while((a+b)<num):
#     b=a+b
#     a=b-a
#     print(b)
#
# # python program to print the fibonacci sequence
# n1=0
# n2=1
# count=0
# nterms=int(input("Enter the number of terms"))
# if nterms<=0:
#     print("Please enter the positive number")
# elif nterms==1:
#     print("Fibonacci sequence upto", nterms, ":")
#     print(n1)
# else:
#     print("Fibonacci series-->")
#     while count<nterms:
#         print(n1)
#         nth=n1+n2
#         n1=n2
#         n2=nth
#         count+=1
# Python Program to Check Armstrong Number
def digCount(num):
    count=0
    while num:
        count+=1
        num//=10
    return count
def orderOfDigit(digit, countOfnum):
    mul=1
    for i in range(0, countOfnum):
        mul*=digit
    print(mul)
    return mul

# def isArmStrong(num):
#     count=digCount(num)
#     # print(count)
#     temp=num
#     sum=0
#     while temp:
#         digit = temp % 10
#         sum += digit ** count
#         temp //= 10
#     if sum==num:
#         return True
#     else:
#         return False
#
# num=int(input("Enter the number"))
# print("number-->", num)
# if(isArmStrong(num)):
#     print("ArmStrong")
# else:
#     print("Not a ArmStrong")
#
# # Python Program to Find Armstrong Number in an Interval
# lower=int(input("Enter the minum interval"))
# upper=int(input("Enter the maximum interval"))
# for num in range(lower, upper):
#     if(isArmStrong(num)):
#         print(num)

# Python Program to Find the Sum of Natural Numbers
# num=int(input("enter the number to find the sum of natural numbers"))
# sum=0
# temp=num
# while temp:
#     sum+=temp
#     temp-=1
# print("sum of natural numbers-->", sum)


# Program to print half pyramid using *
# n=int(input("Enter the number of lines to print"))
# for i in range(n):
#     for j in range(i+1):
#         print("* ", end='')
#     print("\n")
#
# # Program to print half pyramid a using numbers
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end='')
#     print("\n")
#
# # Program to print half pyramid using alphabets
# char = 'A'
# for i in range(n):
#     val=ord(char)+i
#     for j in range(i+1):
#         print(chr(val), end='')
#     print("\n")
#
# #  Inverted half pyramid using *
# for i in range(n):
#     for j in range(i, n):
#         print(" *", end='')
#     print("\n")
#
# # Inverted half pyramid using numbers
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print("\n")
#
# #  Program to print full pyramid using *
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print("\n")
#
#
# # Python Program to Reverse a Number
# num=int(input("Enter the number to reverse "))
# print(num)
# temp=num
# reverse_num=0
# number=''
# while temp:
#     digit=temp%10
#     reverse_num= reverse_num*10+digit
#     temp//=10
# print("number", reverse_num)

# Python Program to Find Numbers Divisible by Another Number
num=13
list_nums= [12, 65, 54, 39, 102, 339, 221,]
for i in list_nums:
    if i%num==0:
        print(i)

divisible_numbers=list(filter(lambda x:(x%13==0), list_nums))
print("divisible", divisible_numbers)