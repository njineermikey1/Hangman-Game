#Step 1 

word_list = ["aardvark", "baboon", "camel", "pistachio","mountain","radio","tumble","forgiveness","newspaper","concede","packet","lothario","tree","signing","copier"]
#word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
#random.seed(1234)
#TODO-1
continue_game = "y"
chosen_word = random.choice(word_list)
chsen_word = chosen_word.lower()
print(chosen_word)
underscore_char = "_"
underscore_word = underscore_char * len(chosen_word)
print(chosen_word)
print(underscore_word)
#TODO-2
while continue_game == "y":
  guess = input("Guess a letter: ")
  guess = guess.lower()
  print(guess)
  word_length = len(chosen_word)
  print(word_length)
  #break
  
  #my_string = "Hello World"
  #index_to_replace = 4 = x
  #new_char = "a" = underscore_char
  #new_string = my_string[:index_to_replace] + new_char + my_string[index_to_replace+1:] - underscor_word = underscore_word[x] + guess + underscore_word[x+1]
  #print(new_string)

  y = 0
  missing = 0
  for x in chosen_word:
    if x == guess:
      print("Match " + guess + " = " + x)
      underscore_word = underscore_word[:y] + guess + underscore_word[y+1:]
      print(underscore_word)
      y += 1
      string1 = underscore_word
      string2 = chosen_word
    else:
      print("No Match " + guess + " != " + x)
      y += 1
      missing += 1
      
        
  for letter in chosen_word:
      if letter == guess:
          print("Right")
      else:
          print("Wrong")
  if len(string1) != len(string2):
        print("The strings do not have the same length.")
  else:
    for i in range(len(string1)):
      if string1[i] != string2[i]:
        print("The strings do not match.")
        break
      else:
        print("The strings match.")
          #break
continue_game = input("Continue?")



#if len(string1) != len(string2):
    #print("The strings do not have the same length.")
#else:
    #for i in range(len(string1)):
        #if string1[i] != string2[i]:
            #print("The strings do not match.")
            #break
    #else:
        #print("The strings match.")
