#  File: LargestCluster.py

#  Description: Determine the largest cluster found in each journey through space.

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

import sys

# Input: s is a string representing your journey through the galaxy
# Output: return an integer representing the largest cluster encountered
def largest_cluster(s):
    unique = []
    count = 0
    if(len(s) <= 0):
        return 0
    for i in range(len(s)):
        if(s[0] == s[i]):
            count += 1
    if(count == len(s)):
        unique.append([0, s[0]])
    for i in range(len(s)):
        if(i != 0 and i != len(s) - 1):
            if(s[i] != s[i + 1] or s[i] != s[i - 1]):
                if(len(unique) > 0):
                    if(s[i] != unique[len(unique) - 1][1]):
                        unique.append([i, s[i]])
                else:
                    unique.append([0, s[i]])
        if(i == 0):
            if(s[i] != s[i + 1]):
                unique.append([i, s[i]])
        if(i == len(s) - 1):
            if(s[i] != s[i - 1]):
                unique.append([i, s[i]])
    high = 0
    for i in unique:
        count = 0
        for j in range(i[0], len(s)):
            if(i[1] == s[j]):
                count += 1
            if(i[1] != s[j]):
                break
        if(count > high):
            high = count

    return high

# IMPORTANT: You should not have to modify anything below this line
def main():
    # read in the number of test cases
    test_cases = int(sys.stdin.readline().strip())

    for i in range(test_cases):
        test_case = sys.stdin.readline().strip()
        max_cluster = largest_cluster(test_case)
        print("The largest cluster of journey", i, "is", max_cluster)

if __name__ == "__main__":
    main()