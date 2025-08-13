from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu =  Menu()
coffe_maker = CoffeeMaker()
def get_usr_input ():
    return input("What would you like? (expresso/latte/cappuccino)")

user_input = get_usr_input()
print(user_input)


if user_input == "report":
    print(coffe_maker.report())

else:
    ingredients =  menu.find_drink(user_input)
    print(ingredients)