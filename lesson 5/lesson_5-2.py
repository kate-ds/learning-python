"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("some_text.txt", "r", encoding="utf-8") as f:
        text_arr = f.readlines()
    print("quantity of strings in file: ", len(text_arr))
    # print("strings: ", text_arr)
    i = 1
    for phrase in text_arr:
        phrase = phrase.split(" ")
        print(f"Quantity of words in string {i}: {len(phrase)}, string: {' '.join(phrase)[:-1]}")
        i += 1
except IOError:
    print("Error!")
