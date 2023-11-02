import random

fps = 60
#Variables


global players_cards
global dealers_cards
global values
global player_wins

def game():
    cards = ['A', 'A', 'A', 'A',
             2, 2, 2, 2,
             3, 3, 3, 3,
             4, 4, 4, 4,
             5, 5, 5, 5,
             6, 6, 6, 6,
             7, 7, 7, 7,
             8, 8, 8, 8,
             9, 9, 9, 9,
             10, 10, 10, 10,
             'J', 'J', 'J', 'J',
             'Q', 'Q', 'Q', 'Q',
             'K', 'K', 'K', 'K']
    def deal_intitial_dealer():
        dealer_holder = []

        card_range = len(cards) - 1
        position = random.randrange(card_range)
        dealer_holder.append(cards[position])
        del cards[position]

        card_range = len(cards) - 1
        position = random.randrange(card_range)
        dealer_holder.append(cards[position])
        del cards[position]

        return dealer_holder

    def deal_intitial_player():
        player_holder = []

        card_range = len(cards) - 1
        position = random.randrange(card_range)
        player_holder.append(cards[position])
        del cards[position]

        card_range = len(cards) - 1
        position = random.randrange(card_range)
        player_holder.append(cards[position])
        del cards[position]

        return player_holder

    def hit(list, list1):
        card_range = len(cards) - 1
        position = random.randrange(card_range)
        list.append(cards[position])
        list1.append(cards[position])
        del cards[position]
        return list

    def value_assignment(list):
        for position in range(len(list)):
            if list[position] == "K":
                list[position] = 10
            if list[position] == "Q":
                list[position] = 10
            if list[position] == "J":
                list[position] = 10
            if list[position] == "A" and list != dealer_value:
                if len(list) < 3:
                    list[position] = 11
                if len(list) >= 3:
                    list[position] = 1
            if list[position] == "A" and list == dealer_value:
                list[position] = 11
        return list

    def total(list):
        total = 0
        for position in range(len(list)):
            total = total + int(list[position])
        return total

    players_cards = deal_intitial_player()
    dealers_cards = deal_intitial_dealer()

    running = True
    print("----------------------------------")
    print("Dealer: " + str(dealers_cards[0]) + ", hidden")
    print("Your hand:")
    print(players_cards)

    player_value = []
    play_values = []
    for x in range(len(players_cards)):
        player_value.append(players_cards[x])

    dealer_value = []
    deal_values = []
    for x in range(len(dealers_cards)):
        dealer_value.append(dealers_cards[x])

    play_values = value_assignment(player_value)
    deal_values = value_assignment(dealer_value)

    while running:
        checker = 0
        condition = True
        player_total = total(play_values)
        dealer_total = total(deal_values)
        checker = player_total

        if checker <= 17:
            players_cards = hit(players_cards, player_value)
            play_values = value_assignment(player_value)
            player_total = total(play_values)
            checker = player_total
            if checker > 21:
                condition = False
            print("----------------------------------")
            print("Dealer: ")
            print(str(dealers_cards[0]) + ", hidden")
            print(" ")
            print("Your hand:")
            print(players_cards)
            print(player_total)

        if checker > 17 or condition == False:
            player_total = total(play_values)
            dealer_total = total(deal_values)
            if dealer_total < 17:
                dealers_cards = hit(dealers_cards, dealer_value)
                deal_values = value_assignment(dealer_value)
                dealer_total = total(deal_values)
                print("----------------------------------")
                print("Dealer: ")
                print(dealers_cards)
                print("Dealer's total " + str(dealer_total))
                print(" ")
                print("Your hand:")
                print(players_cards)
                print("Your total " + str(player_total))
            if dealer_total >= 17:
                print("----------------------------------")
                print("Dealer: ")
                print(dealers_cards)
                print("Dealer's total " + str(dealer_total))
                print(" ")
                print("Your hand:")
                print(players_cards)
                print("Your total " + str(player_total))

            if dealer_total > player_total and dealer_total <= 21:
                print("YOU LOSE")
                return 0
            if dealer_total <= player_total and player_total <= 21:
                print("YOU WIN")
                return 1
            if dealer_total == player_total and player_total <= 21:
                print("YOU WIN")
                return 1
            if dealer_total > 21 and player_total <= 21:
                print("YOU WIN")
                return 1
            if player_total > 21:
                print("YOU LOSE")
                return 0
            if condition == False:
                print("YOU LOSE")
                return 0

            running = False

again = True

player_wins = 0
def reloop(num):
    wins = 0
    for x in range(num):
        holder = int(game())
        wins = wins + holder
    return wins

y = int(input("How many simulations?"))
player_wins = reloop(y)
print("")
print("Player wins: " + str(player_wins))
print("Dealer wins: " + str(y-player_wins))
print("Win percentage: " + str(player_wins/y))

