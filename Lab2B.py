##
# Michael Forsythe & Matthew Womack
# Lab 2 Part B Task 1
# Find errors for code fragments and fix them
##

# display on the console the initials (that is, first letter of each part) of
# the person’s name
first = "Buster"
middle = "G"
last = "Bunny"
print(first[0] + middle[0] + last[0]) #runtime error, changed middle and last brackets to 0

# display on the console all the parts of a person's name with no spaces
# between the parts and with the cursor afterwards on the next line
first = "Babs"
middle = "A"
last = "Bunny"
print(first + middle + last) 
#syntax error, the variables are spelled incorrectly 

# display all the parts of a person's name on the console with one blank
# character between
# each part and with the cursor afterwards on the next line
first = "Wile"
middle = "E"
last = "Coyote"
print(first, middle, last) 
# syntax error, there is no comma after middle variable is called

# display on the console the parts of a person's name with one space in
# between the parts and with string "FOOOM" on the same line and at the end
# and with the cursor afterwards at the start of the next line
end = "FOOOM\n"
first = "Hamilton"
middle = "J"
last = "Pig"
print(first, middle, last, end)
# logic error, end variable was not called

# display on the console the values of the variables named first and last in
# order with a space in between them and the cursor afterwards at the start
# of the second line below
first = "Fifi"
last = "La Fume"
print(first, last, end = "\n\n")
# syntax error, end variable must be defined in a string

# display on the console the values of the variables first and line in order
# with a space in between them and the cursor afterwards at the start of
# the second line below
first = "Calamity"
last = "Coyote"
print(first, last, end = "\n\n")
# syntax error, end variable must be on left side

import math
radius = 3
circle_area = math.pi * radius ** 2

base = 12
height = 11
triangle_area = 1/2 * (base * height)



