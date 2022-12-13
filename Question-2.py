Question :

Write a program to accept a number ‘n’ and check

a). Check if ’n’ is prime.

b). Generate all prime numbers till ‘n’.

c). Generate first ‘n’ prime numbers.

This program may be done using functions

CODE :
# a)
n = int(input("Enter the number to test."))
if n == 0 or n == 1:
    print("Enter a valid number.")
elif n == 2:
    print('The number is prime.')
for i in range(2, n):
    print("The number is not prime.") if n % i == 0 else print("The number is prime.")
    break

# b)
print("Prime numbers till " + str(n) + " are: ")
if n <= 2:
    print(2)
else:
    for i in range(2, n):
        if i > 2:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i, end=" ")
# c)
print("\nFirst " + str(n) + " prime numbers are: ")
count = 0
vals = 1
res = []
output = []
while count < n:
    if vals > 2:
        for nums in range(2, vals):
            if vals % nums == 0:
                break
        else:
            res.append(vals)
            # break
            count += 1
    vals += 1

for items in range(0, len(res)):
    if res[items] not in output:
        output.append(res[items])
print(str(output))

OUTPUT :
Enter the number to test.5
The number is prime.
Prime numbers till 5 are: 
3 
First 5 prime numbers are: 
[3, 5, 7, 11, 13]

