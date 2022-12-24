import random, words, ascii_art, os;

clear = lambda: os.system('cls')

#choose a random word from words file
word = random.choice(words.word_list)

display = []
for letter in word:
    display += "_"

letterFounded = 0
won = 0
lives = 6
stage = 0

print(ascii_art.logo)

while lives > 0:
    print(ascii_art.stages[stage])
    
    letterFounded = 0
    
    guess = input("Guess a letter: ").lower()
    
    while guess in display:
        print("You have already typed this letter! try another.")
        guess = input("Guess a letter: ").lower()
    
    for index in range(0, len(word)):
        if word[index] == guess:
            display[index] = word[index]
            letterFounded = 1
            won += 1
    
    if letterFounded:
        print("You have found a letter!")
        
        if won == len(word):
            print(display)
            print("You won!")
            break
    else:
        stage += 1
        lives -= 1
        
        print("Letter not founded!")
        print(f"Lives left: {lives}")
        
        if lives == 0:
            print(display)
            print("Game over!")
            print("The word was: ", word)
            break
        
    print(display)