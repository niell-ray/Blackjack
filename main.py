import random as rand
from art import logo


# creating a function to generate a random card.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rand.choice(cards)
    return card


# function to calculate cards
def calculate_score(cards):
    # checking for blackjack score
    """take a list of cards and calculate the total"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, com_score):
    if u_score == com_score:
        return "Draw"
    elif com_score == 0:
        return "u lose, opponent has blackjack"
    elif u_score == 0:
        return "win with a blackjack"
    elif u_score > 21:
        return "u went over, u lost."
    elif com_score > 21:
        return " opponent went over, u win!"
    elif u_score > com_score:
        return " u win."
    else:
        return " u lose."


def play_game():
    print(logo)
    # list to store card data.
    user_cards = []
    computer_cards = []

    # just a value to understand whether the code is working according to requirement
    computer_score = -1
    user_score = -1

    is_game_over = False

    # need loop to run just twice, do not need the variable to store it.
    for _ in range(2):

        # adding cards to each player.
        user_cards.append(deal_card())
        computer_cards.append((deal_card()))

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, your score: {user_score}")
        print(f"computer's 1st card: {computer_cards[0]}")
        print("\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            print("\n")
            user_should_deal = input("type 'y' to hit or 'n' to stand: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, final score is: {user_score}")
    print(f"Computer's final hand is: {computer_cards}, computer score is: {computer_score}")
    print(compare(user_score, computer_score))
    print("\n")


while input("do u want to play a game of blackjack? type 'y' or 'n': ") == 'y':
    print("\n" * 50)
    play_game()
