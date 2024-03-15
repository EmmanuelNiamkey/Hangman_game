from time import sleep
import random
import hangman_art

print(hangman_art.logo)
sleep(2)

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = int(len(chosen_word))
lives = 6

# testing code
# print(f"Pssst, the solution is {chosen_word}.")

# Creating an empty list and for each element of the chosen word,
# have the same number of "_" in the list
display = []

# for i in range(length_guess):
#    display.append("_")
# print(display)

for _ in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # loop through each element of the chosen_word;
    # if the letter at that position matches 'guess' then
    # reveal that letter in the position it should be.
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    print(lives)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose, the word was {chosen_word}.")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])