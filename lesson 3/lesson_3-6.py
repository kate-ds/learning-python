"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word: str) -> str:
# Replace first letter in a word to a capital one
    if 97 < ord(word[0]) < 122:
        word = chr(ord(word[0]) - 32) + word[1:]
        return word


def check_input(phrase: list) -> bool:
# Check if the text has capital letters
    for word in phrase:
        for letter in word:
            if 65 < ord(letter) < 90:
                return False
    return True

while True:
    phrase: list = input("Write something: ").split()
    if check_input(phrase):
        print(' '.join(int_func(word) for word in phrase))
    else:
        print("Error! Word should not contain capital letters.")
    res = input("Press 'y' to continue.")
    if res != "y":
        break


