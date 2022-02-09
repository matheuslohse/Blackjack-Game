############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
import random
from art import logo
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game_starter():
  game_score = {
    "player" : [],
    "computer": []
  }
  game_score["player"].append(random.choice(cards))
  game_score["player"].append(random.choice(cards))
  game_score["computer"].append(random.choice(cards))
  game_score["computer"].append(random.choice(cards))
  return game_score

def is_it_over(game_score):
  can_continue = True
  status = ""
  if sum(scores["player"]) == sum(scores["computer"]):
    can_continue = False
    status = "tie"
  elif sum(scores["player"]) > 21:
    can_continue = False
    status = "lose"
  elif sum(scores["computer"]) > 21:
    can_continue = False
    status = "win"
  return can_continue, status


def print_results(game_score):
  print(f"Your cards are {scores['player']}, current score: {sum(scores['player'])}\nComputer's first card: {scores['computer'][0]}")
  game_on, status = is_it_over(game_score)
  return game_on

wanna_play = input("Do you wanna play Blackjack? y or n: ")
if wanna_play == "n":
  print("Ok then, bye bye")
else:
  clearConsole()
  print(logo)
  game_on = True
  scores = game_starter()

  while game_on:
    game_on = print_results(scores)
    another_card = input("Type 'y' to get another card and 'n' to pass. ")
    if another_card == 'n':
      game_on = False
    else:
      print("")
      scores["player"].append(random.choice(cards))
    if 11 in scores["player"] and sum(scores["player"]) > 21:
        scores["player"][scores["player"].index(11)] = 1
  continuar = True

  can_continue, status = is_it_over(scores)
  if status == "lose":
    print("Your score is greater then 21 so YOU LOSE")

  while continuar:
    if sum(scores["computer"]) < 21 and sum(scores["computer"]) < sum(scores["player"]):
      scores["computer"].append(random.choice(cards))
      if 11 in scores["computer"] and sum(scores["computer"]) > 21:
        scores["computer"][scores["computer"].index(11)] = 1
    else:
      continuar = False

  print(f"\n\nThis are the final results:\n   Your final hand: {scores['player']}, final score: {sum(scores['player'])} \n   Computer's final hand: {scores['computer']}, final score: {sum(scores['computer'])}")
  
  can_continue, status = is_it_over(scores)
  if status == "tie":
    print("Both have the same score, so it is a TIE")
  elif status == "lose":
    print("Computer score is closer to  and smaller then 21 so YOU LOSE")
  else:
    print("Your score is closer to  and smaller then 21, so YOU WON")