"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
Beau Beattie
"""

import random

#Variables

lowest_number = 1
highest_number = 20
highscore = 0

def welcome_message():
    print("""
---------------------
NUMBERS GUESSING GAME
--------------------- 
Welcome to the numbers guessing game.
This game will store a random number between {} and {} for you to guess. 
The game will help you by telling you if your guess was too high or too low.
You can then continue to guess.
Whoever guesses correctly in the fewest attempts will hold the highscore!
    """.format(lowest_number, highest_number))
    

def start_game(highscore):
    
    answer = random.randint(lowest_number, highest_number)
    
    if highscore > 0:
        print("""
New game! the current highscore is {} - can you beat it?
Choose a number between {} and {}!
        """.format(highscore, lowest_number, highest_number))
    
    guess_count = 1
    
    while True:
        guess = input("What is your answer?   ")

        try:
            guess = int(guess)
            if guess < lowest_number or guess > highest_number:
                raise ValueError("That number is outside of the range")
        except ValueError as err:
            print("Thats not a valid! {}! Try again!".format(err))
        else:
            if guess == answer:
                if highscore == 0 or guess_count < highscore:
                    highscore = guess_count
                    print("NEW HIGHSCORE!! You got it correct - it took you {} attempts!!".format(guess_count))
                elif guess_count == highscore:
                    print("You got it correct! and matched the existing highscore - it took you {} attempts!!".format(guess_count))
                else:    
                    print("You got it correct - it took you {} attempts!!".format(guess_count))
                    print("The highscore is {}!".format(highscore))
                break
            elif guess < answer:
                print("You were too low!")
                guess_count += 1
                continue
            else:
                print("You were too high!")
                guess_count +=1
                continue
    
    play_again = input("Would you like to play again? Y/N   ")
    if play_again.lower() == "y":
        start_game(highscore)
    else:
        print("Ok. Thanks for playing!!")
             
            
#main
if __name__ == '__main__':
    
    welcome_message()
    start_game(0)
