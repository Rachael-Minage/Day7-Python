from art import logo
from art import min
print(min)
print(logo)
from words import word_list
import random
chosen_word= random.choice(word_list)
print(chosen_word)
# lives= len(stages)-1
lives=6
display=[]
word_length = len(chosen_word)
for _ in range(word_length):
    display+="_"
    print(display)
end_of_game= False
from art import stages
while end_of_game==False:
    guess = input("Guess a letter\n").lower()
    if guess in display:
        print(f"You already guessed {guess}")
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]= letter
    print(display)
    if guess not in chosen_word:
        print(f"{guess} not in letter. You lose a life")
        lives-=1
        if lives ==0:
            end_of_game=True
            print("You lose")
    if "_" not in display:
        end_of_game =True
        print("You win")
    print(stages[lives])    


    



