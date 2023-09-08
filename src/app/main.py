from . import *
from colorama import init as colorama_init
from colorama import Fore
from colorama import Back
from colorama import Style
import cutie


# Define global constants for exception message
EMPTY_CART_MESSAGE = "There are no items in your cart. Please add items first!"
INVALID_INPUT_MESSAGE = "Invalid input. Please enter a valid amount!"
ENTER_TO_CONTINUE = "Press [ENTER] to go back to main menu."

order = Cart()
clear_screen = ClearScreen()
welcome_message = WelcomeMessage()


def is_filled():
    """This boolean function returns True when the cart is not empty, 
    and False otherwise. 
    
    It is used by all functions, with the exception of add_items_menu. 
    
    Its intention is to remind users to add items first
    before they will be able to use other functions.
    """
    if (order.is_true()):
        pass
    else:
        clear_screen.clear()
        print(f"{Back.YELLOW}{Fore.BLACK}{EMPTY_CART_MESSAGE}{Style.RESET_ALL}")
        main()

        
def add_items_menu():
    """A function for adding a new item to the shopping cart.
    
    Parameters:
    User will be prompted to input the item's name, quantity, 
    and price as long as they respond with "yes." 
    If the user answers "no," they will be returned to the main screen.

    Input:

    item_name [string] - The name of the item.
    item_quantity [string] - The quantity of the item.
    item_price [string] - The price of the item.

    Process:
    The item_quantity and item_price will be converted into integers. 
    Then, all these values will be passed as arguments to the add_item function within the Cart class.

    Output:
    The function will display a table containing the item_name, item_quantity, 
    item_price, and the total cost of the item.

    """
    # Clear the main screen
    clear_screen.clear()

    # Set the default flag to True
    flag = True

    # While the flag is True, the code below will be executed continuously.
    while flag:
        try:
            # Control user input so that the input should match the requirements.
            welcome_message.show()

            # Show add items menu.
            print("Kindly provide the details of your items, including their names, quantities, and prices.")
            item_name = input("Item name: ")
            item_quantity = input("Quantity: ")
            item_price = input("Price: ")
            
            order.add_item(item_name, int(item_quantity), int(item_price))

        # If the user enters a wrong format, this exception will be printed.
        except ValueError:
            # Clear the main screen
            clear_screen.clear()

            # Show the error message
            print("\n")
            print(f"{Back.YELLOW}{Fore.BLACK}{INVALID_INPUT_MESSAGE}For item quantity and item price.{Style.RESET_ALL}")
            print("\n")
            continue

        # Ask the user whether the user want to add another item.
        if not cutie.prompt_yes_or_no("Do you want to add another item?", enter_empty_confirms=False):
            # Show welcome message and current cart.
            welcome_message.show()
            order.display_cart()

            # Break the loop.
            flag = False

            # Clear the screen then go back to main menu.
            clear_screen.clear()
            main()

        else:
            clear_screen.clear()
            continue


def update_items_menu(): 
    """A function for modifying the user's shopping cart.

    Parameters:
    The function displays the current cart as a reference and 
    provides choices to the user for updating the item name, item quantity, 
    or item price they previously entered using the add_item function.

    
    Input:
    old_item [String] - The item name in the cart that the user wants to update.
    new_item [String] - The new item name to replace the old one.
    new_quantity [String] - The new quantity for the item to replace the existing quantity.
    new_price [String] - The new price for the item to replace the existing price.

    
    Process:
    - To update the item name, the user should enter the old_item 
    exactly as it appears in the cart and provide the new item name as new_item. 
    Both names will be passed to the update_item_name function in the Cart class.
    
    - To update the item quantity, the user should enter the exact item name 
    and provide the new_quantity. Both values will be passed to the update_item_quantity function in the Cart class.
    
    - To update the item price, the user should enter the exact item name 
    and provide the new_price. Both values will be passed to the update_item_price function in the Cart class.

    
    Output:
    The function will result in an updated shopping cart.
    """
    # Show welcome message and current cart
    welcome_message.show()
    order.display_cart()
    
    # Set the default flag to True
    flag = True

    # While the flag is True, the code below will be executed continuously.
    while flag:
        # Show update items menu.
        print("\n")
        print("Please choose what you wish to modify.")
        menu = ["Item name", "Item quantity",
            "Item price", "View current cart",
            "Back to main menu"]

        try:
            choices = menu[cutie.select(menu)]
            if choices == "Item name":
                clear_screen.clear()
                welcome_message.show()

                order.display_cart()
                print("\n")
                
                # User input.
                print("Kindly provide the details of your items to be updated.")
                old_item  = input("Item name: ")
                new_item = input("New item name: ")
                order.update_item_name(old_item, new_item)
                
                continue

            elif choices == "Item quantity":
                clear_screen.clear()
                welcome_message.show()

                order.display_cart()
                print("\n")

                # User input.
                print("Kindly provide the details of your items to be updated.")
                old_item  = input("Item name: ")
                new_quantity = input("New quantity: ")
                order.update_item_quantity(old_item, int(new_quantity))
                
                continue

            elif choices == "Item price":
                clear_screen.clear()
                welcome_message.show()

                order.display_cart()
                print("\n")
                
                # User input.
                print("Kindly provide the details of your items to be updated.")
                old_item  = input("Item name: ")
                new_price = input("New price: ")
                order.update_item_price(old_item, int(new_price))
                
                continue

            elif choices == "View current cart":
                clear_screen.clear()
                welcome_message.show()
                
                # User input.
                order.display_cart()
                print("\n")
                
                continue
            
            elif choices == "Back to main menu":
                # Break the loop.
                flag = False

                # Clear the screen then go back to main menu.
                clear_screen.clear()
                main()

            else:
                continue

        except ValueError:
            print(INVALID_INPUT_MESSAGE)


