import random


def play_game():

    print("================================")
    print("        HANGMAN GAME")
    print("================================")

    words = ["python", "computer", "science", "coding", "program"]

    word = random.choice(words)

    display_word = ["_"] * len(word)

    attempts = 6
    guessed_letters = []

    while attempts > 0 and "_" in display_word:

        print("\nWord:", " ".join(display_word))
        print("Remaining attempts:", attempts)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")

            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess

        else:
            print("Wrong guess!")
            attempts -= 1

    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
    else:
        print("\n❌ Game Over!")
        print("The correct word was:", word)


while True:

    play_game()

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for playing!")
        print("Goodbye! 👋")
        break
