# Think about adding customization later
import random

def start():
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
    n = 3
    num = random.randrange(1, 10**3)
    # using format
    num_with_zeros = '{:03}'.format(num)
    #using string's zfill
    num_with_zeros = str(num).zfill(3)
    return num_with_zeros

def validate_guess(truth_digits, guess_digits):
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
    start()
    truth = init_truth_value() 
    gameplay(truth)
    replay()

def replay(): 
    cont = input("Do you want to play again? (yes or no): ")
    if cont == "yes":
        game()
    if cont == "no":
        return

if __name__ == '__main__':
    game()

