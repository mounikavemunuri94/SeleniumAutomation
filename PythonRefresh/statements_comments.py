
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print("list-->", a)

# indentation
for i in range(1, 11):
     print(i)
     if i==5:
          break

if True:
    print('Hello')
    a = 5
if True:print("hello");a=5

# Docstrings in Python
def double_value(n):
     """ This function will use to double the value of number"""
     print("double value", n*2)
double_value(3)
print(double_value.__doc__)

# variables
webSite_name="google.com"
print("website name-->", webSite_name)

webSite_name = "yahoo.com"
print("website name-->", webSite_name)

#  Assigning multiple values to multiple variables
a, b, c = 10,11,12
print(a, b, c)

# we want to assign the same value to all three variables
a=b=c=100
print(a, b, c)


a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2

#Complex Literal
x = 3.14j+4

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
#Boolean literals
x = (1==True)
y = (1 == False)
a= True+4
b=False+10
print(x, y, a, b)



drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

# python numbers
a = 10
print("type of a", type(a))
b = 10.5
print("type of b", type(b))

c= 2+2j
print("complex numbers-->", c)
print("type of c", isinstance(c, complex))

# python list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("a-->", a[2])
print("slicing the items-->", a[5:])
print("first three items-->", a[0:3])

# python set
a ={5, 1, 3, 5, 6,7}
print(a)
print(type(a))
# Python Dictionary
d = {1: "mounika", 2: "manasa"}
print(a)

a=dict([[1,2],[3,4]])
print(a)

# python print statement
print(1,2,3,4)
print(1,2,3,4, sep='*')
print(1,2,3,4,sep='$', end='&')
print()

#Python Input
number=input("Enter the user input")
print(type(number))
print(type(int(number)))
# python import
import sys
print(sys.path)

# identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


# membership operators
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)



