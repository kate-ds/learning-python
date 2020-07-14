string = input("Write a string: ")
string = string.split()
print(string)
for i, word in enumerate(string):
    print(i+1, word[:10])
