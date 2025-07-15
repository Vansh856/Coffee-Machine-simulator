import os
water=300
milk=200
coffee=100
money=0
coffee_type={"espresso": {"water": 250, "coffee": 16, "milk": 0, "cost": 4},
              "latte": {"water": 200, "coffee": 24, "milk": 150, "cost": 2.5},
              "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "cost": 3}}
print("Welcome to the Coffee Machine!")
print("Type 'report' to see the current resources.")
print("Type 'exit' to stop using the machine.")
while True:
    try:
    
    
        ordered_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
        if ordered_coffee in coffee_type:
            if water >= coffee_type[ordered_coffee]["water"] and milk >= coffee_type[ordered_coffee]["milk"] and coffee >= coffee_type[ordered_coffee]["coffee"]:
                print(f"YOU HAVE TO PAY ${coffee_type[ordered_coffee]["cost"]} IN COINS")
                print("Please insert coins.")
                quarters = int(input("How many quarters (25 cents)? ")) * 0.25
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console again
                dimes = int(input("How many dimes (10 cents)? ")) * 0.10
                os.system('cls' if os.name == 'nt' else 'clear')    
                nickels = int(input("How many nickels (5 cents)? ")) * 0.05
                os.system('cls' if os.name == 'nt' else 'clear')
                pennies = int(input("How many pennies (1 cent)? ")) * 0.01
                os.system('cls' if os.name == 'nt' else 'clear')
                total_money = quarters + dimes + nickels + pennies
                if total_money < coffee_type[ordered_coffee]["cost"]:
                    print("Sorry, not enough money. Money refunded.")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                    
                elif total_money > coffee_type[ordered_coffee]["cost"]:
                    change = total_money - coffee_type[ordered_coffee]["cost"]
                    print(f"Here is your change: ${change:.2f}")

                print(f"Here is your {ordered_coffee}. Enjoy!")
                water -= coffee_type[ordered_coffee]["water"]
                milk -= coffee_type[ordered_coffee]["milk"]
                coffee -= coffee_type[ordered_coffee]["coffee"]
                money += coffee_type[ordered_coffee]["cost"]
            else:
                print("Sorry, not enough resources.")
        elif ordered_coffee == "report":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Current resources:")
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money}")
        elif ordered_coffee == "exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thank you for using the Coffee Machine. Goodbye!👋👋")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid choice. Please select espresso, latte, or cappuccino.")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid input. Please enter a valid number for coins.")
