Write a program to read a file and

a.) Print the total number of characters, words, and lines in the file.

b.) Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.

c.) Print the words in reverse order.

d.) Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’.

CODE :
file = open('test.txt', 'rt')
print('the original file is: ')
print(file.read())
file.close()

# a)
char_count = 0
words_count = 0
lines_count = 0

# characters count
file = open('test.txt', 'rt')
for line in file:
    for word in line:
        char = word.split()
        char_count += len(word)
print("the file has " + str(char_count) + " characters")
file.close()

# words count
file = open('test.txt', 'rt')
for line in file:
    words = line.split()
    words_count += len(words)
print("the file has " + str(words_count) + " words")
file.close()

# lines count
file = open('test.txt', 'rt')
for i in file:
    lines_count += 1
print("the file has " + str(lines_count) + " lines")
file.close()

# b)
freq_count = {}
file = open('test.txt', 'rt')
text = file.read()
for letter in text:
    if letter in freq_count:
        freq_count[letter] += 1
    else:
        freq_count[letter] = 1
print(freq_count)
file.close()

# c)
reversed_output = []
file = open('test.txt', 'rt')
correct_output = file.read()
for i in correct_output:
    reversed_output.append(i)
reversed_output.reverse()
reversed_output = [''.join(reversed_output)]
print(reversed_output)
file.close()

# d)
# copying the lines
file = open('test.txt', 'rt')
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
file.close()


# creating new files
# after creating the files once this block is not used again
# to create the files uncomment this block of code 
# file_1 = open('file1.txt', 'x')
# file_1.close()
# file_2 = open('file2.txt', 'x')
# file_2.close()



# appending the lines
file_1 = open('file1.txt', 'a')
file_1.write(line1)
file_1.write(line3)
file_1.close()
file_1 = open('file1.txt', 'r')
print(file_1.read())
file_2 = open('file2.txt', 'a')
file_2.write(line2)
file_2.close()
file_2 = open('file2.txt', 'r')
print(file_2.read())

OUTPUT :
the original file is: 
1. hey this is a test file
2. this contains a number of characters
3. this file is used for testing purposes only
the file has 113 characters
the file has 23 words
the file has 3 lines
{'1': 1, '.': 3, ' ': 20, 'h': 5, 'e': 9, 'y': 2, 't': 9, 'i': 9, 's': 12, 'a': 5, 'f': 4, 'l': 3, '\n': 2, '2': 1, 'c': 3, 'o': 5, 'n': 5, 'u': 3, 'm': 1, 'b': 1, 'r': 5, '3': 1, 'd': 1, 'g': 1, 'p': 2}
['ylno sesoprup gnitset rof desu si elif siht .3\nsretcarahc fo rebmun a sniatnoc siht .2\nelif tset a si siht yeh .1']
1. hey this is a test file
3. this file is used for testing purposes only

2. this contains a number of characters
