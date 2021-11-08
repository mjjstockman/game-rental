# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# needed for google sheets api
import gspread
from google.oauth2.service_account import Credentials

# IAM config allowing user access 
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("game_rental")

# games = SHEET.worksheet("games")

# data = games.get_all_values()
# print(data)

def make_choice():
    print("Do you want to:\n 1) Make a sale?\n 2) Return a sale?\n "
          "3) Check stock?\n 4) Add a new customer?\n 5) Add a new title?\n")
    chosen_action = input("Please select from above by entering the "
                          "corresponding number and pressing Enter: ")
    validate_chosen_action(chosen_action)


def validate_chosen_action(chosen_action):
    try:
        if chosen_action not in (1, 2, 3, 4, 5):
            raise ValueError(
                "Must be a whole num between 1 and 5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
    

make_choice()




# Add validation to check for exactly 6 values in provided data