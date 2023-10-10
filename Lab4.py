##
# Michael Forsythe & Mathhew Womack
# Lab 4
# Write for and while loops that output a set of values,
# initialize a countdown, and perform exponent calculations.
##

# problem a
for num in range(2, 9, 2):
    print(num)
print("\nWho do we appreciate?\n")

# problem a2
num = 2
while num < 9:
    print(num)
    num = num + 2
print("\nWho do we appreciate?\n")

# problem b
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
print("\nWho do we appreciate?\n")

# problem b2
num = 1
while num < 10:
    if num % 2 == 0:
        print(num)
    num += 1
print("\nWho do we appreciate?\n")

# problem c
start_value = int(input("Initialize Countdown: "))
for num in range(start_value, 0, -1):
    print(num, end = "...")
print("\nBLASTOFF!!")

# problem c2
countdown_start = int(input("Initialize Countdown: "))
while countdown_start > 0:
    print(countdown_start, end = "...")
    countdown_start -= 1
print("\nBLASTOFF!!")

# problem d
base = int(input("base: "))
exponent = int(input("exponent: "))
final_value = base
for num in range(1, exponent):
    final_value = final_value * base
print(final_value)

# poblem d2
base = int(input("base: "))
exponent = int(input("exponent: "))
final_value = base
num = 1
while num < exponent:
    final_value = final_value * base
    num += 1
print(final_value)

print("the name of this class is anthropology 1 whatever and its superrr boring xpppp")

input("a single letter, irregardless of case")
o = "a"
t = "e"
r = "a"
