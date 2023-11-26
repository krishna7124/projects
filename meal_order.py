# Define menus and prices
food_menu = {"Italian Pizza": 110.0, "Paneer Pizza": 150.0, "Cheese Pizza": 90.0, "Veg. Burger": 70.0, "Paneer Bhurji Burger": 150.0, "French Fries": 80.0, "Peri Peri French Fries": 120.0}
drink_menu = {"Mint Mojito": 40.0, "Cold Coffee": 40.0, "Cold Coco": 40.0, "Kitkat Shake": 60, "Chocolate Shake": 60.0, "Oreo Shake": 60.0, "Cadbury Shake" : 80}
services_menu = {"Delivery": 100.0, "Tip": 50.0}


# Initialize order list
order = []

# Name of the meal system program
meal_system_name = "Foodie Delights"

# Function to display the main menu and handle user input
def main_menu():
    # Reset the order list at the beginning of each session
    order = []
    # Flag to track if payment has been made
    payment_made = False  # Initialize the variable here

    # Get the user's name
    user_name = input(f"Enter your name to start ordering at {meal_system_name}: ")

    print(f"\nWelcome, {user_name}, to {meal_system_name}!\n")
    while True:
        print("\nMain Menu:")
        print("1. Order Food")
        print("2. View Order Reports")
        print("3. Make Payment")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Process food order
            process_order(order, food_menu, drink_menu, services_menu, user_name)
        elif choice == "2":
            # Display order reports
            display_reports(order)
        elif choice == "3":
            # Make payment
            payment_made = make_payment(order)
        elif choice.lower() == "exit" or choice == "4":
            # Exit the program
            if not payment_made:
                print("You must make a payment before exiting.")
            else:
                print(f"Thank you, {user_name}, for using {meal_system_name}. Have a great day!")
                break
        else:
            print("Invalid choice. Please try again.")
            
# Function to process the user's food order
def process_order(order, food_menu, drink_menu, services_menu, user_name):
    while True:
        
        counter = 1
        print("\nFood Menu:")
        # Display the food menu items and prices
        for item, price in food_menu.items():
            print(f"{counter}. {item:<25} ₹{price}")
            counter += 1
                        
        print("\nDrink Menu:")
        # Display the drink menu items and prices
        for item, price in drink_menu.items():
            print(f"{counter}. {item:<25} ₹{price}")
            counter += 1
        
        print("\nServices Menu:")
        # Display the services menu items and prices
        for item, price in services_menu.items():
            print(f"{counter}. {item:<25} ₹{price}")
            counter += 1

        user_input = input("\nEnter the item number you want to order (or type 'done' to finish): ")

        if user_input.lower() == 'done':
            break
        
        if user_input.isdigit():
            item_number = int(user_input)
            total_items = len(food_menu) + len(drink_menu) + len(services_menu)
            
            if 1 <= item_number <= total_items:
                # Determine the menu category based on the selected item number
                
                if item_number <= len(food_menu):
                    menu_category = "Food"
                    menu = food_menu
                
                elif item_number <= len(food_menu) + len(drink_menu):
                    menu_category = "Drink"
                    menu = drink_menu
                    item_number -= len(food_menu)

                else:
                    menu_category = "Services"
                    menu = services_menu
                    item_number -= len(food_menu) + len(drink_menu)

                # Add the selected item to the order
                item = list(menu.keys())[item_number - 1]
                
                quantity = get_positive_integer_input("Enter the quantity: ")
                
                order.append((item, quantity, menu[item]))

                print(f"{item} ({quantity}x) added to your {menu_category} order.")
                break
            else:
                print("Invalid item number. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a valid number.")
            
# Function to display order reports
def display_reports(order):
    if not order:
        print("No orders placed yet.")
        return

    print("\nOrder Reports:")
    
    total_price = 0

    for item in order:
        quantity = item[1]
        price = item[2]
        total_price += quantity * price
  
    print(f"{'Item':<30}{'Quantity':<10}{'Price'}")
    
    for item, quantity, price in order:
        print(f"{item:<30}{quantity:<10}₹{price}")

    print(f"\nTotal Price: ₹{total_price:.2f}")
    applied_discount = apply_discounts(total_price)
    print(f"Discount Applied: {applied_discount}%")
    final_price = total_price * (1 - applied_discount / 100)
    print(f"Final Amount to be Paid: ₹{final_price:.2f}")


# Function to apply discounts based on the total order price
def apply_discounts(total_price):
    discount = 0
    if total_price > 200:
        discount = 5
    if total_price > 1000:
        discount = 10
    if total_price > 5000:
        discount = 15
    return discount

# Function to complete the payment process
def make_payment(order):
    if not order:
        print("No orders to process payment.")
        return False

    # Display order reports before processing payment
    display_reports(order)
    print(f"\nPayment Successful at {meal_system_name}!, Enjoy Your Food")

    # Clear the current order after successful payment
    order.clear()

    return True

# Function to get positive integer input from the user
def get_positive_integer_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print("Invalid input. Please enter a positive integer.")

# Call the main menu function to start the program
main_menu()