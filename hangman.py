import random
import time

def main():
    
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['~', '~', '~']]

    snowmanDict = {
        1 : [2, 1, "O"],
        2 : [1, 1, "O"],
        3 : [1, 0, "/"],
        4 : [1, 2, "\\"],
        5 : [0, 1, "O"]}
    
    allWords = readFile()
    allWordsLen = len(allWords)
    choice = random.randint(0, allWordsLen)
    word = allWords[choice]
    
    wordLen = len(word)
    blanks = []
    
    for letter in word:
        blanks.append("#")

    rightGuessList = []
    wrongGuessCount = 0
    wrongGuessList = []
    win = False
    lose = False

    playerOne = input("what is your name, player one? ")
    time.sleep(0.5)
    playerTwo = input("gotcha. and what is your name, player two? ")

    playerOneTurn = True
    playerTwoTurn = False

    instructions()

    getGuess(board, snowmanDict, word, wordLen, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)
    
def instructions():

    time.sleep(0.5)
    print("thank you both! this is hangman, but instead of hanging a man, you're building a snowman! the theme is mythical creatures. have fun!")
    
def getGuess(board, snowmanDict, word, wordLen, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn):

    while win == False and lose == False:

        time.sleep(1)
        print(blanks)
        time.sleep(1)
        grid(board)
        time.sleep(1)

        if playerOneTurn == True:
            print("okay " + playerOne + ", it's your turn.")
            time.sleep(1)
        elif playerTwoTurn == True:
            print("okay " + playerTwo + ", it's your turn.")
            time.sleep(1)
            
        guess = str(input("what is your guess? "))
        guess = guess.lower()

        if guess == word:
            time.sleep(1)
            print("wow, you figured out the word early! good job!")
            print("the word was " + str(word) + ".")
            time.sleep(1)
            print("here is the final board:")
            time.sleep(1)
            grid(board)
            time.sleep(10)
            
        elif guess in rightGuessList:
            time.sleep(1)
            print("that was already guessed, and it was right. try again.")

            (win, lose) = statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)
            
        elif guess in word:
            time.sleep(1)
            print("yep!")

            for position in range(0, len(word)):
                if word[position] == guess:
                        blanks[position] = guess
                       
            rightGuessList.append(guess)

            (win, lose) = statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)

        elif guess in wrongGuessList:
            time.sleep(1)
            print("that was already guessed, and it was wrong. try again.")
            
            (win, lose) = statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)

        elif guess.isalpha() == False:
            time.sleep(1)
            print("please enter a valid letter. try again.")

            (win, lose) = statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)

        elif len(guess) != 1:
            time.sleep(1)
            print("please only enter one letter. try again.")

            (win, lose) = statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)

        elif guess == "\n":
            time.sleep(1)
            print("did you just hit enter? put in a letter.")

            (win, lose) = statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)
            
        else:
            time.sleep(1)
            print("nope!")
            wrongGuessList.append(guess)
            wrongGuessCount = wrongGuessCount + 1

            if wrongGuessCount == 1:
                row = snowmanDict[1][0]
                col = snowmanDict[1][1] 
                snowmanPiece = snowmanDict[1][2]
                board[row][col] = snowmanPiece
            elif wrongGuessCount == 2:
                row = snowmanDict[2][0]
                col = snowmanDict[2][1] 
                snowmanPiece = snowmanDict[2][2]
                board[row][col] = snowmanPiece
            elif wrongGuessCount == 3:
                row = snowmanDict[3][0]
                col = snowmanDict[3][1] 
                snowmanPiece = snowmanDict[3][2]
                board[row][col] = snowmanPiece
            elif wrongGuessCount == 4:
                row = snowmanDict[4][0]
                col = snowmanDict[4][1] 
                snowmanPiece = snowmanDict[4][2]
                board[row][col] = snowmanPiece
            elif wrongGuessCount == 5:
                row = snowmanDict[5][0]
                col = snowmanDict[5][1] 
                snowmanPiece = snowmanDict[5][2]
                board[row][col] = snowmanPiece

            if playerOneTurn == True:
                playerOneTurn = False
                playerTwoTurn = True
                
            elif playerTwoTurn == True:
                playerTwoTurn = False
                playerOneTurn = True
                    
            (win, lose) = statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn)           

def grid(g):
    for row in g:
        for col in row:
            print(col, end = ' ')
        print()

def readFile():
    f = open("allWords.txt")
    lines = f.readlines()

    fixedLines = []
    for line in lines:
        fixedLine = line.strip()
        fixedLines.append(fixedLine)

    allWords = fixedLines

    return(allWords)
            
def statusReport(board, word, blanks, rightGuessList, wrongGuessCount, wrongGuessList, win, lose, playerOne, playerTwo, playerOneTurn, playerTwoTurn):
    
    if "#" in blanks:
        win = False
        
    else:
        win = True
        
        if playerOneTurn == True:
            time.sleep(1)
            print("you did it, " + playerOne + ", you win!")
        elif playerTwoTurn == True:
            time.sleep(1)
            print("you did it, " + playerTwo + ", you win!")
            
        time.sleep(1)
        print(blanks)
        time.sleep(1)
        print("the word was " + str(word) + ".")
        time.sleep(1)
        print("here is the final board:")
        time.sleep(1)
        grid(board)
        time.sleep(10)

    if wrongGuessCount == 5:
        lose = True
        time.sleep(1)
        print("game over. you've both made too many wrong guesses, and the snowman is complete!")
        time.sleep(1)
        print(blanks)
        time.sleep(1)
        print("the word was " + str(word) + ".")
        time.sleep(1)
        print("here is the final board:")
        time.sleep(1)
        grid(board)
        time.sleep(10)
        
    if win == False and lose == False:
        time.sleep(1)
        grid(board)
        time.sleep(1)
        print("you have made " + str(wrongGuessCount) + " wrong guesses.")
        time.sleep(1)
        print("here is the list of your wrong guesses: " + str(wrongGuessList))
        time.sleep(1)
        print("here is the list of your right guesses: " + str(rightGuessList))
        time.sleep(1)

    return(win, lose)

main()
