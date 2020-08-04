"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(e) for e in line]) for line in self.matrix])
# ---------------------------------------------------------------------------------------

        # res = ""
        # for i in range(0, len(self.matrix)):
        #     for j in range(0, len(self.matrix[i])):
        #         if j == len(self.matrix[i]) - 1:
        #             res += str(self.matrix[i][j])
        #         else:
        #             res += str(self.matrix[i][j]) + "   "
        #     res += "\n"
        # return res

# ---------------------------------------------------------------------------------------

    # def __add__(self, other):
    #     sum = []
    #     for i in range(0, len(self.matrix)):
    #         sum.append([x + y for x, y in zip(self.matrix[i], other.matrix[i])])
    #     return sum

# ---------------------------------------------------------------------------------------
    def __add__(self, other):
        result = ''
        for line1, line2 in zip(self.matrix, other.matrix):
            summed_line = [x + y for x, y in zip(line1, line2)]
            result += ' '.join([str(i) for i in summed_line]) + '\n'
        return result

# ---------------------------------------------------------------------------------
    # def __add__(self, other):
    #     sum_matrix = []
    #     for i in range(0, len(self.matrix)):
    #         int_matrix = []
    #         for j in range(0, len(self.matrix[i])):
    #             int_matrix.append(self.matrix[i][j] + other.matrix[i][j])
    #         sum_matrix.append(int_matrix)
    #     return sum_matrix
    #
# ---------------------------------------------------------------------------------


matrix1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
matrix2 = Matrix([[2, 3, 4], [4, 5, 6], [6, 7, 8]])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
# matrix3 = Matrix(matrix1 + matrix2)
# print(matrix3)