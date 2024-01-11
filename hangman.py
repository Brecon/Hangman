import random

def hangman():
    guesses = 0
    guessed = []
    print("Choose a word for the other player to guess?")
    secretWord = input()

    secretWordList = list(str(secretWord))
    invisibleWord = list(len(str(secretWord)) * "_")

    
    while guesses >= 0:
        print("This is guess number " + str(guesses + 1))
        print("The word you are trying to guess looks like this:")
        print(invisibleWord)
    ##    print(secretWordList)
        print("Guess a letter of the secret word.")
        guessedLetter = input()
        guesses += 1

        #Show the guessed letter and tell them how many guesses they have made
        #print("You have guessed " + guessedLetter)
        


        #Add the guessed letter to the list of letters guessed
        guessed.append(guessedLetter)


        
        #Check if the guessed letter is in the secret word
        if guessedLetter in secretWordList:
            tempNum = (secretWordList.index(guessedLetter))
            del invisibleWord[tempNum]
            invisibleWord.insert(tempNum,guessedLetter)
        else:
            print("That Letter is not in this word, please guess again!")


        print("")
        print("")
        print("")
        print("you have guessed the following letters:")
        print(guessed)

        
        if invisibleWord == list(secretWord):
            print("You Win!")
            break
        elif guesses == 11:
            print("You Lose!")
            break




hangman()
print("Would you like to play again?")
pAgain = input()
if pAgain == "yes":
    hangman()
else:
    exit()
