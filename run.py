# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# needed for google sheets api
import gspread
from google.oauth2.service_account import Credentials
import datetime

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
    """
    Get choice of action input from user.
    Run a while loop to collect valid data from the user via the terminal,
    which must be an integer between 1 and 5. 
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Do you want to:\n 1) Make a sale?\n 2) Return a sale?\n "
              "3) Check stock?\n 4) Add a new customer?\n 5) Add a new title?\n")
        chosen_action = input("Please select from above by entering the "
                              "corresponding number and pressing Enter: ")
    
        if validate_chosen_action(chosen_action):
            if int(chosen_action) == 5:
                add_game()
            break


def validate_chosen_action(chosen_action):
    """
    Inside the try, convert user input to an integer.
    Raises ValueError if input cannot be converted (ie, contains letter/s) 
    or if is not an integer between 1 and 5
    """
    try:
        if int(chosen_action) not in (1, 2, 3, 4, 5):
            raise ValueError(
                "Must be a whole num between 1 and 5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True
    

def add_game():
    """
    Get game information input from user.
    Run a while loop to collect valid data from the user via the terminal.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        title = input("Add game title\n")
        platform = input("Add platform\n")
        genre = input("Add genre\n")
        min_age = input("Add minimum age\n")
        quantity = input("Add how many\n")

        new_game_info = [title, platform, genre, min_age, quantity]

        if validate_add_game(new_game_info):
            update_games_worksheet(new_game_info)
            break
        # validate_add_game(new_game_info)

    # print(f"You entered...\n Title: {title}\n Platform: {platform}\n "
    #       f"Genre: {genre}\n Minimum age: {min_age}\n How many: {number}")


def validate_add_game(new_game_info):
    """
    Check that all fields have been entered.
    Inside the try, convert min_age and quantity to an integer.
    If they cannot be converted (ie, contains letter/s) print error message
    and continue to run add_game() 
    
    """
    # new_game_info = [title, platform, genre, min_age, number]
    # title, platform, genre, min_age, number
    if not all(new_game_info):
        print("Missing element, please try again")
        return False
    else:
        try:
            int(new_game_info[3])
        except:
            print("min age not a number, please try again")
        try:
            int(new_game_info[4])
        except:
            print("quantity not a number, please try again")
            return False

    return True


def update_games_worksheet(new_game_info):
    """
    Convert min_age and quantity to integers and add new row with the list
    data provided.
    """
    new_game_info[3] = int(new_game_info[3])
    new_game_info[4] = int(new_game_info[4])
    print("Updating games worksheet...\n")
    games_worksheet = SHEET.worksheet("games")
    games_worksheet.append_row(new_game_info)
    print("Games worksheet successfully updated.\n")
    

def add_customer():
    while True:
        fname = input("Add first name\n")
        lname = input("Add last name\n")
        dob = input("Add date of birth\n")

        new_cust_info = [fname, lname, dob]

        if validate_add_customer(new_cust_info):
            # update_games_worksheet(new_game_info)
            break

        # if validate_add_game(new_game_info):
        #     update_games_worksheet(new_game_info)
        #     break


def validate_add_customer(new_cust_info):
    """
    Check that all fields have been entered.
    Inside the try, convert min_age and quantity to an integer.
    If they cannot be converted (ie, contains letter/s) print error message
    and continue to run add_game() 
    
    """
    # new_game_info = [title, platform, genre, min_age, number]
    # title, platform, genre, min_age, number
    while True:
        if not all(new_cust_info):
            print("Missing element, please try again")
            return False
        else:
            try:
                formatted_dob = datetime.datetime.strptime(new_cust_info[2], "%d/%m/%Y")

            except:
                print("wrong date format!!!")
                return False

        return True
# make_choice()
add_customer()
