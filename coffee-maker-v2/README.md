# Coffee Machine Simulator ☕

A Python-based coffee machine simulator built using Object-Oriented Programming (OOP) principles. This project demonstrates the use of classes, objects, and encapsulation to create a functional coffee vending machine.

## 🎯 Project Overview

This coffee machine simulator allows users to:
- Order different types of coffee (espresso, latte, cappuccino)
- Insert coins to pay for their drinks
- Check resource levels and profit reports
- Automatically manage ingredients and money

## 🚀 Features

### Available Drinks
- **Espresso** - $1.50 (50ml water, 18g coffee)
- **Latte** - $2.50 (200ml water, 150ml milk, 24g coffee)
- **Cappuccino** - $3.00 (250ml water, 50ml milk, 24g coffee)

### Machine Capabilities
- Resource management (water, milk, coffee)
- Coin processing (quarters, dimes, nickels, pennies)
- Automatic change calculation
- Resource and profit reporting
- Ingredient sufficiency checking

## 📁 Project Structure

```
day-16-oop/
├── main.py              # Main program entry point
├── coffee_maker.py      # CoffeeMaker class for resource management
├── menu.py             # Menu and MenuItem classes
├── money_machine.py    # MoneyMachine class for payment processing
└── README.md           # This file
```

## 🏗️ Architecture

The project follows Object-Oriented Programming principles with four main classes:

### 1. CoffeeMaker (`coffee_maker.py`)
- Manages machine resources (water, milk, coffee)
- Checks if resources are sufficient for orders
- Deducts ingredients when making coffee
- Provides resource reports

### 2. Menu & MenuItem (`menu.py`)
- **MenuItem**: Represents individual drink items with ingredients and cost
- **Menu**: Manages the collection of available drinks
- Provides methods to find drinks and get menu options

### 3. MoneyMachine (`money_machine.py`)
- Handles coin processing and payment validation
- Calculates change and manages profit
- Provides profit reporting functionality

### 4. Main Program (`main.py`)
- Orchestrates the interaction between all classes
- Handles user input and program flow

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x

### Running the Program
1. Navigate to the project directory:
   ```bash
   cd day-16-oop
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

### How to Use
1. **Order a Drink**: Type the name of the drink you want (espresso/latte/cappuccino)
2. **Check Resources**: Type "report" to see current resource levels
3. **Insert Coins**: When prompted, enter the number of each coin type
4. **Receive Change**: The machine will automatically calculate and return change if needed

## 💡 Learning Objectives

This project demonstrates:
- **Class Design**: Creating well-structured classes with clear responsibilities
- **Encapsulation**: Keeping data and methods together within classes
- **Object Interaction**: How different objects communicate and work together
- **Resource Management**: Tracking and updating system resources
- **User Input Processing**: Handling various types of user input
- **Error Handling**: Managing insufficient resources and payments

## 🔧 Code Examples

### Creating a Coffee Order
```python
from menu import Menu
menu = Menu()
drink = menu.find_drink("latte")
```

### Checking Resources
```python
from coffee_maker import CoffeeMaker
coffee_maker = CoffeeMaker()
coffee_maker.report()
```

### Processing Payment
```python
from money_machine import MoneyMachine
money_machine = MoneyMachine()
payment_successful = money_machine.make_payment(2.50)
```

## 🎓 Educational Context

This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu, specifically focusing on Day 16 - Object-Oriented Programming concepts. It serves as a practical application of OOP principles in a real-world scenario.

## 🤝 Contributing

This is a learning project, but suggestions for improvements are welcome! Feel free to:
- Add new drink types
- Implement additional features
- Improve error handling
- Enhance the user interface

## 📝 License

This project is created for educational purposes as part of a Python learning course.

---

**Happy Coding! ☕💻**
