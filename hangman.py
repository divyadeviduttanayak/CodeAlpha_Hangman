import random

# List of words to choose from
words = ["python", "programming", "artificial", "intelligence", "machine", "learning"]

# Number of allowed incorrect guesses
max_guesses = 4

def main():
  # Choose a random word
  word = random.choice(words).upper()
  # Create a list of underscores to hide the word
  hidden_word = ["_" for letter in word]
  # Track used letters
  used_letters = []
  # Track remaining guesses
  guesses_left = max_guesses

  while True:
    # Display current game state
    print("Word:", " ".join(hidden_word))
    print("Used letters:", ", ".join(used_letters))
    print("Guesses left:", guesses_left)

    # Prompt for guess
    guess = input("Guess a letter: ").upper()

    # Validate guess
    if len(guess) != 1 or not guess.isalpha() or guess in used_letters:
      print("Invalid guess. Please enter a single unused letter.")
      continue

    # Update used letters
    used_letters.append(guess)

    # Check if guess is correct
    if guess in word:
      # Update hidden word
      for i in range(len(word)):
        if word[i] == guess:
          hidden_word[i] = guess
    else:
      # Incorrect guess, decrement remaining guesses
      guesses_left -= 1

    # Check game over conditions
    if "_" not in hidden_word:
      print("Congratulations! You guessed the word:", word)
      break
    elif guesses_left == 0:
      print("You ran out of guesses! The word was:", word)
      break

if __name__ == "__main__":
  main()
