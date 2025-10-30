import json
import os

users = {"nisse":"apa"}

menu1 = {"l":"Login", "c":"Create user", "q":"Quit"}
menu2 = {"r":"Try again", "q":"Quit"}
menu3 = {"p":"Play", "l":"Leaderboards", "q":"Quit"}
menu4 = {"a":"Animals", "m":"Movies", "b":"Mixed categories", "r":"Return to menu"}


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

def correct_answer(answer: str  ,questions: dict,question: str): # tar in svar = str, dict = frågebateri och frågan ur den slumpade lsitan = str
    if answer.lower().strip() == questions[question].lower().strip():
        return True
    else:
        return False

def false_answer(answer, questions, question): # egentligen överflödig, kan lika gärna använda not correct_answer
    if not correct_answer(answer, questions, question):
        return True
    else:
        return False

def spel(kategori):
    data = data_handler.load_data()
    tally = 0
    for i in randomizer.randomizer(data["djur"]):
        question = list(data[djur])[i]
        nuvarande_fråga = tally + 1
        print(f"Fråga: {nuvarande_fråga}\n{question}")
        if correct_answer(input("Vad är dit svar: "), data["djur"], question):
            print("Correct answer!")
            tally += 1
        else:
            print(f"Wrong! Correct answer: {data['djur'][question]}")
            print("Game over!")
            if tally > data["player_scores"]:
                print(f"New highsore {tally}")
            else:
                print(f"You got {tally} correct answers!")
            return tally
    data_handler.save_data(data)

def useractions(user):
    print(f"Welcome {user}!")
    while True:
        choice = menu("Select an option: ", "\nOption: ", menu3)
        if choice == "q":
            return "logout"
        elif choice == "p":
            val = menu("Chose a category to play", "\nOption: ", menu4)
            if val == "d":
                spel("Animals")
            elif val == "f":
                spel("Film")
            elif val == "m":
                spel("Mixed categories")
            elif val == "r":

        elif choice == "s":
            return "scoreboards"

