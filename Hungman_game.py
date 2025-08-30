import random

def hangman():
    # Step 1: Predefined word list
    words = ["python", "java", "kotlin", "hangman", "programming"]
    word = random.choice(words)  # Randomly select a word

    guessed_letters = []  # Correct guesses
    wrong_guesses = []    # Incorrect guesses
    attempts_left = 6     # Limit of incorrect attempts

    print("Welcome to Hangman!")
    print("_ " * len(word))  # Show blanks

    # Step 2: Game loop
    while attempts_left > 0:
        guess = input("\nGuess a letter: ").lower()

        # Step 3: Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Step 4: Check if letter is already guessed
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter.")
            continue

        # Step 5: Correct guess
        if guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            wrong_guesses.append(guess)
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        # Step 6: Display progress
        progress = ""
        for letter in word:
            if letter in guessed_letters:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress.strip())

        # Step 7: Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()