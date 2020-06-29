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
    # FILL IN YOUR CODE HERE...
    L = []
    for letter in secretWord:
        for element in lettersGuessed:
            if(letter == element):
                L.append(letter)
                break;
    SW = ''.join(L)
    #print(SW)
    if(secretWord == SW):
        return True
    return False

def isLetterGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    L = []
    Found = False
    for letter in secretWord:
        for element in lettersGuessed:
            if(letter == element):
                L.append(letter)
                Found = True
                break;
    #SW = ''.join(L)
    #print(SW)
    if(Found == True):
        return True
    return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    L = []
    for letter in secretWord:
        Found = False
        for element in lettersGuessed:
            if(letter == element):
                L.append(letter)
                Found = True
                break;
        if(Found == False):
            L.append('_')
            #print(L)
    SW = ''.join(L)
    return(SW)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    List_Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letters in lettersGuessed:
        List_Alphabets.remove(letters)
    SW = ''.join(List_Alphabets)
    #print(SW)
    return SW

def getAvailableLetters_Updated(lettersGuessed,Avialable_Letters):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    #List_Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #for letters in Avialable_Letters:
    Avialable_Letters = Avialable_Letters.replace(lettersGuessed,'')
    SW = ''.join(Avialable_Letters)
    #print(SW)
    return SW


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
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) +  " letters long.")
    print("-----------")
    #print(secretWord)
    Guess_Count = 8
    Updated_List = []
    FinalList = []
    for i in range(len(secretWord)):
        FinalList.append('_')
    Avialable_Letters = getAvailableLetters([])
    LetterIndex = 0
    while(Guess_Count != 0 ):
        print("You have " + str(Guess_Count) +  " guesses left.")
        print("\n")
        count = 0
        print("Available letters:" + Avialable_Letters)
        print("\n")
        Guessed_Letter = (input("Please guess a letter: "))
        print("\n")
        Guessed_Letter = Guessed_Letter.strip()

        if(Guessed_Letter not in Avialable_Letters):
            print ("Oops! You've already guessed that letter:" + ''.join(FinalList))
        elif(isLetterGuessed(secretWord, Guessed_Letter) == True):
            UpdatedList = getGuessedWord(secretWord, Guessed_Letter)
            #print(len(UpdatedList))
            for LetterIndex in range(0,len(UpdatedList)):
                print(LetterIndex)
                if(UpdatedList[LetterIndex] != '_'):
                    FinalList[LetterIndex] = UpdatedList[LetterIndex]

            if(isWordGuessed(secretWord,FinalList) == True):
                print("Good Guess " +  ''.join((FinalList)))
                print("Congratulations, you won!")
                break;
            
            print("Good Guess " +  ' '.join((FinalList)))
            print("----------------")
            
        
        else:
            print("Oops! That letter is not in my word:" + ' '.join((FinalList)))
            Guess_Count = Guess_Count - 1
        
        Avialable_Letters = getAvailableLetters_Updated(Guessed_Letter,Avialable_Letters)
        
            
        if(Guess_Count == 0):
            #print("-----------")
            print("Sorry, you ran out of guesses. The word was " + secretWord)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
