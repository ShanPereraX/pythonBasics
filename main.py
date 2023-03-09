# name = "123"
# print(len(name))  # length()
# print("Character index: " + str(name.find("S"))) #index
# print(name.capitalize()) #first letter Upper
# print(name.upper()) #all UPPER
# print(name.lower()) #all lower
# print(name.isdigit())  # check str is a digit
import math

# ------------------------------------------------------------------

# Type casting : data type of value -> another data type
#
# x = 5
# y = 2.5
# z = "3"
# # print("int : "+str(x))
# # print("float : "+str(y))
# # print("string : "+z)
#
# y = int(y)
# z = int(z)
#
# print(type(y))
# print(type(z))
#
# y = float(y)
# z = str(z)
#
# print(type(y))
# print(type(z))

# -----------------------------------------------------------------
# Key board input -> input()
#
# name = input("What is your name ? : ")
# age = int(input("How old are you ? : "))  # casting string -> int
#
# print("Hello " + name)
# print("You are " + str(age) + " years old")
#
# height = float(input("How tall are you ? : "))  # casting string -> float
# print("You are "+str(height)+"cm tall")

# -----------------------------------------------------------------
# math functions
#
# pi = 3.14
# #  print(round(pi))
# # print(math.ceil(pi))  # up round
# # print(math.floor(pi))  # down round
# # print(abs(pi))
# # print(pow(pi, 3))  # power
# # print(math.sqrt(9)) #squre root
#
# x = 1
# y = 2
# z = 3
#
# print("max : " + str(max(x, y, z)))  # max
# print("min : " + str(min(x, y, z)))  # min

# -----------------------------------------------------------------
# Slicing = create substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]
#                        step -> skips by step
#
# name = "Lakshan_Chamoditha"
#
# first_char = name[0]
# print(first_char)
#
# first_3_char = name[0:3]  # or name[:3]
# print(first_3_char)
#
# last_name = name[7:]
# print(last_name)
#
# funky_name = name[0:17:2]
# print(funky_name)
#
# reversed_name = name[::-1]
# print(reversed_name)
#
#
# # slice() -> same way (: -> ,)
# website = "https://google.com"
# slice = slice(7,-1)
# print(website[slice])
# -------------------------------------------------------------------------



# conditional statements
# if statement = a block of code that will execute if it's condition is true

age = int(input("input your age : "))
if age == 100:
    print("You are a century old ! ")
elif age >= 18:
    print("You are an adult ! ")
elif age <= 0:
    print("you haven't been born yet!")
else:
    print("You are a child ")
