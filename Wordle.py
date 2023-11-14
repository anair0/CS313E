#  File: Wordle.py

#  Description: Given a dictionary and previous guesses, filter out the possible words.

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

import sys
from typing import List, Tuple

'''
Example:
guesses = 
[
    [
        ('A', 'B'),
        ('D', 'Y'),
        ('O', 'Y'),
        ('P', 'Y'),
        ('T', 'B')
    ],
    [
        ('D', 'G'),
        ('O', 'G'),
        ('C', 'B'),
        ('K', 'B'),
        ('S', 'B')
    ]
]

dictionary = 
[
	'ADOPT',
	'DOING',
	'DOPEY',
	'PODGY'
]

wordle(guesses, dictionary) → ['DOPEY']

'''

# Input:
# `guesses` are the previous guesses. They are organized as a list
# list of 2 element tuples. The first element in the tuple is the
# guessed character at that position. The second element is the color 
# ('G’, ‘Y’, ‘B’). 'G' = green, 'Y' = yellow, 'B' = black.
# 
# `dictionary` is the list of all of possible words to narrow down.
# 
# Output:
# The subset of words in `dictionary` that can be the answer
# based on previous guesses. Return an empty list if no words in the
# dictionary are possible.
def wordle(guesses: List[List[Tuple[str, str]]], dictionary: List[str]) -> List[str]:
    wrong = []
    correct = []
    init = []
    words = []
    for i in guesses:
        for j in range(len(i)):
            if(i[j][1] == 'G'):
                correct.append([j, i[j][0]])
                continue
            elif (i[j][1] == 'Y'):
                init.append([j, i[j][0]])
                continue
            elif (i[j][1] == 'B'):
                wrong.append([j, i[j][0]])
                continue
    for i in dictionary:
        trueword = True
        for j in range(len(wrong)):
            if(wrong[j][1] in i):
                trueword = False
                break
        for j in range(len(correct)):
            if(i[correct[j][0]] != correct[j][1]):
                trueword = False
                break
        for j in range(len(init)):
            if(init[j][1] not in i):
                trueword = False
                break
            if(i[init[j][0]] == init[j][1]):
                trueword = False
                break
        if(trueword):
            words.append(i)

    if(len(words) == 0):
        return []

    return words

# BELOW THIS LINE, MODIFY AT YOUR OWN RISK.
def main():
    
    # Helper functions for reading in input.
    LINES = sys.stdin.read().splitlines()[::-1]
    def input(): return LINES.pop()
    
    mul = lambda: map(int,input().strip().split())
    strng = lambda: input().strip()
    
    # First two numbers correspond to the number of words in the dictionary
    # and the number of guesses respectively.
    num_dictionary, num_guesses = mul()
    
    dictionary = [strng().upper() for _ in range(num_dictionary)]
    guesses = []
    
    # Following lines contain the word guessed and the colors.
    for _ in range(num_guesses):
        # Advance reader (skip blank line).
        input()
        guess = strng()
        colors = strng()
        
        assert len(guess) == len(colors)
        guesses.append([(letter.upper(), color) for letter, color in zip(list(guess), list(colors))])
    
    # Call `wordle` function.
    filtered = wordle(guesses, dictionary)
    
    if len(filtered) == 0:
        print('No matches.')
    else:
        print(' '.join(filtered))

if __name__ == "__main__":
    main()
