"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""
import json
from sys import exit

result = []
try:
    with open("text_7.txt", "r", encoding="utf-8") as f:
        total_profit = 0
        i = 0
        for line in f:
            line_list = line.split()
            # print(int(line_list[2]) - int(line_list[3]))
            try:
                profit = int(line_list[2]) - int(line_list[3])
                result.append({
                    line_list[0]: profit})
                if profit > 0:
                    i += 1
                    total_profit += profit
            except ValueError:
                print(f"Value error! in line {i + 2}")
            except IndexError as err:
                print("other err", err)
        average_profit = total_profit / i
        result.append({"average_profit": average_profit})
except IOError:
    print("Error!")
print(result)

with open("result.json", "w", encoding="utf-8") as res:
    json.dump(result, res, ensure_ascii=False)










