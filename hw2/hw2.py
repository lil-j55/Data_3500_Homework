# 2.3
grade = 91

if grade >= 90:
    print("Congratulations! Your grade of", grade, "earns you an A in this course")

# 2.4
print("Addition:", 27.5 + 2)
print("Subtraction:", 27.5 - 2)
print("Multiplication:", 27.5 * 2)
print("Division:", 27.5 / 2)
print("Floor Division:", 27.5 // 2)
print("Exponent:", 27.5 ** 2)

# 2.5
pi = 3.14159
radius = 2

diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2

print("Diameter:", diameter)
print("Circumference:", circumference)
print("Area:", area)

# 2.6
number = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# 2.7
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")

if 2 % 10 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")

# 2.8
print("number\tsquare\tcube")

for number in range(6):
    print(number, "\t", number ** 2, "\t", number ** 3)