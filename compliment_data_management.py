# Read and compliment data
import json
import random
from datetime import datetime

class Compliment:
    def __init__(self, type, expression):
        self.type = type
        self.expression = expression

    def __str__(self):
        return self.expression

class ComplimentData:     # handles persistance of compliment data
    def __init__(self, filename="compliments.json"):
        self.filename = filename
        self.compliments = self.load_compliments()

    def load_compliments(self):   # loads compliment data from file
        try:
            with open(self.filename, "r") as file:
                compliment_data = json.load(file)
                compliments = [Compliment(**data) for data in compliment_data]    # **data syntax is used to unpack the dictionary values as keyword arguments when creating the compliment object
                return compliments
        except FileNotFoundError:
            return []

    def current_season(self):
        now = datetime.now()
        month = now.month

        if 3 <= month <= 5:
            return "spring"
        elif 6 <= month <= 8:
            return "summer"
        elif 9 <= month <= 11:
            return "autumn"
        else:
            return "winter"

    def random_compliment(self):
        current_season = self.current_season()
        valid_types = ["spring","summer","autumn","winter","generic"]

        filtered_compliments = [compliment for compliment in self.compliments if compliment.type == "generic" or compliment.type == current_season]
            # returning a list of compliments that consists of type generic and the relevant season
            
        if not filtered_compliments:
            raise ValueError(f"No compliments found of type {current_season}")

        return random.choice(filtered_compliments)