# Read and write user save information
import json
from user import User

class UserData:     # handles the persistance of user data
    def __init__(self, filename="users.json"):
        self.filename = filename

    def save_users(self, users):    # saves a list of user objects
        with open(self.filename, "w") as file:  # with ensure closes properly after execution
            user_data = [
                {   "first_name": user.first_name,
                    "last_name":user.last_name,
                    "nickname":user.nickname,
                    "date_of_birth":user.date_of_birth,
                    "preferred_name":user.preferred_name
                }
                        for user in users
            ]  # creates a list [] of dictionaries {}
            json.dump(user_data, file, indent=4)  # serializes user_data and writes to file

    def load_users(self):   # loads user data from file
        try:
            with open(self.filename, "r") as file:
                user_data = json.load(file)
                users = [User(**data) for data in user_data]    # **data syntax is used to unpack the dictionary values as keyword arguments when creating the user object
                return users
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []