☕ Coffee Machine Simulator
A console-based Python project that simulates a coffee vending machine. The program handles coin input, resource tracking (water, milk, coffee), and manages drink preparation based on availability and payment.
🔧 Features
- Choose from three drinks: espresso, latte, cappuccino
- Resource check before making coffee
- Coin-based payment system: accepts quarters, dimes, nickels, and pennies
- Calculates and returns change if overpaid
- Tracks total money collected and resources used
- Console cleared between actions for better UX
- Error handling for invalid coin inputs
- Command options: report (show current resources), exit (quit program)
📸 Sample Output
Welcome to the Coffee Machine!
Type 'report' to see the current resources.
Type 'exit' to stop using the machine.
What would you like? (espresso/latte/cappuccino): latte
YOU HAVE TO PAY $2.5 IN COINS
Please insert coins.
How many quarters (25 cents)? 10
How many dimes (10 cents)? 0
How many nickels (5 cents)? 0
How many pennies (1 cent)? 0
Here is your change: $0.00
Here is your latte. Enjoy!
▶️ How to Run
- Make sure Python is installed (python3 --version)
- Clone or download this repo
- Run the script using:
python coffee_machine.py
🚀 Future Improvements
- Add refill option for resources
- Track number of drinks served
- Save daily report to file
- GUI version using Tkinter for a more interactive interface
💻 Author
Created by Vansh — passionate about Python, logic-based projects, and interactive simulations.
Connect on LinkedIn → www.linkedin.com/in/vansh-shan-a23407276


