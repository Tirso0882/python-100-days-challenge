from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# Menu
#     get_items
#     find_drink

# MoneyMachine
#     CURRENCY
#     COIN_VALUES
#     report
#     process_coins
#     make_payment

# CoffeeMaker
#     report
#     is_resource_sufficient
#     make_coffee

# 1. Print report
menu = Menu()
items = menu.get_items()
print(items)
drink_type = menu.find_drink("espresso")
print(drink_type)

# money_machine = MoneyMachine()
# report_mm = money_machine.report()
# print(report_mm)

# coffee_maker = CoffeeMaker()
# report_cm = coffee_maker.report()

# 2. Check resources sufficient
# inventory = coffee_maker.is_resource_sufficient("")




# 3. Process coins
# 4. Check transaction successfull?
# 5. Make coffee