def main():
    # Initialize inventory and categories dictionaries
    inventory = {}
    categories = {}

    print("Welcome to the Inventory Management System!")
    while True:
        # Display main menu and get user choice
        print_menu()
        choice = get_integer_input("Enter choice: ")

        # Perform actions based on user choice
        if choice == 1:
            add_inventory(inventory, categories)
        elif choice == 2:
            remove_inventory(inventory)
        elif choice == 3:
            update_inventory(inventory)
        elif choice == 4:
            search_inventory(inventory)
        elif choice == 5:
            print_inventory(inventory)
        elif choice == 6:
            manage_categories(inventory, categories)
        elif choice == 99:
            print("Goodbye! Thank you for using the Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to print the main menu
def print_menu():
    print('\n=============================')
    print('= Inventory Management Menu =')
    print('=============================')
    print('(1) Add New Item to Inventory')
    print('(2) Remove Item from Inventory')
    print('(3) Update Inventory')
    print('(4) Search Item in Inventory')
    print('(5) Print Inventory Report')
    print('(6) Manage Categories')
    print('(99) Quit')

# Function to get integer input from the user
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# Function to add a new item to the inventory
def add_inventory(inventory, categories):
    print("\nAdding Inventory")
    print("================")
    item_description = input("Enter the name of the item: ").lower()
    item_quantity = get_integer_input("Enter the quantity of the item: ")
    item_category = input("Enter the category of the item: ").lower()

    # Ensure the category exists in the categories dictionary
    categories.setdefault(item_category, [])
    inventory[item_description] = {"quantity": item_quantity, "category": item_category}

# Function to remove an item from the inventory
def remove_inventory(inventory):
    print("\nRemoving Inventory")
    print("==================")
    item_description = input("Enter the item name to remove from inventory: ").lower()
    if item_description in inventory:
        del inventory[item_description]
        print("Item removed from inventory.")
    else:
        print("Item not found in inventory.")

# Function to update the quantity of an item in the inventory
def update_inventory(inventory):
    print("\nUpdating Inventory")
    print("==================")
    item_description = input('Enter the item to update: ').lower()
    if item_description in inventory:
        item_quantity = get_integer_input("Enter the updated quantity. Enter - for less: ")
        inventory[item_description]["quantity"] += item_quantity
    else:
        print("Item not found in inventory.")

# Function to search for an item in the inventory
def search_inventory(inventory):
    print('\nSearching Inventory')
    print('===================')
    item_description = input('Enter the name of the item: ').lower()
    item_info = inventory.get(item_description)
    if item_info:
        print('Item:     ', item_description)
        print('Quantity: ', item_info["quantity"])
        print('Category: ', item_info["category"])
    else:
        print('Item not found in inventory.')

# Function to print the entire inventory
def print_inventory(inventory):
    print('\nCurrent Inventory')
    print('-----------------')
    for item_description, item_info in inventory.items():
        print('Item:     ', item_description)
        print('Quantity: ', item_info["quantity"])
        print('Category: ', item_info["category"])

# Function to manage categories (add, remove, view)
def manage_categories(inventory, categories):
    while True:
        print('\nCategory Management')
        print('===================')
        print('(1) Add Category')
        print('(2) Remove Category')
        print('(3) View Categories')
        print('(4) View Items by Category')
        print('(5) Return to Main Menu')
        category_choice = get_integer_input('Enter choice: ')
    
        if category_choice == 1:
            add_category(categories)
        elif category_choice == 2:
            remove_category(categories)
        elif category_choice == 3:
            view_categories(categories)
        elif category_choice == 4:
            view_items_by_category(inventory, categories)
        elif category_choice == 5:
            # Return to the main menu
            break
        else:
            print("Invalid choice. Please try again.")
# Function to remove a category
def remove_category(categories):
    category_name = input('Enter the name of the category to remove: ').lower()
    if category_name in categories:
        del categories[category_name]
        print('Category removed: ', category_name)
    else:
        print('Category not found.')

# Function to add a new category
def add_category(categories):
    category_name = input('Enter the name of the category: ').lower()
    categories.setdefault(category_name, [])
    print('Category added: ', category_name)

# Function to view all categories
def view_categories(categories):
    print('\nCategories:')
    for category in categories:
        print(category)

# Function to view all items in a specific category
def view_items_by_category(inventory, categories):
    category_name = input('Enter the name of the category: ').lower()
    if category_name in categories:
        print('\nItems in category: ', category_name)
        for item_description, item_info in inventory.items():
            if item_info['category'] == category_name:
                print('Item:     ', item_description)
                print('Quantity: ', item_info['quantity'])

# Call the main function to start the program
main()
