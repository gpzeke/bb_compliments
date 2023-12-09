# Read and write user save information
import json

class ComplimentData:     # handles the persistance of user data
    def __init__(self, filename="compliments.json"):
        self.filename = filename

    def load_users(self):   # loads user data from file
        try:
            with open(self.filename, "r") as file:
                compliment_data = json.load(file)
                compliments = [ComplimentData(**data) for data in compliment_data]    # **data syntax is used to unpack the dictionary values as keyword arguments when creating the user object
                return compliments
        except FileNotFoundError:
            return []