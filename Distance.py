# File: RiverFlow.py

# Description: Determine if a river can flow off the map given starting point.

# Student Name: Arjun Nair

# Student EID: asn922

# Course Name: CS 313E

# Unique Number: 51120

import sys


# Input: two strings:
# Output: the edit distance between the two input strings
def edit_distance(str1, str2):
    if (str1 == str2):
        return 0
    edits = 0
    if (len(str1) == len(str2)):
        for i in range(len(str1)):
            if (str1[i] != str2[i]):
                str2[i] = str1[i]
                edits += 1
    if (len(str1) < len(str2)):
        pass
    pass


# TAKE CAUTION TO EDIT BELOW
if __name__ == "__main__":
    str1 = sys.stdin.readline()[:-1]
    str2 = sys.stdin.readline()[:-1]
    print(edit_distance(str1, str2))
