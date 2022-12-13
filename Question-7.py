Question :

Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list. If the second string is not present in the first string then it should return -1.

CODE :
def indices(first, second):
    for i in second:
        if i in first:
            print(test1.index(i))
        if i not in first:
            print(-1)


test1 = input("Enter the first string:\n")
test2 = input("Enter the second string:\n")
indices(test1, test2)

OUTPUT :
Enter the first string:
hello
Enter the second string:
he
0
1