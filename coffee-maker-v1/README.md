# ☕ Coffee Machine Project

A Python-based coffee machine simulator that allows users to order different types of coffee, process payments with coins, and manage resources.

## 🚀 Features

- **Multiple Coffee Types**: Choose from espresso, latte, and cappuccino
- **Coin Payment System**: Accept quarters, dimes, nickels, and pennies
- **Resource Management**: Track water, milk, and coffee bean levels
- **Profit Tracking**: Monitor earnings from coffee sales
- **Resource Reports**: Check remaining ingredients at any time
- **Change Calculation**: Automatically calculate and return change when overpaying

## 📋 Menu & Pricing

| Coffee Type | Price | Ingredients |
|-------------|-------|-------------|
| Espresso    | $1.50 | 50ml water, 18g coffee |
| Latte       | $2.50 | 200ml water, 150ml milk, 24g coffee |
| Cappuccino  | $3.00 | 250ml water, 100ml milk, 24g coffee |

## 🎮 How to Use

1. **Run the program**:
   ```bash
   python coffee_machine.py
   ```

2. **Choose your coffee**:
   - Type `espresso`, `latte`, or `cappuccino`
   - Type `report` to check remaining resources
   - Type `off` to exit the program

3. **Insert coins** when prompted:
   - Enter the number of quarters (25¢ each)
   - Enter the number of dimes (10¢ each)
   - Enter the number of nickels (5¢ each)
   - Enter the number of pennies (1¢ each)

4. **Enjoy your coffee!** ☕

## 📁 Project Structure

```
day-15/
├── coffee_machine.py    # Main program logic
├── menu.py             # Menu data and resources
└── README.md           # This file
```

## 🔧 Technical Details

### Files Description

- **`coffee_machine.py`**: Contains the main program logic including:
  - Customer interaction functions
  - Resource checking and management
  - Coin processing and payment validation
  - Coffee making simulation
  - Main program loop

- **`menu.py`**: Contains the data structures for:
  - Coffee menu with ingredients and costs
  - Initial resource levels
  - Profit tracking variable

### Key Functions

- `get_customer_demand()`: Handles user input for coffee selection
- `check_resources()`: Validates if sufficient ingredients are available
- `process_coins()`: Calculates total payment from individual coins
- `is_transaction_successful()`: Validates payment and handles change
- `make_coffee()`: Simulates coffee preparation and updates resources
- `print_report()`: Displays current resource levels and profit

## 🎯 Learning Objectives

This project demonstrates:
- **Object-oriented programming concepts**
- **Data structures** (dictionaries, lists)
- **Control flow** (loops, conditionals)
- **Function design and modularity**
- **User input handling and validation**
- **Resource management systems**

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation
1. Clone or download the project files
2. Navigate to the project directory
3. Run the program:
   ```bash
   python coffee_machine.py
   ```

## 🎮 Example Usage

```
Coffee Maker Machine☕
What would you like? (espresso/latte/cappuccino/):​ latte
Insert the coins:
Enter quarters: 10
Enter dimes: 0
Enter nickels: 0
Enter pennies: 0
Your money is more than the cost of coffee. Here is $0.0 dollars in change.
Coffe is brewing, Wait few Seconds☕
Before purchasing latte: 
Report of remaining resources:
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
    Money: $0

After Purchasing latte:
Report of remaining resources:
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5

Here is your latte. Enjoy!
```

## 🤝 Contributing

This is a learning project from Angela Yu's 100 Days of Python course. Feel free to experiment and modify the code to add new features or improve functionality!

## 📝 License

This project is created for educational purposes as part of the 100 Days of Python course.
