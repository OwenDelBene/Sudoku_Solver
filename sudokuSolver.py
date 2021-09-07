board = [ 
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]



def solve(b):
    #look for an empty square
    find = findempty(b)
    if not find:
        return True
    else:
        row, col = find
    #iterate through possible values
    for i in range(1,10):
    #Check if they follow the rules of sudoku
        if valid(b, i, (row,col)):
            b[row][col] = i

            if solve(b):
                return True
            b[row][col]=0
    return False


def valid(b, num, pos):
    Checking if the proposed value from Solve will follow the rules of sudoku
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False
        Creating the Sudoku Boxes
    box_x= pos[1] // 3
    box_y= pos[0] // 3
    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3 ):
            if b[i][j] == num and (i,j) != pos:
                return False
    return True

    

def print_board(b):
    #Printing the borders for the Sudoku Boxes
    for i in range(len(b)):
        if i%3 == 0 and i!=0:
            print('------------------')
        for j in range(len(b[0])):
            if j%3 ==0 and j!= 0:
                print(" | ", end="")
            if j==8:
                print(str(b[i][j]) + " ", end="")


def findempty(b):
    #iterating through the board and looking for an empty square
    # 0 means empty
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j)
    return None

print_board(board)
solve(board)
print('______________________________')
print_board(board)
