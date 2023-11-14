#  File: Reducible.py

#  Description: Finds the longest words that are reducible from a word list

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/23/2022

#  Date Last Modified: 3/25/2022

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word (s, size):
    key = len(s)
    idx = 0
    for j in range (key):
        letter = ord (s[j]) - 96
        idx = (idx * 26 + letter) % size
    return idx

# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size (s, const):
    key = len(s)
    size_step = 0
    for j in range(key):
        letter = ord(s[j]) - 96
        size_step = const - ((size_step * 26 + letter) % const)
    return size_step

# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    length = len(hash_table)
    hash_idx = hash_word(s, length)
    # Goal is to find first empty space to insert word in hash table
    if (hash_table[hash_idx] == ''):
        hash_table[hash_idx] = s
        return
    step = step_size(s, 17)
    while (hash_table[hash_idx] != ''):
        hash_idx = (hash_idx + step) % length
    hash_table[hash_idx] = s

# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word (s, hash_table):
    idx = hash_word(s, len(hash_table))
    step = step_size(s, 17)
    length = len(hash_table)
    if (hash_table[idx] == s):
        return True
    while (hash_table[idx] != s):
        idx = (idx + step) % length
        #if it gets to an empty space without finding the string then it is not in the hash table
        if (hash_table[idx] == ''):
            return False
    return True

# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    if (s == 'a' or s == 'i' or s == 'o'):
        return True
    elif (find_word(s, hash_memo)):
        return True
    #This elif is to reduce the depth of recursions whenever the word is not reducible
    elif (find_word(s, hash_table) == False):
        return False
    elif('a' in s or 'o' in s or 'i' in s):
        for i in range(len(s)):
            word = s[:i] + s[i+1:]
            if (is_reducible(word, hash_table, hash_memo)):
                insert_word(s, hash_memo)
                return True

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    max = 0
    longest_words = []
    for i in range(len(string_list)):
        if (len(string_list[i]) == max):
            longest_words.append(string_list[i])
        if (len(string_list[i]) > max):
            longest_words = []
            max = len(string_list[i])
            longest_words.append(string_list[i])
    return longest_words

def main():

    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append (line)

    # find length of word_list
    length = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    n = 0
    temp = (length * 2) + 1
    while (n == 0):
        if (is_prime(temp)):
            n = temp
            n = int(n)
            break
        else:
            temp += 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for i in range(n):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    m = 0
    temp = 0.2 * length
    while (m == 0):
        if (is_prime(temp)):
            m = temp
            m = int(m)
            break
        else:
            temp += 1

    hash_memo = []

    # populate the hash_memo with M blank strings
    for i in range(m):
       hash_memo.append('')

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for word in word_list:
        if (is_reducible(word, hash_list, hash_memo)):
            reducible_words.append(word)

    # find the largest reducible words in reducible_words
    longest_words = get_longest_words(reducible_words)
    longest_words.sort()

    # print the reducible words in alphabetical order
    # one word per line
    for word in longest_words:
        print(str(word))


if __name__ == "__main__":
    main()
