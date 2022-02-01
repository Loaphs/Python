from email.errors import StartBoundaryNotFoundDefect
import random


number = None

def start():
    print('\nPick a number between 1 and 100\n')

    numGuess = input()

    try:
        int(numGuess)
        if numGuess >= 1 and numGuess <= 100:
            if numGuess == number: 
                win()
            elif numGuess < number:
                print('\nYour guess is lower\n')
                start()
            elif numGuess > number:
                print('\nYour guess is higher\n')
        else:
            print('\nVALUE IS OUTSIDE OF GUESSING RANGE\n')
            start()
    except:
        print('\nINVALID INPUT\n')
        start()

def win():
    print("\nCongratulations, you won! Try Again?\nYes(y)\nNo(n)\n")
    again = input()

    if again == 'y':
        number = random.randrange(1,100)
        start()
    elif again == 'n':
        quit()
    else:
        print('\nINVALID INPUT\n')
        win()

def main():
    print('\nWelcome to Guess That Number! Would you like to begin?\nYes(y)\nNo(n)\n')

    startDec = input()
    startDec.lower()

    if startDec == 'y':
        number = random.randrange(1,100)
        start()
    elif startDec == 'n':
        quit()
    else:
        print('\nINVALID INPUT\n')
        main()

main()