import random


card_list = ['A spades', 'A clubs', 'A diamonds', 'A hearts',
             '2 spades', '2 clubs', '2 diamonds', '2 hearts',
             '3 spades', '3 clubs', '3 diamonds', '3 hearts',
             '4 spades', '4 clubs', '4 diamonds', '4 hearts',
             '5 spades', '5 clubs', '5 diamonds', '5 hearts',
             '6 spades', '6 clubs', '6 diamonds', '6 hearts',
             '7 spades', '7 clubs', '7 diamonds', '7 hearts',
             '8 spades', '8 clubs', '8 diamonds', '8 hearts',
             '9 spades', '9 clubs', '9 diamonds', '9 hearts',
             '10 spades', '10 clubs', '10 diamonds', '10 hearts',
             'J spades', 'J clubs', 'J diamonds', 'J hearts',
             'Q spades', 'Q clubs', 'Q diamonds', 'Q hearts',
             'K spades', 'K clubs', 'K diamonds', 'K hearts']

random.shuffle(card_list)

# creating all global variables
player_hand = []
dealer_hand = []


# deal the cards
def deal_cards():
    while len(player_hand) == len(dealer_hand) and len(player_hand) < 2:
        new_player_card = card_list.pop(1)
        player_hand.append(new_player_card)
        new_dealer_card = card_list.pop(1)
        dealer_hand.append(new_dealer_card)


deal_cards()
# add the cards


def add_players_cards(card_value):
    card_value = 0
    for card in player_hand:
        if card == "A spades" or card == "A hearts" or card == "A clubs" or card == "A diamonds":
            card_value = card_value + 11
        elif card == "2 hearts" or card == "2 diamonds" or card == "2 spades" or card == "2 clubs":
            card_value = card_value + 2
        elif card == "3 hearts" or card == "3 diamonds" or card == "3 spades" or card == "3 clubs":
            card_value = card_value + 3
        elif card == "4 hearts" or card == "4 diamonds" or card == "4 spades" or card == "4 clubs":
            card_value = card_value + 4
        elif card == "5 hearts" or card == "5 diamonds" or card == "5 spades" or card == "5 clubs":
            card_value = card_value + 5
        elif card == "6 hearts" or card == "6 diamonds" or card == "6 spades" or card == "6 clubs":
            card_value = card_value + 6
        elif card == "7 hearts" or card == "7 diamonds" or card == "7 spades" or card == "7 clubs":
            card_value = card_value + 7
        elif card == "8 hearts" or card == "8 diamonds" or card == "8 spades" or card == "8 clubs":
            card_value = card_value + 8
        elif card == "9 hearts" or card == "9 diamonds" or card == "9 spades" or card == "9 clubs":
            card_value = card_value + 9
        elif card == "10 hearts" or card == "10 diamonds" or card == "10 spades" or card == "10 clubs":
            card_value = card_value + 10
        elif card == "J hearts" or card == "J diamonds" or card == "J spades" or card == "J clubs":
            card_value = card_value + 10
        elif card == "Q hearts" or card == "Q diamonds" or card == "Q spades" or card == "Q clubs":
            card_value = card_value + 10
        elif card == "K hearts" or card == "K diamonds" or card == "K spades" or card == "K clubs":
            card_value = card_value + 10
    if card_value > 21:
        for ace in player_hand:
            if ace == "A spades" or ace == "A hearts" or ace == "A clubs" or ace == "A diamonds":
                card_value = card_value - 10
    return card_value


players_value = add_players_cards(0)


def add_dealers_cards(cards_value):
    cards_value = 0
    for cards in dealer_hand:
        if cards == "A spades" or cards == "A hearts" or cards == "A clubs" or cards == "A diamonds":
            cards_value = cards_value + 11
        elif cards == "2 hearts" or cards == "2 diamonds" or cards == "2 spades" or cards == "2 clubs":
            cards_value = cards_value + 2
        elif cards == "3 hearts" or cards == "3 diamonds" or cards == "3 spades" or cards == "3 clubs":
            cards_value = cards_value + 3
        elif cards == "4 hearts" or cards == "4 diamonds" or cards == "4 spades" or cards == "4 clubs":
            cards_value = cards_value + 4
        elif cards == "5 hearts" or cards == "5 diamonds" or cards == "5 spades" or cards == "5 clubs":
            cards_value = cards_value + 5
        elif cards == "6 hearts" or cards == "6 diamonds" or cards == "6 spades" or cards == "6 clubs":
            cards_value = cards_value + 6
        elif cards == "7 hearts" or cards == "7 diamonds" or cards == "7 spades" or cards == "7 clubs":
            cards_value = cards_value + 7
        elif cards == "8 hearts" or cards == "8 diamonds" or cards == "8 spades" or cards == "8 clubs":
            cards_value = cards_value + 8
        elif cards == "9 hearts" or cards == "9 diamonds" or cards == "9 spades" or cards == "9 clubs":
            cards_value = cards_value + 9
        elif cards == "10 hearts" or cards == "10 diamonds" or cards == "10 spades" or cards == "10 clubs":
            cards_value = cards_value + 10
        elif cards == "J hearts" or cards == "J diamonds" or cards == "J spades" or cards == "J clubs":
            cards_value = cards_value + 10
        elif cards == "Q hearts" or cards == "Q diamonds" or cards == "Q spades" or cards == "Q clubs":
            cards_value = cards_value + 10
        elif cards == "K hearts" or cards == "K diamonds" or cards == "K spades" or cards == "K clubs":
            cards_value = cards_value + 10
    if cards_value > 21:
        for aces in dealer_hand:
            if aces == "A spades" or aces == "A hearts" or aces == "A clubs" or aces == "A diamonds":
                cards_value = cards_value - 10
    return cards_value


dealers_value = add_dealers_cards(0)


add_players_cards(players_value)
print("This is the players hand: " + str(player_hand))
print("This is the dealers hand: " + str(dealer_hand[1]))
print("This is the players cards value: " + str(players_value))

# ask for the action

player_action = ""
while players_value < 21 and player_action != "stay":
    player_action = input("Would you like to hit or stay? ").lower()
    if player_action == "hit":
        new_player_card = card_list.pop(1)
        player_hand.append(new_player_card)
        players_value = add_players_cards(players_value)
        print(player_hand, players_value)
if players_value > 21:
    print("Player busted, dealer wins")


while dealers_value < 17:
    new_dealer_card = card_list.pop(1)
    dealer_hand.append(new_dealer_card)
    dealers_value = add_dealers_cards(dealers_value)
    print("This is the dealers hand: " + str(dealer_hand))
    print("This is the dealers valuer: " + str(dealers_value))
if dealers_value > 21:
    print("Dealer busted, player wins!")


# compare the hands
if dealers_value > 21:
    print("Player wins!")
elif dealers_value < players_value:
        print("Player wins!")
elif player_hand > 21:
        print("Dealer wins!")
else:
    print("Dealer wins!")










