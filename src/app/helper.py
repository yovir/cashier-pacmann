# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep

# import library for ascii art
import pyfiglet

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