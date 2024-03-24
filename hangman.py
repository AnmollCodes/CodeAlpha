import random

def choose_word():
    words = ['hangman', 'python', 'programming', 'computer', 'game', 'code', 'challenge']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word. You can make up to", max_incorrect_guesses, "incorrect guesses.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the correct word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Guess another!!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print("Incorrect guesses left:", max_incorrect_guesses - incorrect_guesses)
            if incorrect_guesses == max_incorrect_guesses:
                print("Sorry! No guesses left. The word was:", word)
                break
        else:
            print("Good guess!")

hangman()

