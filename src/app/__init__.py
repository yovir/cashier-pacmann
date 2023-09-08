"""This script is used to mark this directory
as a Python package.

Function definitions and variable assignments 
will be executed first when the package is imported.
"""

# Import module to print colored text.
from colorama import init as colorama_init
from colorama import Fore
from colorama import Back
from colorama import Style

# Import module to clear terminal text.
from os import system, name
from time import sleep

# Import module to produce ASCII art.
import pyfiglet

# Import module to print table.
import tabulate
import pandas as pd

# Import module for currency formatting.
import locale


# Call colorama initialization function, so we can print colored text.
colorama_init()

# Set Indonesia locale as formatting.
locale.setlocale(locale.LC_ALL, "id_ID")


class ClearScreen:
    """A class to clear the terminal screen."""

    def clear(self):
        """Clears the terminal screen.

        This method uses the appropriate clear command 
        for the current operating system.
        """

        # Determine the operating system:
        # for Windows
        if name == "nt":
            _ = system("cls")

        # for Mac and Linux(here, os.name is "posix")
        else:
            _ = system("clear")


# Define global variable for clear screen.
clear_screen = ClearScreen()


class WelcomeMessage:
    """A class to show welcome message."""

    def show(self):
        """Shows the welcome message.

        After showing it, then it clears the screen.
        """

        # Set app name for banner.
        APP_NAME = "Omega Cashier"

        # Use pyfiglet to create ASCII art for app banner.
        message = pyfiglet.figlet_format(APP_NAME, font="ogre")
        print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")


# Define global variable for printing welcome message.
welcome_message = WelcomeMessage()