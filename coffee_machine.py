
INITIAL_INGREDIENTS = {"coffee": 100, "milk": 300, "water": 200, "money": 0.0}
COFFEE_RECIPES = {
    "espresso": {"water": 250, "coffee": 16, "milk": 0, "cost": 4.0},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "cost": 2.5},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "cost": 3.0}
}

class Coffee_Machine:
   
    ingredients = INITIAL_INGREDIENTS.copy() # Ek copy banate hain taaki original dictionary modify na ho
    recipes = COFFEE_RECIPES # Recipes constant rahengi

    def __init__(self):
    
        pass

    def _get_coffee_cost(self, order_type):
        """Helper to get the cost of a coffee type."""
        return self.recipes[order_type]["cost"]

    def _get_coffee_ingredients(self, order_type):
        """Helper to get ingredients required for a coffee type."""
        return self.recipes[order_type] # Returns the dict for that coffee

    def check_sufficient_ingredients(self, order_type):
        """Checks if there are enough ingredients for the requested coffee."""
        if order_type not in self.recipes:
            print(f"Sorry, '{order_type}' is not a valid coffee type.")
            return False

        required_ingredients = self._get_coffee_ingredients(order_type)

        for ingredient, amount_needed in required_ingredients.items():
            if ingredient in self.ingredients and ingredient != "cost": # 'cost' ingredient nahi hai
                if self.ingredients[ingredient] < amount_needed:
                    print(f"Sorry, there is not enough {ingredient}.")
                    return False
        return True # Sab kuch sufficient hai

    def process_coins(self, cost_of_coffee):
        """Collects coins from the user and checks if the amount is sufficient."""
        print(f"You have to pay ${cost_of_coffee:.2f}")
        try:
            print("Please insert coins.")
            quarters = int(input("How many quarters (25 cents)? ")) * 0.25
            dimes = int(input("How many dimes (10 cents)? ")) * 0.10
            nickels = int(input("How many nickels (5 cents)? ")) * 0.05
            pennies = int(input("How many pennies (1 cent)? ")) * 0.01
            
            total_paid = quarters + dimes + nickels + pennies
            print(f"You inserted: ${total_paid:.2f}")

            if total_paid >= cost_of_coffee:
                change = total_paid - cost_of_coffee
                if change > 0:
                    print(f"Your change is ${change:.2f}")
                print("Payment successful! 👍👍")
                return True, change # Return True for success, and the change
            else:
                print(f"Transaction failed due to insufficient amount paid. You paid ${total_paid:.2f} but needed ${cost_of_coffee:.2f}. 😒😒")
                return False, 0 # Return False for failure
        except ValueError:
            print("Invalid input. Please enter whole numbers for coins. Transaction cancelled.")
            return False, 0

    def make_coffee(self, order_type):
        """Deducts ingredients and updates money after a successful transaction."""
        required_ingredients = self._get_coffee_ingredients(order_type)

        for ingredient, amount_needed in required_ingredients.items():
            if ingredient in self.ingredients and ingredient != "cost":
                self.ingredients[ingredient] -= amount_needed
        
        self.ingredients["money"] += required_ingredients["cost"] # Add cost to machine's money

        print(f"Your {order_type} is ready! Enjoy your coffee. 😎😎")

    def report(self):
        """Prints the current report of ingredients and money."""
        print("\n--- Current Machine Report ---")
        for item, amount in self.ingredients.items():
            if item == "money":
                print(f"Money: ${amount:.2f}")
            else:
                print(f"{item.capitalize()}: {amount}ml") # ml units for ingredients
        print("------------------------------")

# --- Main Program Logic ---
def run_coffee_machine():
    machine = Coffee_Machine() # Create one instance of the machine

    print('''
Welcome to the Shan Coffee Machine.
We have Espresso, Latte and Cappuccino☕☕
''')

    while True:
        choice = input("What would you like to have (espresso/latte/cappuccino)? Or type 'report' for supply, 'off' to turn off: ").lower()

        if choice == "off":
            print("Turning off the machine. Goodbye!")
            break
        elif choice == "report":
            machine.report()
        elif choice in machine.recipes:
            order_cost = machine._get_coffee_cost(choice)

            # 1. Check ingredients
            if machine.check_sufficient_ingredients(choice):
                # 2. Process payment
                payment_successful, change_returned = machine.process_coins(order_cost)
                
                if payment_successful:
                    # 3. Make coffee and deduct ingredients
                    machine.make_coffee(choice)
                else:
                    print("Transaction cancelled due to payment issue.")
            else:
                print("Order cannot be fulfilled due to insufficient ingredients.")
        else:
            print("Invalid choice. Please choose from Espresso, Latte, Cappuccino, 'report', or 'off'.")

# Run the coffee machine
run_coffee_machine()