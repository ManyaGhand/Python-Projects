import art
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit=0

def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():

    print("Please insert coins.")
    total = int(input("How many quarters do you have?")) * 0.25
    total+= int(input("How many dimes do you have?")) * 0.1
    total+= int(input("How many nickles do you have?")) * 0.05
    total+= int(input("How many pennies do you have?")) * 0.01
    return total

def transaction_possible(money_received,cost_drink):
    if money_received>=cost_drink:
        change=round(money_received-cost_drink)
        print(f"Here is your change {change}$")
        global profit
        profit+=cost_drink
        return True
    else:
        print("Sorry not enough money.")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} drink.")




machine_runs=True
while machine_runs:
    print(art.logo)
    choice=input("What would you like?(espresso/latte/cappuccino):").lower()


    if choice=="off":
        machine_runs=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:{profit}$")
    else:
        drink=MENU[choice]
        if resource_sufficient(drink['ingredients']):
            coins=process_coins()
            transaction_possible(coins,drink['cost'])
            make_coffee(choice,drink['ingredients'])



