def spin_words(sentence):
    words = sentence.split(" ")
    for i in range(0, len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    words = " ".join(words)
    return words
    # Your code goes here
print(spin_words("Hello my dear waffel"))
