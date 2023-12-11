# Create a user
from user import User
from datetime import datetime

def create_user():
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    nickname = input("What is your nickname?\n")

    while True:
        date_of_birth = input("When were you born (YYYY-MM-DD)?\n")

        try:
            datetime.strptime(date_of_birth, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format, please enter the date in YYYY-MM-DD format.")

    while True:
        print("Would you like me to refer to you by your first name or your nickname?")
        print("1) First Name")
        print("2) Nickname")

        preference_choice = input("Please enter the number of your selection: ")
    
        if preference_choice in ('1', '2'):
            break
        else:
            print("Invalid selection, please enter 1 or 2.")
    preferred_name = first_name if preference_choice == '1' else nickname
    
    return User(
    first_name=first_name,
    last_name=last_name,
    nickname=nickname,
    date_of_birth=date_of_birth,
    preferred_name=preferred_name
)