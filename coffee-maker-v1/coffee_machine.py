from menu import MENU, profit, resources

print ("Coffee Maker Machine☕")

stop_machine = False

def get_customer_demand():
    customer_demand = input("What would you like? (espresso/latte/cappuccino/):​ ").lower()
    return customer_demand


def print_report(resources):
    print(f"""Report of remaining resources:
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${profit}

""")

def check_resources (coffee_ingredients):
    """Checks the resources are sufficent or not"""
    resources_sufficient  = True
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] < resources[ingredient]:
            resources_sufficient = True
        else:
            print(f"Sorry there is not enough {ingredient}.")
            resources_sufficient = False
            break
    return resources_sufficient       
def process_coins(quarters, dime, nickels, pennies): 
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    total_amount = (quarters * quarter_value) + (dime * dime_value) + (nickels * nickel_value) + (pennies * penny_value)
    return total_amount
 
def is_transaction_successful(coffe_cost, customer_money):
    global profit
    if customer_money == coffe_cost:
        profit += coffe_cost
        return True
    elif customer_money > coffe_cost:
        change = round((customer_money -coffe_cost), 2)
        profit += coffe_cost
        print(f"Your money is more than the cost of coffee. Here is ${change} dollars in change.")
        return True
    
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(resources, coffee_type, coffee_ingredients):
    """Makes the coffee and returns the remaining resources."""

    print(f"Before purchasing {coffee_type}: ")
    print_report(resources)
    remaining_resources = {}
    for resource in resources:
        if resource in  coffee_ingredients:
            final_resource = resources[resource] - coffee_ingredients[resource]
            remaining_resources[resource] = final_resource
        else:
            remaining_resources[resource] = resources[resource]

    print(f"After Purchasing {coffee_type}:")
    print_report(remaining_resources)

    return remaining_resources


coffee_types =["espresso", "latte", "cappuccino",]

while not stop_machine:
    customer_demand = get_customer_demand()

    if customer_demand.lower() == "report":
        print_report(resources)
    elif customer_demand.lower() == "off":
        stop_machine = True
    elif customer_demand.lower() in coffee_types:
        coffee_type = customer_demand
        coffee_ingredients =MENU[coffee_type]["ingredients"]
        coffee_cost = MENU[coffee_type]["cost"]
        is_resources_sufficient = check_resources(coffee_ingredients)
        
        if is_resources_sufficient:
            print(f"Insert the coins:")

            quarters = int(input("Enter quarters: "))
            dime = int(input("Enter dimes: "))
            nickels = int(input("Enter nickels: "))
            pennies = int(input("Enter pennies: "))

            customer_money = process_coins(quarters, dime, nickels, pennies)

            transaction_result = is_transaction_successful(coffee_cost, customer_money)

            if transaction_result:
                print(f"Coffe is brewing, Wait few Seconds☕")
                coffee_making_result = make_coffee(resources, coffee_type, coffee_ingredients)
                resources = coffee_making_result
                print(f"Here is your {coffee_type}. Enjoy!")
            else:
                print(f"Not enough money! Here's your refund.")
                stop_machine =True
        else:
            stop_machine=True