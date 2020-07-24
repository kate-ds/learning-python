"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
try:
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        content: list = f.readlines()

    for i in range(0, len(content)):
        if "One" in content[i]:
            content[i]: str = content[i].replace("One", "Один")
        elif "Two" in content[i]:
            content[i] = content[i].replace("Two", "Два")
        elif "Three" in content[i]:
            content[i] = content[i].replace("Three", "Три")
        elif "Four" in content[i]:
            content[i] = content[i].replace("Four", "Четыре")
except IOError:
    print("Error!")
with open("dictionary1.txt", "w", encoding="utf-8") as f:
    f.writelines(content)
