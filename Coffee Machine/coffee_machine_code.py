from coffee_machine_data import MENU, resources, profit


def check_resources(ingredients):
    """ compares ingredients and resources """
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coin_processor():
    """ returns total of coins """
    print("Please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickels?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

def check_transaction(payment_received, drink_cost):
    """ check if money is sufficient """
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry the money is not enough. Money refunded")
        return False
def make_coffee(drink_name, order_ingredients):
    """Subtracts ingredients from resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


order_again = True
while order_again:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        order_again = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = coin_processor()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])