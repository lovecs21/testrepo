# to access other math function
from math import *

print('Hello World!')
# *************** variables ********
character_name = "ahmad"  # data type -> string
character_age = 15  # data type -> numbers
is_Male = True  # data type -> bool

# Working With Strings : in the string we can add "\n" -> which inserts a new line
# " \" " -> it adds a quotation mark.

print(character_name)
# dealing with numbers: any kind of arithmetic
print(3 + 4 * (5 - 1))
# converting a number to a string
num = -5
print(str(num) + " this is a number")
# common functions related to numbers
print(abs(num))
print(pow(5, 2))
print(max(5, 10), min(4, 3))
print(sqrt(36))
print(ceil(5.6))

# input from user
name = input("Enter your name: ")
print("Hello " + name + "!")

# calculator
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
result = float(num1) + float(num2)  # to covert it to a int cause it deals with them as strings
# other than int we can use flout to deal with decimal numbers other than whole number
print(result)

# Mad libs game
noun = input("Enter a noun")
name = input("Enter a name")
print("Yesterday, the giraffe ate a/an" + noun)
print("My dog licked" + name)
print("The mouse ran around" + noun)

A=['1','2','3']

for a in A:

  print(2*a)
