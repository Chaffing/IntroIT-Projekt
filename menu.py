import data_handler, answers, randomizer

data = data_handler.load_data()

def spel(kategori):
    tally = 0
    for i in randomizer.randomizer(data[kategori]):
        question = list(data[kategori])[i]
        print(question)
        if answers.correct_answer(input("Vad är det dit svar:"), data[kategori], question):
            print("Correct answer!")
            tally += 1
        elif not answers.correct_answer(question, data[kategori], question):
            print("Game Over!")
            return tally


def main_menu(title, prompt, options):
    print(title)
    for key, value in options.items():
        print(f"{key}: {value}")
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        else:
            print(f"{choice} is not a valid option.")

def adduser(data):
    print("Please enter your username and select a password!")
    username = input("Username: ")

    users = data.get("användare", {})

    if username in users:
        print(f"User {username} already exists")
        return data  # viktigt: returnera oförändrad data

    password = input("Password: ")
    users[username] = password

    data["användare"] = users  # sätt tillbaka (om users inte fanns innan)
    data["player_scores"][username]= 0
    print(f"Welcome {username}, you have now created an account!\n")

    return data  # returnera uppdaterad data



def login(users):
    while True:
        user = input("   User: ")
        password = input("Password: ")
        if user in users and password == users[user]:
            return user
        else:
            choice =main_menu("\nInvalid username or password\n", "\nOptions: ", data["försök_igen_meny"])
            if choice == "r":
                continue
            else:
                return None

def useractions(user):
    print(f"Welcome {user}!")
    while True:
        choice = main_menu("Select an option: ", "\nOption: ", data["huvud_meny"])
        if choice == "q":
            return "logout"
        elif choice == "p":
            return "play"
        elif choice == "s":
            return 'scoreboards'