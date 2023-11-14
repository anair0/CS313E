#  File: WordSearch.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E 

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    # Find the number of lines in the grid
    num_lines = sys.stdin.readline()
    num_lines = num_lines.strip()
    num_lines = int(num_lines)
    blank_line = sys.stdin.readline()
    grid_letters = []
    word_list = []

    # Transfer grid to 2-D list
    while (num_lines > 0):
        add_line = sys.stdin.readline()
        add_line = add_line.strip()
        grid_letters.append(add_line)
        num_lines -= 1
    blank_line = sys.stdin.readline()
    # Find number of words
    num_lines = sys.stdin.readline()
    num_lines = num_lines.strip()
    num_lines = int(num_lines)
    # Put words in a list
    while (num_lines > 0):
        add_line = sys.stdin.readline()
        add_line = add_line.strip()
        word_list.append(add_line)
        num_lines -= 1

    # Take out the spaces in the rows of the grid
    for i in range(len(grid_letters)):
        grid_letters[i] = grid_letters[i].replace(' ', '')

    return grid_letters, word_list

    
# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
                                        
                                        
                        
                    

            








    
def main():
  # read the input file from stdin
  word_grid, word_list = read_input()
  for line in word_grid:
      print(line)
      for letter in line:
          print(letter)
  # find each word and print its location

if __name__ == "__main__":
  main()
