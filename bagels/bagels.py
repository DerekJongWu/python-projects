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

def gameplay(): 
    n = 3
    value = random(3)


if __name__ == '__main__':
    start()