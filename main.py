from exercise import get_exercises_info 
from google_sheets import create_enrty
import sys
if __name__== "__main__":

    """
    while the program is active 
    1) take input from the user
    2) get exercises info
    3) update the google sheet
    -> repeat untill exit
    """

    query = input("enter what u've done for training:\n-> ")
    create_enrty(get_exercises_info(query))
    sys.exit()
