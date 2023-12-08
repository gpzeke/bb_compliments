# Define the user profile

class User:
    def __init__(self, first_name, last_name, nickname, date_of_birth, preferred_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.date_of_birth = date_of_birth
        self.preferred_name = nickname or first_name