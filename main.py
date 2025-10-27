import json
import os

users = {"nisse":"apa"}

menu1 = {"l":"Login", "c":"Create user", "q":"Quit"}
menu2 = {"r":"Try again", "q":"Quit"}
menu3 = {"p":"Play", "l":"Leaderboards", "q":"Quit"}
menu4 = {"d":"Animals", "f":"Movies", "m":"Mixed categories", "r":"Return to menu"}


def menu(title, prompt, options):
    print(title)
    for key, value in options.items():
        print(f"{key}: {value}")
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        else:
            print(f"{choice} is not a valid option.")

def adduser(users):
    print("Please enter your username: and select a password!")
    username = input("Username: ")
    if username in users:
        print(f"User {username} already exists")
        return
    password = input("Password: ")
    users[username] = password
    print(f"Welcome {username}, you have now created an account!|\n")

def login(users):
    while True:
        user = input("   User: ")
        password = input("Password: ")
        if user in users and password == users[user]:
            return user
        else:
            choice =menu("\nInvalid username or password\n", "\nOptions: ", menu2)
            if choice == "r":
                continue
            else:
                return None

def useractions(user):
    print(f"Welcome {user}!")
    while True:
        choice = menu("Select an option: ", "\nOption: ", menu3)
        if choice == "q":
            return "logout"
        elif choice == "p":
            val = menu("Chose a category to play", "\nOption: ", menu4)
            if val == "r":
                continue
            pass #Lägg till funktion för spelet.
        elif choice == "l":
            pass #lägg till funktion för leaderboards.

def main():
    while True:
        choice = menu("Login menu", "\nOption: ", menu1)
        if choice == "q":
            print("Goodbye!")
            break
        elif choice == "l":
            user = login(users)
            if user: #Om inloggningen lyckas, annars skulle uttrycket varit falskt.
                if useractions(user) == "logout":
                    print("Goodbye!")
                    break
        elif choice == "c":
            adduser(users)

main()