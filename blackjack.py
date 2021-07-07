#blackjack
import random
#dealer Cards
import random

dealer_cards = []

#player_cards
player_cards = []

#dealer_cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

#Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

# Sum of Dealer Cards
if sum(dealer_cards) == 21 :
    print('Dealer has 21, he wins! ')
elif sum(dealer_cards) > 21:
    print("Dealer has busted! ")

#sum of player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit"))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards", player_cards)


    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " from these cards", dealer_cards)
        print(" YOu have a total of " + str(sum(player_cards)) + "with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins")
        else:
            print("Player wins")
        break


if sum(player_cards) > 21:
    print("Busted! Dealer wins")
elif sum(player_cards) == 21:
    print("21!")
    print("BlACKJACK, You win!")