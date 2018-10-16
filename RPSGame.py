#import the random package so that we can generate random numbers
from random import randint
choices = ["Rock","Paper","Scissors"]
computer_choice = choices[randint(0,2)]
print ("Computer chooses: ", computer_choice)
