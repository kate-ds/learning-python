"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


# noinspection SpellCheckingInspection
class Sklad:
    sklad = []

    @staticmethod
    def put_on_sklad(self):
        if self.__class__.__name__ == "Printer":
            obj = {
                "brand": self.brand,
                "model": self.model,
                "price": self.price,
                "quantity": self.quantity,
                "type": self.type,
                "print_in_color": self.print_in_color,
                "wireless": self.wireless
            }
        elif self.__class__.__name__ == "Scanner":
            obj = {
                "brand": self.brand,
                "model": self.model,
                "price": self.price,
                "quantity": self.quantity,
                "resolution": self.resolution,
                "format": self.format
            }
        else:
            obj = {
                "brand": self.brand,
                "model": self.model,
                "price": self.price,
                "quantity": self.quantity,
                "speed_of_copy": self.speed_of_copy,
                "two_side_print": self.two_side_print
            }
        Sklad.sklad.append(obj)
        print(
            f"{self.quantity} {self.__class__.__name__ if self.quantity < 2 else self.__class__.__name__ + 's'} ({self.brand} {self.model}) added to the warehouse")

    @staticmethod
    def move_product_to_department(self, department_name):
        for e in Sklad.sklad:
            if e["brand"] == self.brand and e["model"] == self.model:
                e["quantity"] -= 1

        Sklad.sklad = [e for e in Sklad.sklad if e["quantity"] > 0]
        print(
            f"{self.quantity} {self.__class__.__name__ if self.quantity < 2 else self.__class__.__name__ + 's'} ({self.brand} {self.model}) moved to {department_name}")

    @staticmethod
    def print_all_products():
        print(f"All products: {Sklad.sklad}")


# noinspection SpellCheckingInspection
class Orgteknika(Sklad):
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
        try:
            self.quantity = int(self.quantity)
        except ValueError:
            print(f"Check {self.brand} {self.model}'s quantity value: '{self.quantity}'. It should be integer")
            self.quantity = 0
        try:
            self.price = float(self.price)
        except ValueError:
            print(f"Check {self.brand} {self.model}'s price value: '{self.price}'. It should be numeric")
            self.price = 0


class Printer(Orgteknika):
    def __init__(self, brand, model, price, quantity, type, print_in_color, wireless):
        super().__init__(brand, model, price, quantity)
        self.type = type
        self.print_in_color = print_in_color
        self.wireless = wireless

    def __str__(self):
        return f"Printer {self.brand} {self.model}, price: {self.price} eur\n" + \
               f"type: {self.type}, prints in color: {self.print_in_color}, wireless: {self.wireless}"


class Scanner(Orgteknika):
    def __init__(self, brand, model, price, quantity, resolution, format):
        super().__init__(brand, model, price, quantity)
        self.resolution = resolution
        self.format = format

    def __str__(self):
        return f"Scanner {self.brand} {self.model}, price: {self.price} eur\n" + \
               f"resolution: {self.resolution}, format: {self.format}"


class MFU(Orgteknika):
    def __init__(self, brand, model, price, quantity, speed_of_copy, two_side_print):
        super().__init__(brand, model, price, quantity)
        self.speed_of_copy = speed_of_copy
        self.two_side_print = two_side_print

    def __str__(self):
        return f"MFU {self.brand} {self.model}, price: {self.price} eur\n" + \
               f"speed_of_copy: {self.speed_of_copy}, two_side_print: {self.two_side_print}"


new = Sklad()

hp1020 = Printer("hp", "1020", 118, 1, "laser", False, False)
print(hp1020)
print()
# new.put_on_sklad(hp1020)


canon = Scanner("Canon", "Canoscan LIDE300 ", 190, 3, "2400×2400dpi", "A4")
print(canon)
print()

xerox = MFU("Xerox", "3025NI", 237, 5, "20 page/min", False)
print(xerox)
print()

# new.put_on_sklad()

new.put_on_sklad(hp1020)
# new.put_on_sklad(hp1020, 1)
new.put_on_sklad(xerox)
print()

l120 = Printer("Epson", "L120", "89 usd", "4 psc", "laser", False, False)
print(l120)
print()

new.put_on_sklad(l120)
new.move_product_to_department(hp1020, "Accounting department")
new.put_on_sklad(hp1020)

new.print_all_products()
