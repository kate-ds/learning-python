"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    with open("people.txt", "r", encoding="utf-8") as f:
        file_list = f.readlines()

    people = []
    for e in file_list:
        people.append({
            "name": e.split(" ")[0],
            "salary": float(e.split(" ")[1][:-1])
        })
    print("Guys with salary lesser than 20,000:", ", ".join([e["name"] for e in people if e["salary"] < 20000]))

    salary_sum = 0
    for e in people:
        salary_sum += e["salary"]
    average_salary = salary_sum / len(people)
    print("Average salary: %.2f" % average_salary)

except IOError:
    print("Error!")

