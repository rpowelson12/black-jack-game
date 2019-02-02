import random

card_list = []

for value in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
    for suit in ["spades", "clubs", "hearts", "diamonds"]:
        card_list.append({"suit": suit, "value": value})

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
        if card["value"] in ['J', 'Q', 'K']:
            card_value += 10
        elif card["value"] == 'A':
            card_value += 11
        elif card["value"] in range(2, 11):
            card_value += card["value"]
    if card_value > 21:
        for ace in player_hand:
            if ace["value"] == "A":
                card_value -= 10

    return card_value


players_value = add_players_cards(0)


def add_dealers_cards(cards_value):
    cards_value = 0
    for card in dealer_hand:
        if card["value"] in ['J', 'Q', 'K']:
            cards_value += 10
        elif card["value"] == 'A':
            cards_value += 11
        elif card["value"] in range(2, 11):
            cards_value += card["value"]
    if cards_value > 21:
        for ace in dealer_hand:
            if ace["value"] == "A":
                cards_value -= 10
    return cards_value


dealers_value = add_dealers_cards(0)
add_players_cards(players_value)
print("This is the players hand: " + str(player_hand[0]["value"]) + " " + str(player_hand[0]["suit"]) + " and " +
      str(player_hand[1]["value"]) + " " + str(player_hand[1]["suit"]))
print("This is the dealers hand: " + str(dealer_hand[0]["value"]) + " " + str(dealer_hand[0]["suit"]))
print("This is the players cards value: " + str(players_value))

# ask for the action

player_action = ""
while players_value < 21 and player_action != "stay":
    if dealers_value == 21:
        print("This is the dealers hand: " + str(dealer_hand[0]["value"]) + " " + str(dealer_hand[0]["suit"]) + " and "
              + str(dealer_hand[1]["value"]) + " " + str(dealer_hand[1]["suit"]))
        print("This is the dealers value: " + str(dealers_value))
        print("Dealer wins!")
        break
    player_action = input("Would you like to hit or stay? ").lower()
    if player_action == "hit":
        new_player_card = card_list.pop(1)
        player_hand.append(new_player_card)
        players_value = add_players_cards(players_value)
        print(player_hand, "\n This is the players value: " + str(players_value))
if players_value > 21:
    print("Player busted, dealer wins")

while players_value <= 21 and dealers_value <= 21:

    if dealers_value > 17:
        break

    else:
        if len(player_hand) == 2 and players_value == 21 and dealers_value != 21:
            break
        new_dealer_card = card_list.pop(1)
        dealer_hand.append(new_dealer_card)
        dealers_value = add_dealers_cards(dealers_value)
        print("This is the dealers hand: " + str(dealer_hand[0]["value"]) + " " + str(dealer_hand[0]["suit"]) + " and "
              + str(dealer_hand[1]["value"]) + " " + str(dealer_hand[1]["suit"]))
        print("This is the dealers value: " + str(dealers_value))
        if dealers_value > 21:
            print("Dealer busted, player wins!")
            break

# compare the hands
if players_value and dealers_value <= 21:
    if players_value > 21:
        print("This is the dealers hand: " + str(dealer_hand[0]["value"]) + " " + str(dealer_hand[0]["suit"]) + " and "
              + str(dealer_hand[1]["value"]) + " " + str(dealer_hand[1]["suit"]))
    elif dealers_value > 21:
        print("Player wins!")
    elif dealers_value < players_value:
        print("Player wins!")
    elif dealers_value == players_value:
        print("It is a push")
    elif dealers_value > players_value:
        print("This is the dealers hand: " + str(dealer_hand[0]["value"]) + " " + str(dealer_hand[0]["suit"]) + " and "
              + str(dealer_hand[1]["value"]) + " " + str(dealer_hand[1]["suit"]))
        print("Dealer wins!")
