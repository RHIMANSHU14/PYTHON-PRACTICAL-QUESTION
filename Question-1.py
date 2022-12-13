Question :

Write a program to find the roots of a quadratic equation in the form: ax^2 + bx + c = 0

CODE :
import cmath

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

# calculate the determinant
det = (b ** 2) - (4 * a * c)

# calculate solutions
sol1 = ((-b) - cmath.sqrt(det)) / (2 * a)
sol2 = ((-b) + cmath.sqrt(det)) / (2 * a)

print("The solutions of the quadratic equation are {0} and {1}".format(sol1, sol2))


OUTPUT :
Enter the value for a: 2
Enter the value for b: 1
Enter the value for c: 4
The solutions of the quadratic equation are (-0.25-1.3919410907075054j) and (-0.25+1.3919410907075054j)
