# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list.
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Continuous loop for ordering
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the menu options
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")

            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Ask customer to input menu item number
            item_number = input("Type the item number to order: ")

            if item_number.isdigit():
                item_number = int(item_number)
                if item_number in menu_items:
                    item_name = menu_items[item_number]["Item name"]
                    item_price = menu_items[item_number]["Price"]

                    # Ask for the quantity
                    quantity = input(f"How many {item_name} would you like to order? ")

                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1  # default to 1 if invalid

                    # Add the item to the order list
                    order.append({
                        "item name": item_name,
                        "price": item_price, 
                        "quantity": quantity
                    })

                else:
                    print("Order is not valid.")    
            else:
                print("You didn't select a number.")
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")

    # Ask if they want to order more
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").lower()
        if keep_ordering == 'y':
            break
        elif keep_ordering == 'n':
            place_order = False
            break
        else:
            print("Please enter 'Y' or 'N'.")

# Print out the customer's order
print("This is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the items in the customer's order
for item in order:
    item_name = item["item name"]
    item_price = item["price"]
    quantity = item["quantity"]

    # Calculate spaces for formatted printing
    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item_price:.2f} | {quantity}")

# Calculate the total cost of the order
total_cost = sum(item["price"] * item["quantity"] for item in order)
print(f"\nTotal cost: ${total_cost:.2f}")
print("Thank you for your order!")