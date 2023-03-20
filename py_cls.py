x = "THE FUN PART OF PROGRAMMING IS WRITING SYNTAX"

lenght = len(x)

print("The length is ", lenght)

py = 22/7
r = lenght*lenght

area = py * r

print("The Area Is",area)


#Number 2
import math

a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print('It should be more than 0')
else:

    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)

    print("The solutions are:")
    print("x1 =", x1)
    print("x2 =", x2)



