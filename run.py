"""Description of what it does

Args:
    arg_name (data type) : Description of arg_name
        indent next line of description if need to

Returns:
    data_type : Optional description of return value
    Extra lines are not indented

Raises:
    TypeOfError : Include error types intentianally
        raised

Notes:
    See ......... for more info
"""

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# needed for google sheets api
import gspread
from google.oauth2.service_account import Credentials
import datetime
from pprint import pprint

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


def make_choice():
    """Get choice of action as an input from user
    """
    while True:
        print("Do you want to:\n 1) Make a sale?\n 2) Return a sale?\n "
             "3) Check stock?\n 4) Add a new customer?\n 5) Add a new title?\n")
        chosen_action = input("Please select from above by entering the "
                              "corresponding number and pressing Enter:\n")
    
        # HOW TIDY UP, BRIAN??
        if validate_chosen_action(chosen_action):
            if int(chosen_action) == 5:
                add_game()
            elif int(chosen_action) == 4:
                add_customer()
            elif int(chosen_action) == 3:
                print_stock()
            elif int(chosen_action) == 1:
                input_sale_data()
            break


def update_rental_worksheet(fname, lname, game, platform, format_date):
    """Updates the rentals worksheet

    Args:
        fname (str) : Customers first name

        lname (str) : Customers last name

        game (str) : The game the customer is trying to rent

        platform (str) : The platform (console type) the customer is trying 
            to rent

        format_date (datetime) : The date the rental is due back,
            formatted to DD/MM/YYYY
    """
    print("Updating rentals worksheet...")
    rental_data = [fname, lname, game, platform, format_date]
    worksheet_to_update = SHEET.worksheet("rentals")
    worksheet_to_update.append_row(rental_data)
    print("Worksheet updated successfully")


def calculate_return_date(fname, lname, game, platform):
    """Adds three days to todays date

    Args:
        fname (str) : Customers first name

        lname (str) : Customers last name

        game (str) : The game the customer is trying to rent

        platform (str) : The platform (console type) the customer is trying 
            to rent
    """
    today = datetime.datetime.now().date()
    return_date = today + datetime.timedelta(days=3)
    format_date = return_date.strftime("%d-%m-%Y")
    update_rental_worksheet(fname, lname, game, platform, format_date)


