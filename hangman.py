import random

words = ["python", "program", "computer", "internet", "keyboard"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== HANGMAN GAME =====")
print("The word has", len(word), "letters. Start guessing!\n")

while wrong_guesses < max_wrong:
    # Display the word (guessed letters are shown)
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display)
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Guessed letters:", guessed_letters)

    # Check for win
    if "_" not in display:
        print("\nCongratulations! You won! 🎉")
        print("The word was:", word)
        break

    guess = input("\nGuess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You have already guessed this letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess! ✅\n")
    else:
        wrong_guesses += 1
        print("Wrong guess! ❌\n")

else:
    print("\nGame Over! You lost.")
    print("The correct word was:", word)
