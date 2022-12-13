Ouestion :
Write a program to accept a name from a user. Raise and handle the appropriate exception(s) if the text entered by the user contains digits and/or special characters.

name = input('enter your name \n')
name.split()
c = 0
s = '"[@_!#$%^&*()<>?/\|}{~:]"'
for i in range(len(name)):
    if name[i] in s or name[i].isdigit():
        c += 1
if c == 0:
    print("your name is " + name)
else:
    try:
        raise Exception('Invalid character')
    except Exception as e:
        print('invalid character in your name', e



OUTPUT :
for valid input : 

enter your name 
Puneet
your name is Puneet

for invalid input :
enter your name 
$Puneet
invalid character in your name Invalid character