def remove_item_menu():
    """A function designed to remove an individual item from the cart.

    Parameters:
    The cart is displayed as a reference.
    A condition checks whether the cart is empty.

    Input:
    remove_item_input [String] - The item name the user wishes to remove.

    Process:
    If the cart is not empty:
        remove_item_input is forwarded to the remove_item method within the Cart class.
        Subsequently, the main screen is presented.
    If the cart is empty:
        The main screen is displayed.

    Output:
    An updated cart.

    """
    welcome_message.show()
    order.display_cart()
    print("\n")
    flag = True
    while flag:
        # User input.
        print("Kindly provide the details of your items to be removed.")
        remove_item_input = input("Item name: ")
        order.remove_item(remove_item_input)
        is_filled()

        # Ask the user whether the user want to remove item again.
        if not cutie.prompt_yes_or_no("Do you want to remove another item?", enter_empty_confirms=False):
            # Show welcome message and current cart.
            welcome_message.show()
            order.display_cart()

            # Break the loop.
            flag = False

            # Clear the screen then go back to main menu.
            clear_screen.clear()
            main()

        else:
            continue


def reset_item_menu():
    """A function responsible for resetting the cart.

    Parameters:
    The current cart is displayed for reference.
    A condition checks if the cart is empty.

    Input:
    A user prompt asking if they genuinely wish to reset the cart.

    Process:
    If the cart is not empty:
        If the user responds with "no," the main menu will be displayed.
        Otherwise, the reset_item method is invoked, clearing the cart.
    If the cart is empty:
        The main menu is displayed.

    Output:
    An updated cart.

    """
    welcome_message.show()
    order.display_cart()
    print("\n")

    # Ask the user whether the user want to remove item again.
    if not cutie.prompt_yes_or_no("Do you want to reset the cart?", enter_empty_confirms=False):
        # Show welcome message and current cart.
        welcome_message.show()
        order.display_cart()

        # Clear the screen then go back to main menu.
        clear_screen.clear()
        main()
    
    else:
        order.reset_item()
        print("\n")
        input(ENTER_TO_CONTINUE ).lower().startswith(" ")
        clear_screen.clear()
        main()


def check_order_menu():
    """A function to display the user's cart.

    Parameters:
    Invoking the check_order method and returning to the main menu.

    """
    welcome_message.show()
    order.check_order()
    print("\n")
    input(ENTER_TO_CONTINUE ).lower().startswith(" ")
    clear_screen.clear()
    main()


def main():
    """A main menu function.

    Using the arrow keys, user will be prompted to select an option.

    """
    # Set the store name.
    STORE_NAME = "Omegamart"

    # Show app banner.
    welcome_message.show()

    # Show main menu.
    print(f"Welcome to {Back.BLUE}{Fore.WHITE}{STORE_NAME}{Style.RESET_ALL}. How may we help you today?")
    menu = ["Add items", "Update cart",
            "Remove an item", "Reset cart",
            "Check order", "Checkout cart",
            "Exit"]
    
    choices = menu[cutie.select(menu)]

    if choices == "Exit":
        clear_screen.clear()
        exit()

    elif choices == "Add items":
        clear_screen.clear()
        add_items_menu()

    elif choices == "Update cart":
        is_filled()
        clear_screen.clear()
        update_items_menu()

    elif choices == "Remove an item":
        is_filled()
        clear_screen.clear()
        remove_item_menu()

    elif choices == "Reset cart":
        is_filled()
        clear_screen.clear()
        reset_item_menu()

    elif choices == "Check order":
        is_filled()
        clear_screen.clear()
        check_order_menu()

    elif choices == "Checkout cart":
        is_filled()
        clear_screen.clear()
        checkout_menu()
        
# Execute code when the file runs as a script
if __name__ == "__main__":
    clear_screen.clear()
    main()