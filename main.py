import randomizer, points, data_handler
from answers import correct_answer, false_answer


def main():
    data = data_handler.load_data()
    tally = 0
    for i in randomizer.randomizer(data["questions"]):
        question = list(data["questions"])[i]
        print(question)
        if correct_answer(input("Vad är det dit svar:"), data["questions"], question):
            print("Correct answer!")
            tally += 1
        else:
            print(f"Game over!")
            if tally > data["player_scores"]["ABBA"]:
                print(f'New highscore: {tally}')
            else:
                print(f'You got {tally} correct answers!')
            break
    data_handler.save_data(data)
if __name__ == "__main__":
    main()