import random

#Varriables needed to track the decks
global players_cards
global dealers_cards
global values

balance = 0

def main():
    #Opens a balance
    with open('balance.txt', 'r') as fp:
        bal = fp.read()
    balance = float(bal)
    print("Balance: " + str(balance))

    bet = int(input("How much to bet?"))
    balance = balance - bet
    winnings = 0
    print("Balance: " + str(balance))

    #Card bank
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

    #deals the intital two cards for the dealer
    #follows Vegas rules with only one card showing
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

    #deals the players initial deck
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

    #Function used to "hit"
    def hit(list, list1):
        card_range = len(cards) - 1
        position = random.randrange(card_range)
        list.append(cards[position])
        list1.append(cards[position])
        del cards[position]
        return list

    #Assigns a value to face cards while keeping them face cards to the player
    def value_assignment(list):
        for position in range(len(list)):
            if list[position] == "K":
                list[position] = 10
            if list[position] == "Q":
                list[position] = 10
            if list[position] == "J":
                list[position] = 10
            if list[position] == "A" and list != dealer_value:
                n = str(input("1 or 11 for Ace?"))
                if n == "1":
                    list[position] = 1
                if n == "11":
                    list[position] = 11
            if list[position] == "A" and list == dealer_value:
                list[position] = 11
        return list

    #gets the total of each deck to track if decks go over 21
    def total(list):
        total = 0
        for position in range(len(list)):
            total = total + int(list[position])
        return total

    #creates the list for players
    players_cards = deal_intitial_player()
    dealers_cards = deal_intitial_dealer()

    running = True

    #intial print of the two deks
    print("Dealer: " + str(dealers_cards[0]) + ", hidden")
    print("Your hand:")
    print(players_cards)

    #Gets the value of the player deck
    player_value = []
    for x in range(len(players_cards)):
        player_value.append(players_cards[x])

    #gets the value of the dealer deck
    dealer_value = []
    for x in range(len(dealers_cards)):
        dealer_value.append(dealers_cards[x])

    #Assigns numerical values to face cards
    play_values = value_assignment(player_value)
    deal_values = value_assignment(dealer_value)

    while running:
        a = str(input("Hit or stand?"))
        checker = 0
        condition = True
        player_total = total(play_values)

        if a == "h":
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

        if a == "s" or condition == False:
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
                winnings = 0
                print("YOU LOSE")
            if dealer_total <= player_total and player_total <= 21:
                winnings = (1.5 * bet) + bet
                print("YOU WIN")
            if dealer_total == player_total and player_total <= 21:
                winnings = (1.5 * bet) + bet
                print("YOU WIN")
            if dealer_total > 21 and player_total <= 21:
                winnings = (1.5 * bet) + bet
                print("YOU WIN")
            if dealer_total > 21 and player_total > 21:
                winnings = 0
                print("YOU LOSE")
            if condition == False:
                winnings = 0
                print("YOU LOSE")

            balance = balance + winnings
            with open('balance.txt', 'w') as fp:
                fp.write(str(balance))
            print("Balance: " + str(balance))
            running = False

again = True

#While loop used to track if player wants to keep playing
while again:
    l = input("Play a game? (y/n)")
    if l == "y":
        main()
    if l == "n":
        again = False