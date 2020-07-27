"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""
from sys import exit

print("this program will generate a sequence of numbers and calculate their sum")
try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the last number: "))
except ValueError:
    print("Numbers should be only integers")
    exit(1)

with open("numbers.txt", "w", encoding="utf-8") as f:
    num: list = [str(i) for i in range(n1, n2) if i % 2 == 1]
    num: str = " ".join(num)
    f.write(num)

with open("numbers.txt", "r", encoding="utf-8") as f:
    numbers: str = f.read()
numbers_list: list = numbers.split(" ")

try:
    numbers_list: list = [int(i) for i in numbers_list]
    print(numbers_list)
    sum = 0
    for i in numbers_list:
        sum += i
    print("Sum: ", sum)
except ValueError:
    print("File should contain only numbers")
except IOError:
    print("File opening error!")




