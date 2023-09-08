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