# MOVE INTO MAKE_CHOICE, 
def validate_chosen_action(chosen_action):
    """
    Inside the try, convert user input to an integer.
    Raises ValueError if input cannot be converted (ie, contains letter/s) 
    or if is not an integer between 1 and 5


    """
    """Checks chosen_action input was an integer between 1 and 5

    Args:
        chosen_action (int) : The input the user entered when choosing 
            an action

    Raises:
        ValueError : If chosen_action is not a full number between 1 and 5

    Notes:
        Converts chosen_Action to a string before testing for inclusion
    """
    try:
        if int(chosen_action) not in {1, 2, 3, 4, 5}:
            raise ValueError(
                "Must be a whole num between 1 and 5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True
    

def input_sale_data():
    """Asks user for customers first name, last name, game title and
      its platform (INDENT????????????????????????????????)

    Args:
        arg_name (data type) : Description of arg_name
            indent next line of description if need to

    Returns:
        SHOULD THE PRINT RETURN BE HERE, OR JUST EXPLICIT RETURNS??????????????????????????

    """
    # HAVE BELOW AS GLOBAL OR PASS BETWEEN FUNCTIONS??????????????????????????
    # global customer
    # global game
    # global platform
    fname = input("\nPlease enter the customer First Name:\n")
    lname = input("\nPlease enter the customer Last Name:\n")
    game = input("\nPlease enter the game title:\n")
    platform = input("\nPlease enter platform:\n")
    # ADD PLTFORM VALIDATION
    print(f"\nYou entered:\n First Name: {fname} \n Last Name: {lname} \n "
            f"Game: {game} \n Platform: {platform}")
    # ask for confirmation
    is_game_in_sheet(fname, lname, game, platform)


def check_stock(fname, lname, game, platform):
    """Checks the game to be rented is in stock

    Args:
        fname (str) : Customers first name

        lname (str) : Customers last name

        game (str) : The game the customer is trying to rent

        platform (str) : The platform (console type) the customer is trying 
            to rent
    """
    worksheet_stock = SHEET.worksheet("games").col_values(1)
    game_index = worksheet_stock.index(game) + 1
    worksheet_game_data = SHEET.worksheet("games").row_values(game_index)
    stock = worksheet_game_data[4]
    stock_int = int(stock)
    if stock_int <= 0:
        print("from 184, game not in stock")
    else:
        check_platform(fname, lname, game, platform, worksheet_game_data)
 


def check_customer_lname(fname, lname, game, platform, worksheet_game_data, fname_index):
    worksheet_lnames = SHEET.worksheet("customers").col_values(2)
    customer_lname = worksheet_lnames[fname_index]
    if customer_lname == lname:
        print("names match")
        calculate_return_date(fname, lname, game, platform)
    else:
        print("wrong last name")
   

def check_customer_fname(fname, lname, game, platform, worksheet_game_data):
    worksheet_fnames = SHEET.worksheet("customers").col_values(1)
    if fname not in worksheet_fnames:
        print("No record of customers First Name")
    else:
        fname_index = worksheet_fnames.index(fname)
        print(fname_index)
        check_customer_lname(fname, lname, game, platform, worksheet_game_data, fname_index)



def check_platform(fname, lname, game, platform, worksheet_game_data):
    """Description of what it does

    Args:
        fname (str) : Customers first name

        lname (str) : Customers last name

        game (str) : The game the customer is trying to rent

        platform (str) : The platform (console type) the customer is trying 
            to rent
    """
    worksheet_platform = worksheet_game_data[1]
    if worksheet_platform == platform:
        check_customer_fname(fname, lname, game, platform, worksheet_game_data)
    else:
        print("wrong platform")
  


def is_game_in_sheet(fname, lname, game, platform):
    """
    See if the game to be rented is in the games worksheet
    """

    """See if the game to be rented is in the games worksheet

    Args:
        fname (str) : Customers first name

        lname (str) : Customers last name

        game (str) : The game the customer is trying to rent

        platform (str) : The platform (console type) the customer is trying 
            to rent
    """
    worksheet_games = SHEET.worksheet("games").col_values(1)
    pprint(worksheet_games)
    if game in worksheet_games:
        print("GAME IS IN SHEET!!!!")
        check_stock(fname, lname, game, platform)
    else:
        print("game is not in sheet")
        

# IS THIS BEING USED???
# def get_game_id():
#     data_list = SHEET.worksheet("games").col_values(1)
#     id = data_list[-1]
#     print(f"game id is {id}")
#     update_rental_worksheet()


# NOT BEING USED, NEED ID_NuMBERS???????????????????????????????
# def get_customer_id():
#     data_list = SHEET.worksheet("customers").col_values(1)
#     id = data_list[-1]
#     print(f"customer id is {id}")
#     get_game_id()


def add_game():
    """Adds new game data to games worksheet if data is verified
    """
    while True:
        title = input("\nAdd game title:\n")
        platform = input("\nAdd platform:\n")
        genre = input("\nAdd genre:\n")
        min_age = input("\nAdd minimum age:\n")
        quantity = input("\nAdd how many:\n")

        new_game_info = [title, platform, genre, min_age, quantity]

        # REFRACTOR validate_add_customer AND validate_add_game INTO ONE FUNCTION?????
        if validate_add_game(new_game_info):
            print(f"\nYou entered...\n Title: {title}\n Platform: {platform}\n "
                  f"Genre: {genre}\n Minimum age: {min_age}\n "
                  f"How many: {quantity}\n")
            print("Is this correct?\n")
            confirm = input("Enter Y for yes, N for No\n")
            confirm_strip_lcase = confirm.strip().lower()
            if confirm_strip_lcase == "n":
                validate_add_game(new_game_info)
                print("from 339 confirm says no")
            elif confirm_strip_lcase == "y":
                update_worksheet(new_game_info, "games")
                break
          

def validate_add_game(new_game_info):
    """Checks all data has been entered and is valid

    Returns:
        bool : True if data validates, False if not
    """
    if not all(new_game_info):
        print("Missing element, please try again")
        return False
    if new_game_info[1] not in ("switch", "ps5", "xbox one"):
        print("Platform must be either switch, ps5 or xbox one. "
                    f"You entered {new_game_info[1]}")
        print("Please enter info again")
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
        try:
            if new_game_info[1] not in ("switch", "ps5", "xbox one"):  
                return False    
        except:
            print("Platform must be either switch, PS5 or xbox one. "
                    f"You entered {new_game_info[1]}")
                
        return True



def add_customer():
    """Gets user input for first name, last name, date of birth, display inputed data, ask for confirmation
    """
    while True:
        fname = input("\nAdd first name:\n")
        lname = input("\nAdd last name:\n")
        # give example of format
        dob = input("\nAdd date of birth\n")

        new_customer_info = [fname, lname, dob]

        if validate_add_customer(new_customer_info):
            print(f"\nYou entered...\n First Name: {fname}\n "
                  f"Last Name: {lname}\n "
                  f"Date of Birth: {dob}\n")
            print("Is this correct?\n")
            # ADD FUNCTION FOR THIS AND VALIDATE_ADD_GAME, DRY
            confirm = input("Enter Y for yes, N for No:\n")
            confirm_strip_lcase = confirm.strip().lower()
            if confirm_strip_lcase == "n":
                validate_add_customer(new_customer_info)
            elif confirm_strip_lcase == "y":
                update_worksheet(new_customer_info, "customers")
                break    



def validate_add_customer(new_customer_info):
    """Checks all data has been entered and is valid

    Returns:
        bool : True if data validates, False if not

    """
    while True:
        if not all(new_customer_info):
            print("Missing element, please try again")
            return False
        else:
            try:
                datetime.datetime.strptime(new_customer_info[2], "%d/%m/%Y")
            except:
                print("wrong date format!!!")
                return False 

        return True


# NOT USED, NEED????????????????????
# def create_id(worksheet):
#     """
#     Create id for column 1 in worksheet.
#     EXPLAIN THE LOGIC???
#     """
#     worksheet_to_update = SHEET.worksheet(worksheet)
#     get_id_list = worksheet_to_update.col_values(1)
#     if get_id_list == ["id"]:
#         new_id = 1
#     else:
#         last_id = get_id_list[-1]
#         new_id = int(last_id) + 1
#     return new_id



def update_worksheet(data, worksheet):
    """Updates a worksheet

    Args:
        data (list) : The data to input into the worksheet

        worksheet (str) : Name of the worksheet to update

    Returns:
        data_type : Optional description of return value
        Extra lines are not indented
    """
    if worksheet == "games":
        data[3] = int(data[3])
        data[4] = int(data[4])
    print(f"\nUpdating {worksheet} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    # id = create_id(worksheet)
    # data.insert(0, id)
    worksheet_to_update.append_row(data)
    print(f"\n{worksheet} updated successfully.")



def print_stock():
    """Pretty print the games worksheet to the terminal
    """
    stock = SHEET.worksheet("games").get_all_values()
    print("\n")
    pprint(stock)

if __name__ == "__main__":
   make_choice()

