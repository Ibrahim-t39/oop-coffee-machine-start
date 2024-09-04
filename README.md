# Coffee Machine

## Full Description

The Coffee Machine project is an interactive console-based simulation of a coffee vending machine. Users can choose from three types of coffee: latte, cappuccino, and espresso. The machine checks if there are enough resources (water, milk, coffee) to make the selected drink and processes the payment. It also provides the option to view a report of the current resources and earnings.

**Features:**
- **Coffee Options:** The user can choose between latte, cappuccino, and espresso.
- **Resource Management:** The machine checks if it has enough ingredients to prepare the selected coffee. If resources are insufficient, it informs the user.
- **Payment Processing:** The machine handles payments, ensuring the user inserts the correct amount of money before dispensing the coffee.
- **Reports:** Users can view a report of the current resources (water, milk, coffee) and the total money earned.
- **Turn Off Option:** The machine can be turned off by entering "off" as a command.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### How to Use

1. Clone or download the repository to your local machine.
2. Ensure you have the `menu.py`, `coffee_maker.py`, and `money_machine.py` modules in the same directory.
3. Run the script using Python:

   ```bash
   python coffee_machine.py
   ```

4. Follow the on-screen prompts to:
   - Choose a coffee option.
   - Insert money to make a purchase.
   - View reports on the machine's resources and earnings.
   - Turn off the machine by typing "off."

5. The machine will prepare your selected coffee if there are sufficient resources and the payment is successful.

### Customization

You can customize the Coffee Machine by:
- **Adding More Drinks:** Modify the `Menu` class to include additional coffee types or other beverages.
- **Adjusting Prices and Resources:** Change the prices or required resources for each drink to simulate different machine configurations.
- **Enhancing Functionality:** Add features such as restocking resources, handling change, or adding new report metrics.
