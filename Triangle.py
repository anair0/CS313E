#  File: Triangle.py

#  Description: Finds greatest path sum down a triangle using 4 different styles

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/2/2022

#  Date Last Modified: 3/4/2022

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force(grid):
    sums = []
    rows = len(grid)
    sum = grid[0][0]
    brute_force_helper(grid, rows, 0, 0, sum, sums)
    #returns the greatest value out of all path sums
    return max(sums)

#finds every path sum and adds them all to a list
def brute_force_helper(grid, rows, row, col, sum, sums):
    if (row == rows - 1):
        sums.append(sum)
    else:
        brute_force_helper(grid, rows, row + 1, col, sum + grid[row + 1][col], sums)
        brute_force_helper(grid, rows, row + 1, col + 1, sum + grid[row + 1][col + 1], sums)

# returns the greatest path sum using greedy approach
def greedy(grid):
    sum = 0
    index = 0
    max = 0
    #Every row finds the greatest number adjacent to previous to get
    #'greatest' path sum with the greedy approach
    for i in range(len(grid)):
        if (i == 0):
            sum = grid[i][0]
            continue
        for j in range(len(grid[i])):
            if (j == index or j == index + 1):
                if (grid[i][j] > max):
                        max = grid[i][j]
                        temp = j
            if (j == len(grid[i]) - 1):
                sum = sum + max
                max = 0
                index = temp
    return sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    rows = len(grid)
    return divide_conquer_helper(grid, rows, 0, 0)

#Uses recursion to look at each path and take the one resulting in the bigger path sum
def divide_conquer_helper(grid, rows, row, col):
    if (row == rows):
        return 0
    else:
        return grid[row][col] + max(divide_conquer_helper(grid, rows, row + 1, col),
                                    divide_conquer_helper(grid, rows, row + 1, col + 1))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    triangle = grid[:]
    dynamic_prog_helper(triangle)
    return triangle[0][0]

#starts from bottom of triangle and as it goes to each row upwards it adds the greatest values from the previous row
#Therefore by the time it reaches the end it will have altered the grid and the top of the triangle will have the
#greatest value
def dynamic_prog_helper(grid):
    for j in range(len(grid) - 1, -1, -1):
        for i in range(len(grid[0]) - 1):
            if (grid[j][i + 1] == 0 and j == 1):
                return grid
            grid[j - 1][i] += max(grid[j][i], grid[j][i + 1])



# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    '''
    # check that the grid was read in properly
    print (grid)
    '''

    # output greatest path from exhaustive search
    print('The greatest path sum through exhaustive search is')
    print(str(brute_force(grid)))
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print('The time taken for exhaustive search in seconds is')
    print(str(times))

    # output greatest path from greedy approach
    print('The greatest path sum through greedy search is')
    print(str(greedy(grid)))
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    # print time taken using greedy approach
    print('The time taken for greedy approach in seconds is')
    print(str(times))

    # output greatest path from divide-and-conquer approach
    print('The greatest path sum through recursive search is')
    print(str(divide_conquer(grid)))
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print('The time taken for recursive search in seconds is')
    print(str(times))

    # output greatest path from dynamic programming
    print('The greatest path sum through dynamic programming is')
    print(str(dynamic_prog(grid)))
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming
    print('The time taken for dynamic programming in seconds is')
    print(str(times))


if __name__ == "__main__":
    main()