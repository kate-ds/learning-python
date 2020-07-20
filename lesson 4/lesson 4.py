# # my_list = [1, 2, 3, 4, 5, 6]
# new_1 = (el ** 2 for el in range(1, 7))
# new_2 = [el ** 2 for el in range(1, 7)]
#
# # for i in new_1:
# #     print(i)
# print(tuple(new_1))
# print(new_2)

# -----------------------------------------------------------

# from random import randint, randrange, random
#
# print(random())

#-------------------------------------------------------
def my_gen():
    for i in {1, 34, 4, 8}:
        yield i

for i in my_gen():
    print(i)
