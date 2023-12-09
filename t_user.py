from user_creation import create_user
from user_data_management import UserData

def main():
    # Create a user
    new_user = create_user()

    # Store with our data handler
    user_data_handler = UserData()
    users = user_data_handler.load_users()
    users.append(new_user)
    user_data_handler.save_users(users)

    print("User created successfully:")
    print(f"User: {new_user.nickname}")
    print(f"Full Name: {new_user.first_name} {new_user.last_name}")
    print(f"Date of Birth: {new_user.date_of_birth}")
    print(f"Preferred Name: {new_user.preferred_name}")

if __name__ == "__main__":
    main()