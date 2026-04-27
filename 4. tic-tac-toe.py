'''
-update of Final version
-started on Sep 19, 2025: finished Oct 21, 2025
-updated on April 2026: added Exceptions, skipped lines, terminated program after failed trys

Winning Combinations:
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], 
[2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
'''


EMPTY = " "
board = []
moves = [5]
moves_by_human = []
moves_by_computer = [5]
X = 'X'
O = 'O'  

print('\n')
def display_board(board):
    print('Board: ', board)

for i in range(3):
    row = [EMPTY for i in range(3)]
    board.append(row)
display_board(board)

print('\n')
print("Computer's first move is: 5")
board[1][1] = X
display_board(board)
print('\n')


# To determine the winner
import sys 
def victory_for(board, sign):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], 
        [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]
        ]
    
    for i in winning_combinations:
        common_elements = list(set(board).intersection(set(i)))
        if i == sorted(common_elements):
            print('\n')
            print(sign, 'WINS!!!',i)
            print('\n')
            sys.exit(0)
            #quit()
    else:
        print('No win.')
        print('\n')


# Moves by human
def enter_move(board):
    try:
        m = int(input("Human's turn... "))
        if m < 1 or m > 9:
            print("You lose a turn. Please enter an integer between 1 to 9 only. ")
            print('\n')
            # enter_move(board)
            return
    except ValueError:
        print("Last try...Please enter an integer between 1 to 9 only. ")
        print('\n')
        try:
            m = int(input("Human's turn... "))
            print("Human's move is: ", m)
        except ValueError:
            print('\n')
            print("Please add more coins...")
            print('\n')
            quit()        

    if m not in moves:
        moves.append(m)
        moves_by_human.append(m)
        print(' - Move(s) by human: ',moves_by_human )
        print(' - Moves by human and computer: ', moves)
    else:
        print('Already taken, try again...')      
        enter_move(board)
        return
        
    if m == 1:
        board[0][0] = O     
    if m == 2:
        board[0][1] = O    
    if m == 3:
        board[0][2] = O
    if m == 4:
        board[1][0] = O
    if m == 5:  
        board[1][1]
    if m == 6:
        board[1][2] = O
    if m == 7:
        board[2][0] = O
    if m == 8:
        board[2][1] = O   
    if m == 9:
        board[2][2] = O
    print('Board update: ',board)
    victory_for(moves_by_human, 'HUMAN')        


enter_move(board)


# Moves by computer 
from random import randrange
for i in range(10):
    num = randrange(1, 9)
    print("Computer's move is: ",num)

    if num not in moves:
        moves.append(num)
        moves_by_computer.append(num)
        print(' - Moves by computer: ', moves_by_computer)
        print(' - Moves by human and computer: ', moves)
    else:
        print('Already taken...')       
        continue
    
    if num == 1:
        board[0][0] = X     
    if num == 2:
        board[0][1] = X    
    if num == 3:
        board[0][2] = X
    if num == 4:
        board[1][0] = X
    if num == 5:  
        board[1][1]
    if num == 6:
        board[1][2] = X
    if num == 7:
        board[2][0] = X
    if num == 8:
        board[2][1] = X   
    if num == 9:
        board[2][2] = X

    print('Board update: ',board)
    victory_for(moves_by_computer, 'COMPUTER')
    enter_move(board)

else:
    print('\n')
    print('Game Over. No winner.')
    print('\n')




