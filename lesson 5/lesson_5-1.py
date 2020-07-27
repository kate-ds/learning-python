"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

from sys import stdin

with open("user_text.txt", "w", encoding="utf-8") as user_text:
    print("Enter file contents:")
    for line in stdin:
        # if line == " \n":
        if line.isspace():
            break
        user_text.write(line)

# -------------------------------------------------------------------------------------

print("Enter:")
user_input = ""
for line in stdin:
    user_input += line
    if line.isspace():
        break
print(user_input, end="\n")
with open("user_text.txt", "w", encoding="utf-8") as user_text:
    user_text.write(user_input[:-1])

# -------------------------------------------------------------------------------------

print("Enter:")
user_input: list = []
for line in stdin:
    user_input.append(line)
    if line.isspace():
        break

with open("user_text.txt", "w", encoding="utf-8") as f:
    f.write("".join(user_input[:-1]))


