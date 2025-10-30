import data_handler, answers, randomizer

menyer = data_handler.load_data()
data = data_handler.load_data()

def spel(kategori):
    tally = 0
    for i in randomizer.randomizer(data[kategori]):
        question = list(data[kategori])[i]
        print(question)
        if answers.correct_answer(input("Vad är det dit svar: "), data[kategori], question):
            print("Rätt svar!")
            tally += 1
        elif not answers.correct_answer(question, data[kategori], question):
            print(f"Game Over! Rätt svar var {data[kategori][question]}!")
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
            print(f"{choice} är inte ett giltigt alternativ.")

def adduser(data):
    print("Ange ditt användarnamn och lösenord!")
    username = input("Användarnamn: ")

    users = data.get("användare", {})

    if username in users:
        print(f"Användaren {username} finns redan")
        return data  # viktigt: returnera oförändrad data

    password = input("Lösenord: ")
    users[username] = password

    data["användare"] = users  # sätt tillbaka (om users inte fanns innan)
    data["player_scores"][username]= 0
    print(f"Välkommen {username}, du har nu skapat ditt användarkonto!\n")

    return data  # returnera uppdaterad data



def login(users):
    while True:
        user = input("   Användare: ")
        password = input("Lösenord: ")
        if user in users and password == users[user]:
            return user
        else:
            choice = main_menu("\nOgiltig användare eller lösenord\n", "\nAlternativ: ", menyer["försök_igen_meny"])
            if choice == "r":
                continue
            else:
                return None

def useractions(user):
    print(f"Välkommen {user}!")
    while True:
        choice = main_menu("Välj ett alternativ: ", "\nAlternativ: ", menyer["huvud_meny"])
        if choice == "q":
            return "logout"
        elif choice == "p":
            return "play"
        elif choice == "s":
            return 'scoreboards'

