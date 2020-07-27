string = input("Write a string: ")
string = string.split()
print(string)
for i, word in enumerate(string, 1):
    print(i, word[:10])
