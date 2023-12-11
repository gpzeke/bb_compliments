import tkinter as tk
from tkinter import messagebox
from user_creation import create_user
from user_data_management import UserData
from compliment_data_management import ComplimentData

def show_compliment():
    compliment_data = ComplimentData()
    compliment = compliment_data.random_compliment()
    messagebox.showinfo("Compliment", compliment.expression)

def main():
    root = tk.Tk()

    users_data = UserData()
    users = users_data.load_users()

    if not users:
        # No users found, create a new user
        user = create_user()
        if user:
            users = [user]
            users_data.save_users(users)
        else:
            # User creation failed, exit
            root.destroy()
            return

    # Display a compliment
    show_compliment()

    root.destroy()  # Close the window after displaying the compliment

if __name__ == "__main__":
    main()