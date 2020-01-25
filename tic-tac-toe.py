import random
initial_board=["","1","2","3","4","5","6","7","8","9"]
playing_board=["","1","2","3","4","5","6","7","8","9"]
player1=""
player2=""
turn=""
counter1 = 0
counter2 = 0
check =0

def display_board(board):
    print()
    print(board[7], '|', board[8], '|', board[9])
    print(board[4], '|', board[5], '|', board[6])
    print(board[1], '|', board[2], '|', board[3])


def player_choice(choice=""):
    global player1, player2
    while choice!="X" and choice!="O":
        print()
        choice=input("Player 1, Do you want to play as X or O ?").upper()
    if choice=="X":
        player1="X"
        player2="O"
    else:
        player1="O"
        player2="X"
    print()
    print()
    print("Player 1 play as",player1)
    print()
    print(f"Player 2 play as {player2}")
    print()
    print()
    display_board(playing_board)

def player_turn():
    flip=random.randint(0,1)
    if flip==0:
        return "Player1"
    else:
        return "Player2"

def player_input():
    global turn
    input_list=[]
    turn= player_turn()
    print()
    print(f"{turn} goes first.")
    if player1=="X":
        while len(input_list) != 9:
            if turn == "Player1":
                print()
                print("It's", turn, "turn")
                input_choice = int(input("Please enter a number to place your X: "))
                if input_choice not in input_list:
                    playing_board[input_choice] = "X"
                    input_list.append(input_choice)
                    turn = "Player2"
                else:
                    print("Please input available number")
                    turn = "Player1"
                display_board(playing_board)
            elif turn == "Player2":
                print()
                print("It's", turn, "turn")
                input_choice = int(input("Please enter a number to place your O: "))
                if input_choice not in input_list:
                    playing_board[input_choice] = "O"
                    input_list.append(input_choice)
                    turn = "Player1"
                else:
                    print("Please input available number")
                    turn = "Player2"
                display_board(playing_board)
            stop=winning_condition()
            if stop=="stop":
                break
    elif player2=="X":
        while len(input_list)!=9:
            if turn=="Player2":
                print()
                print("It's", turn, "turn")
                input_choice = int(input("Please enter a number to place your X: "))
                if input_choice not in input_list:
                    playing_board[input_choice] = "X"
                    input_list.append(input_choice)
                    turn="Player1"
                else:
                    print("Please input available number")
                    turn="Player2"
                display_board(playing_board)
            elif turn=="Player1":
                print()
                print("It's", turn, "turn")
                input_choice=int(input("Please enter a number to place your O: "))
                if input_choice not in input_list:
                    playing_board[input_choice] = "O"
                    input_list.append(input_choice)
                    turn="Player2"
                else:
                    print()
                    print("Please input available number")
                    print()
                    turn="Player1"
                display_board(playing_board)
            stop = winning_condition()
            if stop == "stop":
                break
    return playing_board


def winning_condition1(result_board):
    global counter1, check
    winning_board=["","X","X","X","X","X","X","X","X","X"]
    winning_list= [ [winning_board[1],winning_board[2],winning_board[3]],
                    [winning_board[4],winning_board[5],winning_board[6]],
                    [winning_board[7],winning_board[8],winning_board[9]],
                    [winning_board[1],winning_board[5],winning_board[9]],
                    [winning_board[7],winning_board[5],winning_board[3]],
                    [winning_board[3],winning_board[6],winning_board[9]],
                    [winning_board[1],winning_board[4],winning_board[7]],
                    [winning_board[2],winning_board[5],winning_board[8]]
                    ]
    result_list=  [ [result_board[1],result_board[2],result_board[3]],
                    [result_board[4],result_board[5],result_board[6]],
                    [result_board[7],result_board[8],result_board[9]],
                    [result_board[1],result_board[5],result_board[9]],
                    [result_board[7],result_board[5],result_board[3]],
                    [result_board[3],result_board[6],result_board[9]],
                    [result_board[1],result_board[4],result_board[7]],
                    [result_board[2],result_board[5],result_board[8]]]
    for num_check in range(len(result_list)):
        if result_list[num_check]==winning_list[num_check]:
            counter1 += 1
            break
        check=num_check
    return counter1, check

def winning_condition2(result_board):
    global counter2, check
    winning_board=["","O","O","O","O","O","O","O","O","O"]
    winning_list= [ [winning_board[1],winning_board[2],winning_board[3]],
                    [winning_board[4],winning_board[5],winning_board[6]],
                    [winning_board[7],winning_board[8],winning_board[9]],
                    [winning_board[1],winning_board[5],winning_board[9]],
                    [winning_board[7],winning_board[5],winning_board[3]],
                    [winning_board[3],winning_board[6],winning_board[9]],
                    [winning_board[1],winning_board[4],winning_board[7]],
                    [winning_board[2],winning_board[5],winning_board[8]]
                    ]
    result_list=  [ [result_board[1],result_board[2],result_board[3]],
                    [result_board[4],result_board[5],result_board[6]],
                    [result_board[7],result_board[8],result_board[9]],
                    [result_board[1],result_board[5],result_board[9]],
                    [result_board[7],result_board[5],result_board[3]],
                    [result_board[3],result_board[6],result_board[9]],
                    [result_board[1],result_board[4],result_board[7]],
                    [result_board[2],result_board[5],result_board[8]]]
    for num_check in range(len(result_list)):
        if result_list[num_check]==winning_list[num_check]:
            counter2 += 1
            break
        check=num_check
    return counter2, check

def winning_condition():
    winning_condition1(playing_board)
    winning_condition2(playing_board)
    if counter1==1 and counter2==0:
        print("Congratulations! X won the game")
        print()
        return "stop"
    elif counter1==0 and counter2==1:
        print("Congratulations! O won the game")
        print()
        return "stop"
    elif check==8:
        print("It's a draw!")
        print()


def playing():
    global counter1,counter2,check, playing_board
    ans="Y"
    while ans.upper()=="Y":
        counter1=0
        counter2=0
        check=0
        playing_board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print()
        print("Welcome to tic-tac-toe game !")
        display_board(initial_board)
        player_choice()
        player_input()


        ans=input("Do you want to play again? (Y/N)")

playing()
