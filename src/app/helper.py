# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep

class clearScreen:
# define our clear function
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')