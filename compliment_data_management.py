# Read and compliment data
import json
import random

class Compliment:
    def __init__(self, type, expression):
        self.type = type
        self.expression = expression

class ComplimentData:     # handles persistance of compliment data
    def __init__(self, filename="compliments.json"):
        self.filename = filename
        self.compliments = self.load_compliments()

    def load_compliments(self):   # loads compliment data from file
        try:
            with open(self.filename, "r") as file:
                compliment_data = json.load(file)
                compliments = [ComplimentData(**data) for data in compliment_data]    # **data syntax is used to unpack the dictionary values as keyword arguments when creating the compliment object
                return compliments
        except FileNotFoundError:
            return []

    def random_compliment(self, type_select):
        valid_types = ["spring","summer","autumn","winter","generic"]

        if type_select not in valid_types:
            raise ValueError("Invalid type.")

        filtered_compliments = [compliment for compliment in self.compliments if compliment.type == "generic" or compliment.type == type_select]
            # returning a list of compliments that consists of type generic and the relevant season
            
        if not filtered_compliments:
            raise ValueError(f"No compliments found of type {type_select}")

        return random.choice(filtered_compliments)