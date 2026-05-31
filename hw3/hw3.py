#3.4
for row in range(2):
    for col in range(7):
        print("@", end="")
    print()


#3.9
number = int(input("Enter a number 7 to 10 digits: "))

while number > 0:
    digit = number // (10 ** (len(str(number)) - 1))
    print(digit)
    number = number % (10 ** (len(str(number)) - 1))


#3.11
total_miles = 0
total_gallons = 0

gallons = float(input("Enter the gallons used (-1 to end): "))

while gallons != -1:
    miles = float(input("Enter the miles driven: "))

    mpg = miles / gallons
    print("The miles/gallon for this tank was", mpg)

    total_miles += miles
    total_gallons += gallons

    gallons = float(input("Enter the gallons used (-1 to end): "))

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print("The overall average miles/gallon was", overall_mpg)


#3.12
number = input("Enter a number: ")

backwards = ""

for i in range(len(number) - 1, -1, -1):
    backwards += number[i]

if number == backwards:
    print("palindrome")
else:
    print("not palindrome")


#3.14
pi = 4.0

first_314 = -1
first_3141 = -1

for i in range(1, 3001):
    term = 4 / (2 * i + 1)

    if i % 2 == 1:
        pi -= term
    else:
        pi += term

    print(i + 1, pi)

    if first_314 == -1 and str(pi).startswith("3.14"):
        first_314 = i + 1

    if first_3141 == -1 and str(pi).startswith("3.141"):
        first_3141 = i + 1

print("First iteration to reach 3.14:", first_314)
print("First iteration to reach 3.141:", first_3141)