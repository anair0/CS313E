#  File: EscapeTheMaze.py

#  Description: Determine if you are able to escape the maze unscathed.

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

import sys
from typing import List

def print_grid(grid: List[List[str]]) -> None:
    """ Prints grid left aligned, for your debugging.
    Args:
        grid (List[List[str]]): Grid to print.
    """
    for row in grid:
        # Change '7' to any int to adjust the width of the column.
        print(''.join([ '{:<7}'.format(c) for c in row ]))

def escape_the_maze(
        grid: List[List[str]],
        strength: int, 
        potion_strength: int, 
        potions: int
    ) -> int:
    """ Returns the minimum number of potions needed to escape the maze. -1 if unable to.
    Args:
        grid (List[List[str]]): Grid to traverse (elements are either an integer or 'X').
        strength (int): Your base strength.
        potion_strength (int): Strength increase from a single potion.
        potions (int): Number of potions you have.
    Returns:
        int: Returns the minimum number of potions needed to escape the maze. -1 if unable to
        escape the maze.
    """
    location = [0][0]
    while ()
    pass


# DO NOT CHANGE ANYTHING BELOW THIS LINE.

def main():
    """ Main harness for reading in input from STDIN. """
    
    # ------ INPUT UTILITIES ------

    # Fast input.
    LINES = sys.stdin.read().splitlines()[::-1]
    def input(): return LINES.pop()

    # Multiple integers, mapped.
    mul = lambda: map(int, input().strip().split())

    # String input.
    strng = lambda: input().strip()

    # Words split on white space.
    strwords = lambda: strng().split()
    
    # Read in a grid based on the number rows.
    read_grid = lambda rows: [strwords() for _ in range(rows)]
    
    
    # ------ READ IN INPUT ------

    rows, cols = mul()
    base, potion_strength, potions = mul()
    grid = read_grid(rows)
    
    # ------ EVALUATION ------
    print(escape_the_maze(grid, base, potion_strength, potions))

if __name__ == "__main__":
    main()
