with open("some_text.txt", "r", encoding="utf-8") as f:
    text_arr = f.readlines()
print("quantity of strings in file: ", len(text_arr))
print("strings: ", text_arr)
i = 1
for phrase in text_arr:
    phrase = phrase.split(" ")
    print(f"Quantity of words in string {i}: {len(phrase)}")
    i += 1
