"""This program simulates a double dice roll game, in which the player wins if the sum of the two rolls is guessed, otherwise, the computer wins! """

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("So, please take your guess:"))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximal value can be: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "The guess is invalid"
  else:
    print "Rolling..." 
    sleep(2)
    print "First roll: %d" % first_roll
    sleep(1)
    print "Second roll: %d" % second_roll
    total_roll = first_roll + second_roll
    print "Total roll: %d" % total_roll
    sleep(1)
    if guess == total_roll:
      print "You won! :)"
    else:
      print "You lose! :/"  

roll_dice(6)
