import pandas as pd
from matplotlib import pyplot as plt
import random

#Layout parameters of the graph
plt.rcParams["figure.figsize"] = [15, 7]
plt.rcParams["figure.autolayout"] = True

#Establishes the list for the data
data_list = []
#Retrieves the amount of times to run the simulation
trial = int(input("How many samples?"))

#Variables for the game() function
global players_cards
global dealers_cards
global values
global player_wins

#Function that runs the games
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

        if checker > 17 or condition == False:
            player_total = total(play_values)
            dealer_total = total(deal_values)
            if dealer_total < 17:
                dealers_cards = hit(dealers_cards, dealer_value)
                deal_values = value_assignment(dealer_value)
                dealer_total = total(deal_values)
            if dealer_total >= 17:
               print("")
            if dealer_total > player_total and dealer_total <= 21:
               # print("YOU LOSE")
                return 0
            if dealer_total <= player_total and player_total <= 21:
               # print("YOU WIN")
                return 1
            if dealer_total == player_total and player_total <= 21:
              #  print("YOU WIN")
                return 1
            if dealer_total > 21 and player_total <= 21:
              #  print("YOU WIN")
                return 1
            if player_total > 21:
               # print("YOU LOSE")
                return 0
            if condition == False:
               # print("YOU LOSE")
                return 0

            running = False

again = True

#Variable used to keep track of wins
player_wins = 0

#function that runs the game() function and returns if the player wins or not
def reloop(num):
    wins = 0
    for x in range(num):
        holder = int(game())
        wins = wins + holder
    return wins

#Runs the simulation for the set amount of time
for f in range(trial):
    y = 100
    player_wins = reloop(y)
    percent = (player_wins)/(y)
    data_list.append(round(float(percent), 3))

#Sorts the data
freq = sorted(data_list, key = float)
print(freq)
fig = plt.subplots()

df = pd.DataFrame({'numbers': freq}) #creates the data frame
print(str(df['numbers'].describe().loc[['min', '25%', '50%', '75%', 'max']])) #prints the five number summary
df['numbers'].value_counts()[df.numbers.unique()].plot(kind='bar', xlabel='numbers', ylabel='frequency') #creates the plot

plt.show() #shows the plot