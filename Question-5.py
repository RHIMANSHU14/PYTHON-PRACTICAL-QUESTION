Question :
 ??
Write a program to perform the following operations on a string:

a.) Find the frequency of a character in a string.

b.) Replace a character with another character in a string.

c.) Remove the first occurrence of a character from a string.

d.) Remove all occurrences of a character from a string.

CODE :
test = input("enter the string to perform the tasks \n")
element = input("enter the character to find its frequency \n")
freq = 0
for i in test:
    if i == element:
        freq += 1

print(freq)

# b)

test = list(test)

swap = input("enter the character to swap \n")
swap_with = input("enter the character to swap with \n")
i = int(test.index(swap))
j = int(test.index(swap_with))
test[i], test[j] = test[j], test[i]
print(''.join(test))

# c)

rem = input("enter the character to remove \n")
r = test.index(rem)
test.pop(r)
print(''.join(test))

# d)

rem_all = input("enter the character to remove all occurrence \n")
for a in test:
    if rem_all in test:
        test.remove(rem_all)
print(''.join(test))

OUTPUT :
enter the string to perform the tasks 
hello 
enter the character to find its frequency 
h
1
enter the character to swap 
e
enter the character to swap with 
l
hlelo 
enter the character to remove 
o
hlel 
enter the character to remove all occurrence 
l
he 