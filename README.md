
# Py_Cafe: Virtual Cafe Management System

## Overview
Py_Cafe is an interactive Python-based cafe management system designed to simulate a virtual coffee shop experience. It allows users to order coffee, cakes, and muffins while maintaining inventory, generating bills, and simulating a realistic cafe workflow.

## Features
- **Dynamic Menu**: Offers coffee, cakes, and muffins with customizable options for size, flavor, and shape.
- **Inventory Management**: Automatically updates inventory and alerts when ingredients are low.
- **Billing System**: Calculates total cost, accepts payment, and provides change.
- **Realistic Simulation**: Includes slow-print animations for a lifelike customer interaction experience.
- **Order Tracking**: Assigns order numbers for better tracking.

## Requirements
- Python 3.6+
- Libraries: None (built using standard Python libraries)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/py_cafe.git
   ```
2. Navigate to the project directory:
   ```bash
   cd py_cafe
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

## Project Structure
```
Py_Cafe/
│
├── CoffeeMachine.py         # Handles coffee preparation and inventory
├── Baking_Machine.py        # Manages cake and muffin baking
├── Billing_Machine.py       # Manages billing operations
├── menu.py                  # Contains menu items, sizes, shapes, and flavors
├── inventory.py             # Tracks inventory levels for ingredients
├── main.py                  # Main program to run Py_Cafe
├── README.md                # Project documentation
```

## Sample Output
```
Welcome to Py_cafe
What would you like to order today? Options: ['espresso', 'cappuccino', 'latte', 'cake', 'muffin']: cake
What shape would you like? Available shapes: ['round', 'square', 'love']: round
What flavour would you like? Available flavours: ['chocolate', 'vanilla', 'berry']: berry
Round Berry cake baked successfully!
$20 added to your bill. Total bill: $20
Thank you! Your order no. #1 is being prepared...
......
Thanks for ordering. Next customer, please!
```

## Future Enhancements
- Add more food and drink options.
- Integrate a GUI using Tkinter or PyQt.
- Enable saving order history in a database.

## Contributing
Feel free to submit pull requests or report issues. Contributions are welcome!
