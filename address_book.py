# Dictionary to store contacts
contacts = {}

# Functions for contact management

def add_contact(name, address, email, phone):
    # Add a new contact to the dictionary
    contact = {"name": name, "address": address, "email": email, "phone": phone}
    contacts[name] = contact

def delete_contact(name):
    # Delete a contact by name if it exists
    if name in contacts:
        del contacts[name]
        return True
    return False

def delete_all_contacts():
    # Delete all contacts from the dictionary
    contacts.clear()

def search_contacts(name):
    # Search for a contact by name and print its details if found
    if name in contacts:
        print(f"Name: {contacts[name]['name']}, Address: {contacts[name]['address']}, Email: {contacts[name]['email']}, Phone: {contacts[name]['phone']}\n")
    else:
        print("Contact not found")

def list_contacts():
    # List all contacts in the dictionary
    if not contacts:
        print("No contacts found")
    else:
        for contact in contacts.values():
            print(f"Name: {contact['name']}, Address: {contact['address']}, Email: {contact['email']}, Phone: {contact['phone']}\n")

# Functions for user input

def get_contact_info_from_user():
    # Prompt the user for contact information and handle empty responses
    fields = ["name", "address", "email", "phone"]
    contact_info = {}

    for field in fields:
        while True:
            value = input(f"Please give the {field} of this contact: ")
            if value.strip():
                contact_info[field] = value
                break
            else:
                print(f"Error: {field.capitalize()} cannot be empty. Try again.")
    
    return contact_info

def add_contact_to_contacts():
    # Add a new contact to the dictionary based on user input
    contact_info = get_contact_info_from_user()
    add_contact(**contact_info)

def delete_contact_from_contacts():
    # Delete a contact based on user input
    name = input("Please give the name of the contact you want to delete: ")
    if delete_contact(name):
        print("Successfully removed contact!")
    else:
        print("Failed to find contact, please try again")

def create_search():
    # Search for a contact based on user input
    name = input("Please give the name of the contact you want to search for: ")
    search_contacts(name)

# Functions for program flow

def handle_response(response):
    # Handle user responses and perform corresponding actions
    response_lower = response.lower()
    if response_lower == "list":
        list_contacts()
    elif response_lower == "add":
        add_contact_to_contacts()
    elif response_lower == "delete":
        delete_contact_from_contacts()
    elif response_lower == "delete all":
        delete_all_contacts()
        print("Successfully deleted all contacts")
    elif response_lower == "search":
        create_search()
    elif response_lower == "close":
        print("See you next time!")
        return False
    else:
        print("Incorrect response. Please respond correctly next time!")
    return True

def run():
    # Main function to run the address book program
    running = True
    welcome = "Welcome to your favorite address book!"
    main_menu = """What do you want to do?
    | List       | Lists all users
    | Add        | Adds a user
    | Delete     | Deletes a user
    | Delete all | Removes all users
    | Search     | Search for a user
    | Close      | Closes the address book"""

    print(welcome)
    
    while running:
        print(main_menu)
        user_response = input()
        running = handle_response(user_response)

# Start the address book program
run()