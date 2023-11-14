#  File: Bomberman.py

#  Description: Determines the state of the board after the bombs detonate

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120


# Prints the board. Useful for debugging. DO NOT MODIFY THIS METHOD
def print_board(temp):
    for row in temp:
        print(" ".join(row))


# Input: k is an int specifying how strong the bombs are. The bomb's blast
#        should extend a maximum of k blocks in each cardinal direction.
#        board is an N by M matrix that contains the following characters:
#           'E' to denote an empty space
#           'B' to denote a bomb
#           'H' to denote a hard wall that cannot be destroyed
#           'S' to denote a soft wall that can be destroyed
# Output: The updated grid. Any spaces with a bomb or soft walls that were
#         destroyed should now have an 'E'.
def update_board(k, board):
    # YOUR CODE HERE
    pass


# DO NOT MODIFY THIS METHOD
def main():
    # read number of rows of board
    n = int(input())
    # read the explosiveness of the bombs
    k = int(input())

    board = []
    # read data from standard input
    for _ in range(n):
        board.append(list(map(str, input().split())))

    # get the new board state
    result = update_board(k, board)

    # print the result to standard output
    print_board(result)


if __name__ == "__main__":
    main()
