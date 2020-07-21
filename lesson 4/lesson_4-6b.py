"""
6. Реализовать два небольших скрипта:

б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import cycle

my_list = ["Don't", "worry!", "Be", "happy"]
i = 0
for word in cycle(my_list):
    if i > 8:
        break
    print(word)
    i += 1

# ---------------------------------------------------------------------------

einstein_said = ["Example",  "isn`t", "another way", "to teach", "it is", "the only way", "to teach."]
word = cycle(einstein_said)
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))

