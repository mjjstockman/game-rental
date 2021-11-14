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


# PUT CUST INFO IN RENTAL
# LIBRARY TO PRINT TABLES


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
    

        # HOW TIDT UP, BRIAN??
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


def update_rental_worksheet():
    worksheet_to_update = SHEET.worksheet("rentals")
    # id = create_id(worksheet)


def validate_chosen_action(chosen_action):
    """
    Inside the try, convert user input to an integer.
    Raises ValueError if input cannot be converted (ie, contains letter/s) 
    or if is not an integer between 1 and 5
    """
    try:
        # USE A SET
        # if int(chosen_action) not in set[(1, 2, 3, 4, 5)]:
        if int(chosen_action) not in (1, 2, 3, 4, 5):
            raise ValueError(
                "Must be a whole num between 1 and 5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True
    

def input_sale_data():
    # HAVE BELOW AS GLOBAL OR PASS BETWEEN FUNCTIONS??
    # global customer
    # global game
    fname = input("Please enter the customer First Name:\n")
    lname = input("Please enter the customer Last Name:\n")
    game = input("Please enter the game title:\n")
    print(f"You entered:\n First Name: {fname} \n Last Name: {lname} \n "
            f" Game: {game}")
    # ask for confirmation
    check_game_data(fname, lname, game)


def check_customer_data(fname, lname):
    """
    only checking fname
    """
    worksheet_fname = SHEET.worksheet("customers").col_values(2)
    pprint(worksheet_fname)
    if fname in worksheet_fname:
        print("first name IS IN SHEET!!!")
    else:
        print("first name not in sheet")


def is_game_in_sheet(game):
    """
    Get stock of entered game
    """
    worksheet_games = SHEET.worksheet("games").col_values(2)
    pprint(worksheet_games)
    try:
        game_index = worksheet_games.index(game)
    except:
        print("game is not in list")
    






    # ["foo", "bar", "baz"].index("bar")
    # IN PYTHON FIND GAME IN LIST
    # GET IT'S INDEX NUMBER IN LIST
    # FIND ROW NUMBER
    # GET ALL VALUES
    # CHECK STOCK COLUMN



    # get game in column
    # games = SHEET.worksheet("games").col_values(2)
    # cell = games.find(game) #Find a cell with exact string value
    # print("Text found at R%sC%s" % (cell.row, cell.col))



def check_game_data(fname, lname, game):
    """
    Check the game title is in games worksheet
    """
    games = SHEET.worksheet("games").col_values(2)
    if game in games:
        print("GAME IS IN SHEET!!!")
        # REANAME BELOW FUNCTION
        check_game_is_in_sheet(game)
    else:
        print("WE DONT HAVE THAT GAME")
        

def get_game_id():
    data_list = SHEET.worksheet("games").col_values(1)
    id = data_list[-1]
    print(f"game id is {id}")
    update_rental_worksheet()


def get_customer_id():
    data_list = SHEET.worksheet("customers").col_values(1)
    id = data_list[-1]
    print(f"customer id is {id}")
    get_game_id()

# get_customer_id()

def get_sale_info():
    global customer
    global game
    fname = input("Please enter the customer First Name:\n")
    lname = input("Please enter the customer Last Name:\n")
    game = input("Please enter the game title:\n")
    print(f"You entered:\n First Name: {fname} \n Last Name: {lname} \n"
        f"Game: {game}")
    # ask for confirmation
    get_customer_id()

# get_sale_info()


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

        # REFRACTOR validate_add_customer AND validate_add_game INTO ONE FUNCTION?????
        if validate_add_game(new_game_info):
            print(f"\nYou entered...\n Title: {title}\n Platform: {platform}\n "
                  f"Genre: {genre}\n Minimum age: {min_age}\n "
                  f"How many: {quantity}\n")
            print("Is this correct?\n")
            confirm = input("Enter Y for yes, N for No\n")
            if confirm == "N" or confirm == "n":
                validate_add_game(new_game_info)
            elif confirm == "Y" or confirm == "y":
                update_worksheet(new_game_info, "games")
                break
            

def validate_add_game(new_game_info):
    """
    Check that all fields have been entered.
    Inside the try, convert min_age and quantity to an integer.
    If they cannot be converted (ie, contains letter/s) print error message
    and continue to run add_game() 
    
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
    while True:
        fname = input("Add first name\n")
        lname = input("Add last name\n")
        dob = input("Add date of birth\n")

        new_customer_info = [fname, lname, dob]

        if validate_add_customer(new_customer_info):
            print(f"\nYou entered...\n First Name: {fname}\n "
                  f"Last Name: {lname}\n "
                  f"Date of Birth: {dob}\n")
            print("Is this correct?\n")
            confirm = input("Enter Y for yes, N for No\n")
            if confirm == "N" or confirm == "n":
                validate_add_customer(new_customer_info)
            elif confirm == "Y" or confirm == "y":
                # print("Please renter the correct details")
                update_worksheet(new_customer_info, "customers")
                break    


def validate_add_customer(new_customer_info):
    """
    Check that all fields have been entered.
    Inside the try, convert min_age and quantity to an integer.
    If they cannot be converted (ie, contains letter/s) print error message
    and continue to run add_game() 
    
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


def create_id(worksheet):
    """
    Create id for column 1 in worksheet.
    EXPLAIN THE LOGIC???
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    get_id_list = worksheet_to_update.col_values(1)
    if get_id_list == ["id"]:
        new_id = 1
    else:
        last_id = get_id_list[-1]
        new_id = int(last_id) + 1
    return new_id



def update_worksheet(data, worksheet):
    if worksheet == "games":
        data[3] = int(data[3])
        data[4] = int(data[4])
    print(f"Updating {worksheet} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    id = create_id(worksheet)
    data.insert(0, id)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully.\n")



def print_stock():
    """
    Pretty print the games worksheet to the terminal
    """
    stock = SHEET.worksheet("games").get_all_values()
    pprint(stock)


