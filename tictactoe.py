#Implementation of Two Player tic-tac-toe game in python.

'''We will make the board using dictionary
    in which keys will be the location(i.e : top left,mid- right, etc)
    and initialliy it's value will be empty space and then after every move
    we will change the value according to player's choice of move.'''

theBoard = {'7': ' ', '8': '', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

'''We will have to print the updated board after evert move in the game and thus we will make a function in which we'll define the printBoard function. '''
def printBoard(board):
    print(board['7'] + '|' + ['8'] + '|' + ['9'])
    print('-+-+-')
    print(board['4'] + '|' + ['5'] + '|' + ['6'])
    print('-+-+-')  
    print(board['1'] + '|' + ['2'] + '|' + ['3'])

    # now We'Ll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Its your turn," + turn + "Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1

        else:
            print("That place is already filled.\n Move to which place?")
            continue

        # Now we will check if player X or 0 has won for every move after 5 moves

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':# across the top

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':# across the middle

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':# across the bottom

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break
            elif theBoard['1'] == theBoard['7'] == theBoard['4'] != ' ':# down the left side

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':# down the middle

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break
            elif theBoard['3'] == theBoard['9'] == theBoard['6'] != ' ':# down the right side

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':# diagonal

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':# diagonal

                printBoard(theBoard)
                print('\nGame Over.\n')

                print("****" + turn + "won. ****")
                break

            # if neither X or 0 wins and the board is full, we'll declare the result as 'tie'.

            if count == 9:
                print("\nGame Over.\n")

                print("Its a tie!!")

                # Now we have to change the player after every move.
                if turn == "X":
                    turn = '0'
                else:
                    turn = 'X'


                #Now we will ask if player wants to restart the game or not

                    restart = input("Do want to play Again?(y/n)")
                    if restart == "y" or restart == "Y":  
                        for key in board_keys:
                            theBoard[key] = " "

                        game()

if __name__ == "__main__":
    game()