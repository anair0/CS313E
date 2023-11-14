#  File: DNA.py

#  Description: Prints longest common sequence(s) between pairs of DNA sequences

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 1/23/2022

#  Date Last Modified: 1/24/2022

import sys

#Input: string s
#Output: returns a list of all substrings of s
def all_substrs(s):
    #create a list to store the substrings
    substrs = []

    #get the size of the window
    wnd = len(s)

    #find all substrings
    while(wnd > 0):
        start_idx = 0
        while((start_idx + wnd) <= len(s)):
            sub_string = s[start_idx: start_idx + wnd]
            substrs.append(sub_string)
            start_idx += 1
        wnd = wnd - 1

    return substrs


# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence(s1, s2):
    substrs_lst = []
    s1_substrs = all_substrs(s1)
    start_idx = 0
    for i in range(len(s1_substrs)):
        if(s1_substrs[i] in s2):
            if(substrs_lst):
                if(len(s1_substrs[i]) > len(substrs_lst[start_idx])):
                    substrs_lst.append(s1_substrs[i])
                elif(len(s1_substrs[i]) == len(substrs_lst[start_idx])):
                    substrs_lst.append(s1_substrs[i])
            else:
                substrs_lst.append(s1_substrs[i])
    substrs_lst = list(set(substrs_lst))
    substrs_lst = sorted(substrs_lst)
    return substrs_lst


def main():
    # read the number of pairs
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)

    # for each pair call the longest_subsequence
    for i in range(num_pairs):
        st1 = sys.stdin.readline()
        st2 = sys.stdin.readline()

        st1 = st1.strip()
        st2 = st2.strip()

        st1 = st1.upper()
        st2 = st2.upper()

        # get the longest subsequences
        long_sub = longest_subsequence(st1, st2)

        # print the result
        if(long_sub):
            for i in range(len(long_sub)):
                print(long_sub[i])
        else:
            print('No Common Sequence Found')
        # insert blank line
        print('')

#Test Cases
def test_cases():
    #test the function longest_subsequence()
    assert longest_subsequence('','') == []
    assert longest_subsequence('abcd','abcd') == ['abcd']
    assert longest_subsequence('abcd','bcef') == ['bc']
    assert longest_subsequence('abcd','xyz') == []
    assert longest_subsequence('aabcaa','aadaa') == ['aa']

if __name__ == "__main__":
    main()