def user_data(name, surname, year, city, email, telph):
    print(f"{name} {surname}, {year} year of birth, {city}, contacts: email - {email}, tel - {telph}")


name = input("Your name: ")
surname = input("Your surname: ")
year = input("Year of birth: ")
city = input("City: ")
email = input("Email: ")
telph = input("Telephone number: ")

user_data(name, surname, year, city, email, telph)
