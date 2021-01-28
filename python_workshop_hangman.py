    #for this we will need to download the package "RandomWords"
    #so pip install RandomWords
    #after we can load everything in:
def main():
    #importing necessary packages
    import random as random
    #importing package to select random words
    from random_words import RandomWords
    rw = RandomWords()
    #importing package for time
    import time as time

    #starting program now
    name = input("What is your name? ")
    time.sleep(1)
    print("Good Luck,", name,"!")
    time.sleep(1)
    print("\n")
    print("Now, let's play hangman!:D")
    print("Instructions: Please guess the characters in the word one at a time.")

    #defining the function for the game
    def hangman_game():

        print("Finding a word...")
        word = rw.random_word()
        time.sleep(1)
        print("Okay, ready.")
        print("\n")
        #telling the number of characters
        a = len(word)
        print("The word has", a, "characters.")
        #print(word)

        for char in word:
            print("_ ", end="")

        turns = 6
        guesses = []
        print("\n")
        print("You will have 6 turns.")
        print("Guess the characters:")

        while turns > 0:
            # counts the number of times a user fails
            failed = 0

            # all characters from the input
            # word taking one at a time.
            for char in word:
                # comparing that character with
                # the character in guesses
                if char in guesses:
                    print(char, end="")
                else:
                    print("_ ", end="")

                    # for every failure 1 will be
                    # incremented in failure
                    failed += 1

            if failed == 0:
                # user will win the game if failure is 0
                # and 'You Win' will be given as output
                print("Congratulations, you win :D")

                # this print the correct word
                print("The word was: ", word)
                break

            # if user has input the wrong letter then
            # it will ask user to enter another letter
            print("\n")
            guess = input("Guess a letter:")

            # every input character will be stored in guesses
            guesses += guess

            # check input with the character in word
            if guess not in word:

                turns -= 1

                # if the character doesn’t match the word
                # then “Wrong” will be given as output
                print("\n")
                print("Incorrect.")

                # this will print the number of
                # turns left for the user
                print("You have", + turns, 'more guesses.')

                if turns == 0:
                    print("\n")
                    print("I'm sorry, you lose.")
                    print("The word was", word)

    #setting a trigger to play the game
    playGame = "Y"
    ready = input("Would you like to play? Press Y to play or any other letter to end. :) ")
    if ready != "Y":
        print("Thanks for playing!")

    while ready == playGame:
        hangman_game()
        ready = input("Would you like to play again? Press Y to play or any other letter to end. ")
        if ready != "Y":
            print("\n")
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
