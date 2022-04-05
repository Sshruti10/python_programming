import random
import art
import hangman_words
life = 5

print(art.logo)

print("Choose a category:")
print('''1. Animals
2. Flowers
3. Fruits
4. Sports
5. Professions ''')

try:
    category = int(input("Enter your choice(1-5): "))
except:
     print("Wrong input. Try again.")
     quit()

if category not in range(1,6):
    print("Wrong input. Try again.")
    quit()

chosen_word = random.choice(hangman_words.word_list[category-1])
display = []
for letter in chosen_word:
    display.append("_")
print('Guess the word: ', display)
print("Total chances: " + art.lives[life])


while('_' in display and life>=0):
    guess = input("\nGuess the letter: ").lower()
    if len(guess)!=1 or (not guess.isalpha()):
        print("Wrong input. Please try again.")
        continue
    if guess not in hangman_words.alphabets:
        print("You have already guessed letter '" + guess + "'")
        continue


    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in display:
        if life-1>=0:
            print("Wrong guess! " + art.lives[life-1] + " chances remaining!")
        print(art.stages[life])
        life -= 1
    else:
        print(display)
    hangman_words.alphabets.remove(guess)

print("The word is '" + chosen_word + "'")   
if chosen_word == ''.join(display):
   print("Yay! You guessed it right")
else:
   print("You missed all the chances. Try again next time!")
