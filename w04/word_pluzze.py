def generate_hint(secret_word, guess):
    hint = ""
    for i in range(len(secret_word)):
        if i < len(guess):
            if guess[i].lower() == secret_word[i].lower():
                hint += secret_word[i]  
            elif guess[i].lower() in secret_word.lower():
                hint += guess[i].lower()
            else:
                hint += "_"
        else:
            hint += "_"
    return hint

def play_game():
    secret_word = "byupathway"
    guess_count = 0
    
    print("Welcome to the word guessing game made for Jairo Castro!")
    print("Your hint is:", " ".join(["_"] * len(secret_word)))
    
    while True:
        guess = input("What is your guess? ")
        guess_count += 1
        
        if len(guess) != len(secret_word):
            print(f"Sorry, the guess must have {len(secret_word)} letters.")
            continue
        
        # chech if the hint is correct
        if guess.lower() == secret_word.lower():
            print(f"\nCongratulations! You guessed it!")
            print(f"It took you {guess_count} guesses.")
            break
        
        
        hint = generate_hint(secret_word, guess)
        print("Your hint is:", " ".join(hint))

def main():
    while True:
        play_game()
        
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

# Restar the program
if __name__ == "__main__":
    main()