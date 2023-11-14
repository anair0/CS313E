#  File: WordSearch.py

#  Description: Given a n by n grid of letters and words this program finds the row and column location of the words

#  Student Name: Arjun Nair 

#  Student UT EID: asn922

#  Partner Name: Nanxiang Zhao

#  Partner UT EID: nz3332

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 1/25/2022

#  Date Last Modified: 1/27/2022

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
    #Find the number of lines in the grid
    num_lines = sys.stdin.readline()
    num_lines = num_lines.strip()
    num_lines = int(num_lines)
    blank_line = sys.stdin.readline()
    grid_letters = []
    word_list = []

    #Transfer grid to 2-D list
    while(num_lines > 0):
        add_line = sys.stdin.readline()
        add_line = add_line.strip()
        grid_letters.append(add_line)
        num_lines -= 1
    blank_line = sys.stdin.readline()
    #Find number of words
    num_lines = sys.stdin.readline()
    num_lines = num_lines.strip()
    num_lines = int(num_lines)
    #Put words in a list
    while(num_lines > 0):
        add_line = sys.stdin.readline()
        add_line = add_line.strip()
        word_list.append(add_line)
        num_lines -= 1

    #Take out the spaces in the rows of the grid
    for i in range(len(grid_letters)):
        grid_letters[i] = grid_letters[i].replace(' ', '')

    return grid_letters, word_list
    
        
    

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word(grid, word):
    ##Create row and column iterators to keep track of the location in the grid
    row_it = -1
    col_it = -1
    for line in grid:
        row_it += 1
        for letter in line:
            col_it += 1
            #resets col iterator when it gets to the end of a line
            if(col_it == len(line)):
                col_it = 0
            if letter == word[0]:
                #Save the original row/col for output
                row = row_it
                col = col_it
                #Have secondary row/col to manipulate for finding words
                row2 = row_it
                col2 = col_it
                if (word[0] == word and len(word) == 1):
                    location = (row + 1, col + 1)
                    return location
                #Saves how far in the word we are when searching the word search
                leng_word = 1
                #Saves the number of directions around the letter we have searched
                dir_num = 0
                #Check in the 8 directions around the letter to see if the second letter is there
                while dir_num != 9:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if((row2 + i) == -1 or (row2 + i) == len(grid) or (row2 + i) == len(grid) + 1):
                                dir_num += 1
                                continue
                            if((col2 + j) == -1 or (col2 + j) == len(line) or (col2 + j) == len(line) + 1):
                                dir_num += 1
                                continue
                            if(i == 0 and j == 0):
                                dir_num += 1
                                continue
                            if(grid[row2 + i][col2 + j] == word[leng_word]):
                                if (word[leng_word] == word[1] and len(word) == 2):
                                    location = (row + 1, col + 1)
                                    return location
                                row2 = row2 + i
                                col2 = col2 + j
                                leng_word += 1
                                #Once second letter is found go in that direction until word is found or
                                #there is a letter that doesn't match up
                                for k in range(len(word) - 2):
                                    #Make sure the row and col we are searching does not exceed the scope of the grid
                                    if ((row2 + i) == -1 or (row2 + i) == len(grid) or (row2 + i) == len(grid) + 1):
                                        leng_word = 1
                                        break
                                    if ((col2 + j) == -1 or (col2 + j) == len(line) or (col2 + j) == len(line) + 1):
                                        leng_word = 1
                                        break
                                    if(grid[row2 + i][col2 + j] == word[leng_word]):
                                        if (word[leng_word] == word[2] and len(word) == 3):
                                            location = (row + 1, col + 1)
                                            return location
                                        leng_word += 1
                                        row2 = row2 + i
                                        col2 = col2 + j
                                        if ((row2 + i) == -1 or (row2 + i) == len(grid) or (row2 + i) == len(grid) + 1):
                                            leng_word = 1
                                            break
                                        if ((col2 + j) == -1 or (col2 + j) == len(line) or (col2 + j) == len(line) + 1):
                                            leng_word = 1
                                            break
                                        if (grid[row2 + i][col2 + j] == word[len(word) - 1] and len(word) - 1 == leng_word):
                                            location = (row + 1, col + 1)
                                            return location
                                    else:
                                        leng_word = 1
                                        break
                                row2 = row_it
                                col2 = col_it
                            dir_num += 1

    location =(0,0)
    return location

def main():
  # read the input file from stdin
  word_grid, word_list = read_input()


  # find each word and print its location
  for word in word_list:
    location = find_word(word_grid, word)
    print (word + ": " + str(location))

if __name__ == "__main__":
  main()
