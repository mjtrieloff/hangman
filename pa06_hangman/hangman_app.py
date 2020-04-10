"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random

filename = "eecumings.txt"
file = open(filename,'r')
text = file.read()
paragraph = text.split("\n\n")
words = text.split()

def generate(list_of_words):
    word = list_of_words[random.randrange(0, len(list_of_words))]
    return word

def print_word( word , guessed_letter ) :
    global guessed_letters
    #guessed_letters.append(guessed_letter)
    #progress = []
    word = list(word)
    for letter in word:
        if letter not in guessed_letters:
            print('-')
        elif letter in guessed_letters:
            print(letter)


def play_hangman():
   want_to_play = True
   while (want_to_play):
        guessed_letters = []
        def print_word( word , guessed_letter ) :
            word = list(word)
            for letter in word:
                if letter not in guessed_letters:
                    print('-')
                elif letter in guessed_letters:
                    print(letter)

        guesses_left = 6
        word = generate(words)
        print("Your word is", len(word), "letters long")
        letter = input("What letter would you like to guess? ")
        done = False

        while not done:

            if letter in guessed_letters:
                guesses_left += -1
                print("You already guessed that one, idiot")
            elif letter not in word:
                guessed_letters.append(letter)
                guesses_left += -1
                print("That one isn't in the word")
            else:
                guessed_letters.append(letter)
                print("That one is in the word!")

            testlist = []
            for letter in list(word):
                if letter in guessed_letters:
                    testlist.append(letter)

            if len(testlist) == len(word):
                print("You did it!")
                print_word(word,'!')
                done = True
            elif guesses_left == 0:
                print("A man is dead due to your failings")
                done = True
            else:
                print_word(word, letter)
                letter = input("what letter would you like to guess? ")
            testlist = []
        want_to_play = input("Would you like to play again? y/n")
        if want_to_play == 'y':
            want_to_play = True
        else:
            want_to_play = False

if __name__ == '__main__':
    play_hangman()
