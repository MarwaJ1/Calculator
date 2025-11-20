import math


def addition(x, y):
    return x + y 

def subratction(x, y): 
    return x - y 

def multiplication(x, y): 
    return x * y 

def divison(x, y): 
    return x / y 

def power_x(x, y):
    return x**y

def square(x): 
    return math.sqrt(x)

user_input = input("""Addition : a
Subtraction : s
Multiplication : m
Divison : d
Square : sq
To the power of x: p
 """)
    
if user_input.lower() == "a": 
    x = int(input("Add x")) 
    y = int(input("Add y"))
    print(addition(x, y))

elif user_input.lower() == "s": 
    x = int(input("Add x"))
    y = int(input("Add y"))    
    print(subratction(x, y))

elif user_input.lower() == "m": 
   x = int(input("Add x"))
   y = int(input("Add y"))
   print(multiplication(x, y))

elif user_input.lower() == "d": 
    x = int(input("Add x"))
    y = int(input("Add y"))
    print(divison(x, y))

elif user_input.lower() == "p": 
    x = int(input("Whats your base?"))
    y = int(input("Whats your exponent?"))
    print(power_x(x, y))

elif user_input.lower() == "sq": 
    x = int(input("What would you like to square?"))
    print(square(x))

else: 
    print("Entre a valid letter!!!")
    print("Addition : a ")
    print("Subtraction : s")
    print("Multiplication : m")
    print("Divison : d")
    print("Square : s")
    print("To the power of x: p")

