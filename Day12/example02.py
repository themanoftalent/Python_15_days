# AUthor : Mehmet Akif Cifci

# This is iteration 1 of the project "Guess the number" game. The game is
# played between two players. The first player thinks of a number between 1
# and 100 and the second player tries to guess it. The first player tells
# the second player whether the guess is too high or too low. The second
# player keeps guessing until he/she gets the number right. The second
# player wins the game if he/she guesses the number in 10 tries or less.

def main():
    # This is the main function of the program.
    # It is the entry point of the program.
    # It calls the other functions to play the game.

    # Display the welcome message.
    display_welcome_message()

    # Get the number to be guessed.
    number = get_number()

    # Get the player's guess.
    guess = get_guess()

    # Check the guess.
    check_guess(number, guess)


def display_welcome_message():
    # Display the welcome message.
    print('Welcome to the "Guess the Number" game!')
    print('I am thinking of a number between 1 and 100.')
    print('Try to guess it in 10 tries or less.')
    print()


def get_number():
    # Get the number to be guessed.
    number = int(input('Enter the number: '))
    return number


def get_guess():
    # Get the player's guess.
    guess = int(input('Enter your guess: '))
    return guess


def check_guess(number, guess):
    # Check the guess.
    if guess == number:
        print('Congratulations! You guessed it!')
    else:
        print('Sorry, that is not correct.')
        print('The correct answer is', number)


# Call the main function to start the program.
main()
