import randomizer, points, data_handler, menu


def main():
    data = data_handler.load_data()
    while True:
        choice = menu.main_menu("Login Menu", "\nOption: ", data["login_meny"])

        if choice == 'q':
            break

        elif choice == 'l':
            user = menu.login(data["användare"])
            if not user:
                continue  # tillbaka till login-menyn

            # inloggad användarslinga
            while True:
                action = menu.useractions(user)  # t.ex. 'play', 'logout', 'back'
                if action == 'play':
                    kategori = menu.main_menu("Välj kategori", "\nOption: ", data["spel_meny"])
                    tally = menu.spel(kategori)            # <-- fånga poängen
                    old = data["player_scores"].get(user, 0)
                    data["player_scores"][user] = max(old, tally) # <-- spara
                    data_handler.save_data(data)
                    print(f"Du fick {tally} poäng!")
                elif action == 'logout':
                    break
                elif action == 'scoreboards':
                    print(f'Sorterat efter poäng: {points.sort_by_point(data["player_scores"])} ')
                    print(f'Sorterat efter namn: {points.sort_by_name(data["player_scores"])} ')
                elif action in ('back', None):
                    # tillbaka till huvudmenyn
                    break

        elif choice == 'c':
            data_handler.save_data(menu.adduser(data))
if __name__ == "__main__":
    main()