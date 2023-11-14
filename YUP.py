#  File: Radix.py

#  Description: Sorts a list of strings/digits using a modified Radix Sort algorithm

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/27/2022

#  Date Last Modified: 3/27/2022

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

# Input: string_list a list of words
# Output: returns the length of the string with the max length
def get_longest_word (string_list):
    max = 0
    for i in range(len(string_list)):
        if (len(string_list[i]) > max):
            max = len(string_list[i])
    return max

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    queue_list = []
    for i in range(36):
        queue_list.append(Queue())
    pass_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
                 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16, 'h':17, 'i':18,
                 'j':19, 'k':20, 'l':21, 'm':22, 'n':23, 'o':24, 'p':25, 'q':26, 'r':27,
                 's':28, 't':29, 'u':30, 'v':31, 'w':32, 'x':33, 'y':34, 'z':35}

    max_length = get_longest_word(a)
    iterator = -1
    for i in range(len(a)):
        if (len(a[i]) < max_length):
            diff = max_length - len(a[i])
            for j in range(diff):
                a[i] = a[i] + ' '

    while (max_length > -1):
        for j in range(len(a)):
            if (iterator < - len(a[j])):
                value = pass_dict[a[j][0]]
                queue_list[value].enqueue(a[j])
                continue
            if (a[j][iterator] == ' '):
                queue_list[0].enqueue(a[j])
                continue
            value = pass_dict[a[j][iterator]]
            queue_list[value].enqueue(a[j])
        iterator -= 1
        a = []
        for p in range(len(queue_list)):
            if(queue_list[p].is_empty()):
                continue
            size = queue_list[p].size()
            for l in range(size):
                a.append(queue_list[p].dequeue())
        max_length -= 1

    for i in range(len(a)):
        if (a[i][-1] != ' '):
            continue
        filtered = filter(lambda ch: ch != ' ', a[i])
        a[i] = ''.join(filtered)

    return a


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    '''
    # print word_list
    print (word_list)
    '''

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_list)


if __name__ == "__main__":
    main()