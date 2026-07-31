import random

# List of words
words = ["python", "computer", "programming", "hangman", "developer"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0:
    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)
