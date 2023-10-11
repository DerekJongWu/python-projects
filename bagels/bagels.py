# Think about adding customization later
import random

def start():
    """
    This method gives the instructions to the player.
    
    """
    print("""Welcome to the Bagels Game 
          I am thinking of a 3-digit number. Try to guess what it is
          Here are some clues: 
          When I say:   That means:
          Pico          One digit is correct but in the wrong position.
          Fermi         One digit is correct and in the right position.
          Bagels        No digit is correct.
          
          I have thought up a number.
          You have 10 guesses to get it.
          """
          )

def init_truth_value() -> str: 
    """ 
    Generate a random 3 digit number for the players to guess
    """
    n = 3
    num = random.randrange(1, 10**3)
    # using format
    num_with_zeros = '{:03}'.format(num)
    #using string's zfill
    num_with_zeros = str(num).zfill(3)
    return num_with_zeros

def validate_guess(truth_digits, guess_digits):
    """
    Take a guess from the user and compare it to the truth value. Print out the clues. 

    Args: 
        truth_digits (List[str]): A list of all the digits of the truth value in string form
        guess_digits (List[str]): A list of all the digits of the player's guess in string form 
    """
    count = 0
    for i,digit in enumerate(guess_digits):
        if truth_digits[i] == digit: 
            print("Fermi")
            count +=1 
            continue
        elif digit in truth_digits: 
            print('Pico') 
            count +=1 
            continue
    if count == 0: 
        print("Bagels")

def gameplay(truth): 
    """" 
    Run through the actual gameplay of Bagels. Gives the player 10 tries to guess the truth value 

    Args: 
        truth(int) : the truth value the player is trying to guess
    """
    num_tries = 1
    truth_digits = [*truth]
    while num_tries < 11:
        guess = input(f"Guess #{num_tries}: ") 
        guess_digits = [*guess]
        if len(guess) != 3: 
            print("Please input a three digit number!")
            continue
        if guess_digits == truth_digits: 
            print("You Got It!")
            return
        else: 
            validate_guess(truth_digits, guess_digits)
        num_tries += 1 
    print(f"Better luck next time! The number was {truth}")
    return

def game(): 
    """
    Run through all of the steps of the game from the initial prompt to the actual gameplay
    """
    start()
    truth = init_truth_value() 
    gameplay(truth)
    replay()

def replay(): 
    """ 
    Ask the user if they would like to replay the game, if yes then start the game over again, 
    if no then exit. 
    """
    cont = input("Do you want to play again? (yes or no): ")
    if cont == "yes":
        game()
    if cont == "no":
        return

if __name__ == '__main__':
    game()

