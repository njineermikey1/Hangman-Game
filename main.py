#Step 1 

word_list = ["aardvark", "baboon", "camel", "pistachio","mountain","radio","tumble","forgiveness","newspaper","concede","packet"]
#word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
#random.seed(1234)
#TODO-1
chosen_word = random.choice(word_list)
chsen_word = chosen_word.lower()
print(chosen_word)

#TODO-2
guess = input("Guess a letter: ")
guess = guess.lower()
print(guess)
word_length = len(chosen_word)
print(word_length)
#underscore_word = "_".join(str(e)for e in chosen_word
#print(underscore_word)
y = 0
for x in chosen_word:
  if x == guess:
    print("Match " + guess + " = " + x)
    #y += 1
  else:
    print("No Match " + guess + " != " + x)
    #y += 1
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")