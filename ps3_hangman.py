# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    for x in secretWord:
        if x not in lettersGuessed:
            result += "_"
        else:
            result += x   
    return (result)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = string.ascii_lowercase
    result = ""
    for x in availableLetters:
        if x not in lettersGuessed:
            result += x
    return (result)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %s letters long." %(len(secretWord)))
    print("-----------")
    mistakesMade = 0
    lettersGuessed = []
    
    while mistakesMade < 8:
        
        print("You have %s guesses left." %(8 - mistakesMade))
        print("Available letters: %s" %(getAvailableLetters(lettersGuessed)))
        aGuess = input("Please guess a letter: ")
        aGuess = aGuess.lower()
        
        if aGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: %s" %(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed.append(aGuess)            
            
            if aGuess not in secretWord:
                print("Oops! That letter is not in my word: %s" %(getGuessedWord(secretWord, lettersGuessed)))
                mistakesMade += 1
            else:
                print("Good guess: %s" %(getGuessedWord(secretWord, lettersGuessed)))
                        
            if isWordGuessed(secretWord, lettersGuessed):
                print("-----------")                
                print("Congratulations, you won!")
                break
        
        print("------------")
        
        
         
    if mistakesMade >= 8:
        print("Sorry, you ran out of guesses. The word was %s." %(secretWord))
        

    



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# secretWord = "zzz"
hangman(secretWord)
