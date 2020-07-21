"""
6. Реализовать два небольших скрипта:

а) итератор, генерирующий целые числа, начиная с указанного.
"""

from itertools import count

for el in count(5, 5):
    if el > 30:
        break
    else:
        print(el)
