import random
import pygame
import tkinter
import sys
import pandas as pd

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255, 255, 0)
gray = (128, 128, 128)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# defining a font
smallfont = pygame.font.SysFont('Corbel', 30)

# rendering a text written in
# this font
quit_text = smallfont.render('Quit', True, color)
again_text = smallfont.render(' Play Again', True, color)

card_font = pygame.font.Font('CARDC___.TTF', 42)
huge_font = pygame.font.Font('Crimson-Roman.ttf', 36)
instruct_font = pygame.font.Font('Crimson-Roman.ttf', 24)
title_font = pygame.font.Font('freesansbold.ttf', 56)

board = [" ", " ", " "]

#Window set up
root = tkinter.Tk()
root.withdraw()
WIDTH = root.winfo_screenwidth()/1.1
HEIGHT = root.winfo_screenheight()/1.1
screen = pygame.display.set_mode((WIDTH, HEIGHT),
                                     pygame.RESIZABLE)
pygame.display.set_caption('Blackjack')
fps = 60
timer = pygame.time.Clock()



global players_cards
global dealers_cards
global values

balance = 0

players_cards = [" ", " ", " ", " "," ", " ", " ", " "]
dealers_cards = [" ", " ", " "]

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


# deals the intital two cards for the dealer
# follows Vegas rules with only one card showing
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


# deals the players initial deck
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


# Function used to "hit"
def hit(list, list1):
    card_range = len(cards) - 1
    position = random.randrange(card_range)
    list.append(cards[position])
    list1.append(cards[position])
    del cards[position]
    return list


# Assigns a value to face cards while keeping them face cards to the player
def value_assignment(list):
    for position in range(len(list)):
        if list[position] == "K":
            list[position] = 10
        if list[position] == "Q":
            list[position] = 10
        if list[position] == "J":
            list[position] = 10
        if list[position] == "A" and list != dealer_value:
            n = "11"
            if n == "1":
                list[position] = 1
            if n == "11":
                list[position] = 11
        if list[position] == "A" and list == dealer_value:
            list[position] = 11
    return list


# gets the total of each deck to track if decks go over 21
def total(list):
    total = 0
    for position in range(len(list)):
        total = total + int(list[position])
    return total

again = True

def draw_board():
    global dealers_cards
    global players_cards
    for col in range(0, 3):
        pygame.draw.rect(screen, white, [col * 300 + 375, 100 + 12, 250, 350], 3, 5)
        piece_text = huge_font.render(dealers_cards[col], True, gray)
        screen.blit(piece_text, (col * 200 + 30, 100 + 25))
    for c in range(0, 5):
        pygame.draw.rect(screen, white, [c * 300 + 95, 500 + 75, 250, 350], 3, 5)
        piece_text = huge_font.render(players_cards[c], True, gray)
        screen.blit(piece_text, (c * 200 + 30, 100 + 25))

# #While loop used to track if player wants to keep playing
# while again:
#     l = input("Play a game? (y/n)")
#     if l == "y":
#         main()
#     if l == "n":
#         again = False

running = True
while running:
    timer.tick(fps)
    screen.fill(gray)

    draw_board()

    players_cards = deal_intitial_player()
    dealers_cards = deal_intitial_dealer()

    player_value = []
    for x in range(len(players_cards)):
        player_value.append(players_cards[x])

    # gets the value of the dealer deck
    dealer_value = []
    for x in range(len(dealers_cards)):
        dealer_value.append(dealers_cards[x])

    play_values = value_assignment(player_value)
    deal_values = value_assignment(dealer_value)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        # Quit button
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH / 2 <= mouse[0] <= WIDTH / 2 + 140 and HEIGHT - 75 <= mouse[1] <= HEIGHT - 35:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        if WIDTH / 2 <= mouse[0] <= WIDTH / 2 + 140 and HEIGHT - 75 <= mouse[1] <= HEIGHT - 35:
            pygame.draw.rect(screen, color_light, [WIDTH / 2, HEIGHT - 75, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [WIDTH / 2, HEIGHT - 75, 140, 40])
        screen.blit(quit_text, (WIDTH / 2 + 40, HEIGHT - 70))

        # Play again button
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH / 2 - 200 <= mouse[0] <= WIDTH / 2 -60 and HEIGHT - 75 <= mouse[1] <= HEIGHT - 35:
                deal_intitial_dealer() #CHANGE TO PLAY AGAIN
        mouse = pygame.mouse.get_pos()
        if WIDTH / 2 - 200 <= mouse[0] <= WIDTH / 2 -60 and HEIGHT - 75 <= mouse[1] <= HEIGHT - 35:
            pygame.draw.rect(screen, color_light, [WIDTH / 2 - 200, HEIGHT - 75, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [WIDTH / 2 - 200, HEIGHT - 75, 140, 40])
        screen.blit(again_text, (WIDTH / 2 - 200, HEIGHT - 70))

        checker = 0
        condition = True
        player_total = total(play_values)

        if ev.type == pygame.K_h:
            players_cards = hit(players_cards, player_value)
            play_values = value_assignment(player_value)
            player_total = total(play_values)
            checker = player_total
            if checker > 21:
                condition = False
        if ev.type == pygame.K_s or condition == False:
            player_total = total(play_values)
            dealer_total = total(deal_values)
            if dealer_total < 17:
                dealers_cards = hit(dealers_cards, dealer_value)
                deal_values = value_assignment(dealer_value)
                dealer_total = total(deal_values)
            if dealer_total >= 17:
                print("W")
            if dealer_total > player_total and dealer_total <= 21:
                winnings = 0
                print("YOU LOSE")
            if dealer_total <= player_total and player_total <= 21:
                print("YOU WIN")
            if dealer_total == player_total and player_total <= 21:
                print("YOU WIN")
            if dealer_total > 21 and player_total <= 21:
                print("YOU WIN")
            if dealer_total > 21 and player_total > 21:
                winnings = 0
                print("YOU LOSE")
            if condition == False:
                winnings = 0
                print("YOU LOSE")

        pygame.display.update()
