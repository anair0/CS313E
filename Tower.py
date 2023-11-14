#  File: Tower.py

#  Description: Computes number of movements needed to transfer disks from one peg to the final peg

#  Student's Name: Arjun Nair

#  Student's UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/6/2022

#  Date Last Modified: 3/6/2022

import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    #Memo
    moves_memo = {'total':0}

    if(n == 0):
        return 0

    towers_four(n, moves_memo)

    return moves_memo['total']

#Calculates the number of movements when only 3 pegs can be used
def towers_three(n, moves_memo):
    if (n == 1):
        moves_memo['total'] += 1
    else:
        towers_three(n - 1, moves_memo)
        towers_three(n - 1, moves_memo)
        moves_memo['total'] += 1

#Calculates the number of movements when only 4 pegs can be used
def towers_four(n, moves_memo):
    if (n == 1):
        moves_memo['total'] += 1
    elif (n == 2):
        moves_memo['total'] += 3
    elif (n == 3):
        moves_memo['total'] += 5
    else:
        # value of k that minimizes the number of movements
        k = round(n - math.sqrt(2 * n + 1) + 1)
        k = int(k)

        #Follows the algorithm for a 4 peg tower
        towers_four(k, moves_memo)
        towers_four(k, moves_memo)
        towers_three(n - k - 1, moves_memo)
        towers_three(n - k - 1, moves_memo)
        moves_memo['total'] += 1




def main():
    # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int (line)
        print (num_moves (num_disks))

if __name__ == "__main__":
    main()
