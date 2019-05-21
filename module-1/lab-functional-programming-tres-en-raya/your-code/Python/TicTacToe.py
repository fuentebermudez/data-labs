#Select a game mode
def selectGameMode():
    
    gameMode = ""
    gameModeOptions = ["human", "h", "computer", "c"]
    
    while gameMode == "":
        gameMode = input("\nWill you play vs a [h]uman or vs the [c]omputer? ").lower()
        if gameMode not in gameModeOptions:
            print("Please, check your input!")
            gameMode = ""

    if gameMode == "human" or gameMode == "h": #Human vs human
        print("You will play 2-player mode.")
        return("vsHuman")
       
    elif gameMode == "computer" or gameMode == "c": #Human vs computer
        print("You will play 1-player mode.")
        return("vsComputer")

    
#Enter a name for each human player
def enterPlayerNames(gameMode):
    
    player1 = ""
    player2 = ""
    
    while player1 == "": #Always ask for a name for player 1      
        player1 = input("\nEnter name for player 1: ").capitalize()
        if player1 == "":
            print("A name can't be empty!")
    
    if gameMode == "vsHuman": #If the game mode is 1 vs 1, ask also the name for player 2
        while player2 == "":   
            player2 = input("Enter name for player 2: ").capitalize()
            if player2 == "":
                print("A name can't be empty!")
            elif player2 == player1:
                print("You can't choose the same name than player 1!")
                player2 = ""

    return(player1, player2)
    

#Choose how many rounds will be played
def enterMaxRounds():
    
    try:      
        maxRounds = int(input("\nHow many rounds do you want to play? "))       
    except: #Prevent a non-number input
        print("Come on, try with a number at least...")
        enterMaxRounds()
        
    print("These are the numbers for each cell:")
    drawBoard()
    return(maxRounds)


#Randomly select the players order
def randomizePlayersOrder (player1, player2):
    
    from random import randint
    randomValue = randint(0, 1)
    
    if randomValue == 0:
        return(player1, player2)
    else:
        return(player2, player1)


#Draw a 3x3 board from a list of the type [[a,b,c],[d,e,f],[g,h,i]]. Print a demo if there are not arguments.
def drawBoard(board = [["1","2","3"], ["4","5","6"], ["7","8","9"]]):
    
    print("") #Print an empty line before board for clarity
    for vector in board:
        row = ""
        for value in vector:
            row = row + " | " + value + " |"
        print(row)
        

#Game Core
def ticTacToeCore(player1, player2, maxRounds):
    
    import copy
    
    emptyBoard = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
    currentRound = 1
    
    player1Turn = True
    player2Turn = False
    
    player1Victories = 0
    player2Victories = 0
    
    while currentRound <= maxRounds:
        
        board = copy.deepcopy(emptyBoard)
        
        while checkForRows(board) == False:
    
            if player1Turn:
                board = askForMove(player1, board, "X")
                
            elif player2Turn:
                board = askForMove(player2, board, "O")
            
            player1Turn = not(player1Turn)
            player2Turn = not(player2Turn)
        
        if player1Turn == True:
            drawBoard(board)
            player1Victories += 1  
            print(("\n" + player1), "won this round!", player1, player1Victories, "-", player2Victories, player2)
            
        elif player2Turn == True:
            drawBoard(board)
            player2Victories += 1
            print(("\n" + player2), "won this round!", player1, player1Victories, "-", player2Victories, player2)
            
        currentRound += 1
    
    return(player1Victories, player2Victories)
        
        
#Check to see if any of the players have won
def checkForRows(board):
    
    #Check rows
    if board[0][0] == board[0][1] == board[0][2] != "-":
        return(True)
    elif board[1][0] == board[1][1] == board[1][2] != "-":
        return(True)     
    elif board[2][0] == board[2][1] == board[2][2] != "-":
        return(True)
   
    #Check columns
    elif board[0][0] == board[1][0] == board[2][0] != "-":
        return(True)
    elif board[0][1] == board[1][1] == board[2][1] != "-":
        return(True)             
    elif board[0][2] == board[1][2] == board[2][2] != "-":
        return(True)

    #Check diagonals
    elif board[0][0] == board[1][1] == board[2][2] != "-":
        return(True)  
    elif board[2][1] == board[1][1] == board[0][2] != "-":
        return(True)
    
    #0 matches
    else:
        return(False)
        
        
#Computer chooses its move
def computerMoves(board, shape):
    pass


#Insert a valid move in board
def moveToBoard(move, board, shape):
    
    if move == 1:
        board[0][0] = shape    
    elif move == 2:
        board[0][1] = shape    
    elif move == 3:        
        board[0][2] = shape        
    elif move == 4:        
        board[1][0] = shape       
    elif move == 5:
        board[1][1] = shape       
    elif move == 6:        
        board[1][2] = shape  
    elif move == 7:        
        board[2][0] = shape       
    elif move == 8:        
        board[2][1] = shape       
    elif move == 9:        
        board[2][2] = shape         
            
    return(board)
    

#Ask and make a valid move
def askForMove(player, board, shape):
    
    availableMoves = []
    cellNumber = 0
    move = ""
    
    for vector in board:
        for value in vector:
            cellNumber += 1
            if value == "-":
                availableMoves.append(cellNumber)
        
    if player == None:
        move = computerMoves(board, shape)
        
    else:
        drawBoard(board)
        print("\nTurn for", player, "playing with", shape+'!')
             
        while move not in availableMoves:
            move = input("Make your move: ")   
            
            try:
                move = int(move)
                if move in availableMoves:
                    availableMoves.remove(move)
                    board = moveToBoard(move, board, shape)
                    break
                else:
                    print("\nTry again! Choose an empty cell from:", availableMoves) 
            except:
                print("\nYour input must be an integer.") 
                move = ""
        
        return(board)
    
    
#Print final score
def finalScore(player1, player2, player1Victories, player2Victories, maxRounds):
    
    print("End of the game! Played rounds:", maxRounds)
    print(player1, player1Victories, "-", player2Victories, player2)
    
    if player1Victories > player2Victories:
        print(player1, "wins!")
    elif player2Victories > player1Victories:
        print(player2, "wins!")
    else:
        print("It's a tie!")

#Start Tic-Tac-Toe - The game
def ticTacToe():
    
    print("Welcome to Tic-Tac-Toe!")
    
    #Set game configuration
    gameMode = selectGameMode()
    player1, player2 = enterPlayerNames(gameMode)
    maxRounds = enterMaxRounds()
    player1, player2 = randomizePlayersOrder(player1, player2)
    
    #Play
    player1Victories, player2Victories = ticTacToeCore(player1, player2, maxRounds)
    
    #Return results
    finalScore(player1, player2, player1Victories, player2Victories, maxRounds)
    
#Test
ticTacToe()

