Question :

Write a program that accepts a character and performs the following:

a.) print whether the character is a letter, numeric digit, or a special character.

b.) if the character is a letter, print whether the letter is uppercase or lowercase.

c.) if the character is a numeric digit, print its name in the text (e.g., if the input is 9, the output is NINE)

CODE :
test = input("Enter the test character: ")
# a)
if test.isalpha():
    print("The test character is a letter.")
elif test.isdigit():
    print("The test character is a numeric digit.")
elif test == ' ':
    print("The test character is whitespace.")
else:
    print("The test character is a special character.")

# b)
if test.isalpha():
    print("The test character is uppercase.") if test.isupper() else print("The test character is lowercase.")

# c)
out = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
       '8': 'eight', '9': 'nine', }
if test.isdigit():
    if test in out.keys():
        print(out[test])

OUTPUT :
for character:

Enter the test character: a
The test character is a letter.
The test character is lowercase.

for numeric digits:

Enter the test character: 9
The test character is a numeric digit. 
nine

for special characters:

Enter the test character: '
The test character is a special character.