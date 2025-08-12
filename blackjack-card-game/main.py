from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
start_game = True
def score(cards):
    score = 0
    for card in cards:
        score += card
    return score

while start_game:
    play_the_game = input("~~~~~~~Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_the_game == 'n':
        start_game = False
        break
    else :
 
        player_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]

        print(f"   Your cards: {player_cards}, current score: {score(player_cards)}")
        print(f"   Computer's first card: {computer_cards[0]}")
        
        game_end =False
        while not game_end:
            get_another_cards = input("\nType 'y' to get another card, type 'n' to pass: ")

            if get_another_cards == "y":
                player_cards.append(random.choice(cards))
                print(f"   Your cards: {player_cards}, current score: {score(player_cards)}")
                print(f"   Computer's first card: {computer_cards[0]}")
                if score(player_cards) > 21 :
                    print(f"\nYou went over. You lose! 😒\n\n")
                    game_end = True
                elif score(computer_cards) == 21 :
                    print("\nYou win 😁\n\n")
                    game_end = True
            else:
           
                while (score(computer_cards)) < 17:
                    computer_cards.append(random.choice(cards))

                print(f"   Your final hand: {player_cards}, final score: {score(player_cards)}")
                print(f"   Computer's final hand: {computer_cards}, final score: {score(computer_cards)}")

                if (score(computer_cards)) > 21:
                    print("\nOpponent went over. You win! 😍\n\n")
                    game_end = True
                elif (score(computer_cards)) <= 21 and (score(computer_cards)) > (score(player_cards)):
                    print("\nComputer Won! 😊\n\n")
                    game_end = True
                elif (score(computer_cards)) == (score(player_cards)):
                    print("\nGame Draw! 📍\n\n")
                    game_end = True
                else:
                    print("\nYou won! 😁\n\n")
                    game_end = True

