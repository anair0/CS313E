#  File: Work.py

#  Description: Compares linear and binary search when looking for how many lines of code
#               Vyasa can write before drinking the first coffee

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/20/2022

#  Date Last Modified: 2/21/2022

import sys, time

#Input: int v, the number of lines of code that can be written before first cup of coffee
#       int k, the productivity factor
#Output: the total number of lines of code that can be written with coffee
def total_lines(v, k):
    exp = 1
    lines = 1
    while(lines != 0):
        lines = v // (k**exp)
        if(lines == 0):
            break
        exp += 1
    total = v
    for i in range(1, exp):
        total = total + (v // (k ** i))

    return total


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    # use linear search here
    v = n
    total = total_lines(v, k)
    while (total > n):
        total = total_lines(v, k)
        if(total < n):
            break
        v = v - 1
    #Adds one to values that come out to be less than the min number of lines
    #of code to be written (n)
    total = total_lines(v, k)
    if (total < n):
        v = v + 1
    return v

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    # use binary search here
    hi = n
    lo = 0
    while(lo <= hi):
        mid = (lo + hi) // 2
        total = total_lines(mid, k)
        #Whenever the binary search doesn't get to an exact value that equals n
        #this checks the mid at the end when low and high and mid are all the same
        #to see if the value above mid or mid equals the lowest v
        if(lo == hi):
            if (total < n):
                return mid + 1
            if (total > n):
                return mid
        if (total < n):
            lo = mid + 1
        elif (total > n):
            hi = mid - 1
        elif (total == n):
            return mid
    return -1

# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
