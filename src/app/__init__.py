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


class clearScreen:
# define our clear function
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

class welcomeMsg:
# define our message function to print message at startup
    def show(self):
        # always clear screen first
        clr = clearScreen()

        # using pyfiglet to create ascii art
        message = pyfiglet.figlet_format("Pacmann Cashier")
        clr.clear()
        print(message)

        # break the line at the end message
        print("\n")