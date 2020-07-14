i = 1
list_product = []
while True:
    name = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Product quantity: "))
    piece = input("Unit: ")
    product_parameter = {"name": name, "price": price, "quantity": quantity, "unit": piece}
    product = (i, product_parameter)
    list_product.append(product)
    print(list_product)
    res = input("One more? y/n ")
    if res == "n":
        break
    i = i + 1
names = []
price = []
quantity = []
piece = []
for e in list_product:
    num, dictionary = e
    names.append(dictionary["name"])
    price.append(dictionary["price"])
    quantity.append(dictionary["quantity"])
    if not dictionary["unit"] in piece:
        piece.append(dictionary["unit"])
stat = {"name": names, "price": price, "quantity": quantity, "piece": piece}
print(stat)


