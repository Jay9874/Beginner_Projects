
import random

start_over = True
while start_over:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    first_cards = []
    com_first_cards = []
    player_score = 0
    com_score = 0

    def first_two_card():
        """Returns two random cards from deck."""
        for i in range(2):
            first_cards.append(random.choice(cards))
            com_first_cards.append(random.choice(cards))

    def player_first_hand():
        global player_score
        first_two_card()
        com_first_hand()
        player_score += cal_score(first_cards)
        print(f"  Your card: {first_cards}, current score: {player_score}")
        return player_score

    def com_first_hand():
        global com_score
        com_score += cal_score(com_first_cards)
        return com_score

    def cal_score(chosen_cards):
        score = sum(chosen_cards)
        return score

    def another_card():
        global player_score
        global com_score
        first_cards.append(random.choice(cards))
        com_first_cards.append(random.choice(cards))
        player_score = cal_score(first_cards)
        com_score = cal_score(com_first_cards)
        print(f"  Your card: {first_cards}, current score: {player_score}")

    def result():
        print(f"  Your final hand: {first_cards}, final score: {player_score}")
        print(
            f"  Computer's final hand: {com_first_cards}, final score: {com_score}"
        )

    check = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if check == "y":
        player_first_hand()
        print(f"  Computer's first card: {com_first_cards[0]}")
        should_continue = True
        while should_continue:
            if player_score > 21:
                result()
                print("You went over 21. You lost.😫")
                should_continue = False
            else:
                want_new_card = input(
                    "Type 'y' to get another card, type 'n' to pass: ")
                if want_new_card == "y":
                    another_card()
                    print(f"  Computer's first card: {com_first_cards[0]}")
                elif want_new_card == "n":
                    if com_score > player_score and com_score <= 21:
                        result()
                        print("Computer won 🖥 💪.")
                        should_continue = False
                    else:
                        result()
                        print("You won😇🤩.")
                        should_continue = False

    elif check == "n":
        start_over = False
        print("Thank you for playing.")
