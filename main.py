import randomizer, points, data_handler, menu
from answers import correct_answer, false_answer


def main():
    data = data_handler.load_data()
    while True:
        choice = menu.main_menu("Login Menu", "\nOption: ", data["login_meny"])
        if choice == 'q':
            break
        elif choice == 'l':
            user = menu.login(data["användare"])
            if user:
                while menu.useractions(user) == 'play':
                    data["player_scores"][user] = menu.spel(menu.main_menu("Välj kategori", "\n Option ", data["spel_meny"]))
            elif menu.useractions(user) == "logout":
                break
        elif choice == 'c':
            data_handler.save_data(menu.adduser(data))




if __name__ == "__main__":
    main()

