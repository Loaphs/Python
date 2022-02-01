import random


def start(number, tries):
    print('\nPick a number between 1 and 100\n')

    numGuess = input()

    try:
        numGuess = int(numGuess)
    except:
        print('\nINVALID INPUT\n')
        start(number, tries)
    else:
        if numGuess >= 1 and numGuess <= 100:
            if numGuess == number: 
                win(tries)
            elif numGuess < number:
                print('\nYour guess is lower\n')
                tries += 1
                start(number, tries)
            elif numGuess > number:
                print('\nYour guess is higher\n')
                tries += 1
                start(number, tries)
        else:
            print('\nVALUE IS OUTSIDE OF GUESSING RANGE\n')
            start(number, tries)

def win(tries):
    print("\nCongratulations, you won! Attempts: " + str(tries) + "\n\nTry Again?\nYes(y)\nNo(n)\n")
    again = input()

    if again == 'y':
        number = random.randrange(1,100)
        start(number, 0)
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
        start(number, 0)
    elif startDec == 'n':
        quit()
    else:
        print('\nINVALID INPUT\n')
        main()

main()