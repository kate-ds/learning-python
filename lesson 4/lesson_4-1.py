from sys import argv
file_name, hours_worked, rate, bonus = argv


try:
    salary = float(hours_worked) * float(rate) + float(bonus)

    print(f"Hours worked: {hours_worked} hours")
    print(f"Rate: {rate} rub/hour")
    print(f"Bonus: {bonus} rub")
    print(f"Your salary: {salary} rub")
except ValueError:
    print("Incorrect Values!")


