#  File: Boxes.py

#  Description: Finds the number of boxes that can fit in each other and also the number of sets of nesting boxes

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/9/2022

#  Date Last Modified: 3/10/2022

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
    memo = {'max_now':0, 'sets':1}
    count_dict = {}
    reps = 0
    #We look for boxes that have the same value and remove them to decrease processing time
    for i in range(len(box_list)):
        box_list[i] = tuple(box_list[i])
    for i in range(len(box_list)):
        if(box_list[i] not in count_dict):
            count_dict[box_list[i]] = 1
        else:
            count_dict[box_list[i]] += 1
    for key in count_dict:
        if(count_dict[key] > 1):
            reps = count_dict[key]
            for i in range(count_dict[key] - 1):
                box_list.remove(key)

    max_nesting(box_list, memo, 0)

    #Accounts for the boxes that are taken out if they are duplicates
    if(reps != 0):
        memo['sets'] = (reps ** memo['max_now']) * memo['sets']

    return memo['max_now'], memo['sets']

#Finds the set of nested boxes with the greatest number of boxes and how many occurrences that has
def max_nesting (box_list, memo, idx, subset = []):
    #Looks at all the possible subsets that can be made and checks the ones that have boxes that fit
    hi = len(box_list)
    if (idx == hi):
        fit = True
        for i in range(len(subset) - 1):
            if(does_fit(subset[i],subset[i + 1]) == False):
                fit = False
                break
        if (fit == True):
            #Out of the boxes that fit we find the max value and check for the number of occurrences
            if(len(subset) > memo['max_now']):
                memo['max_now'] = len(subset)
                memo['sets'] = 1
            elif(len(subset) == memo['max_now']):
                memo['sets'] += 1
            return memo
    else:
        temp = subset[:]
        subset.append(box_list[idx])
        max_nesting(box_list, memo, idx + 1, subset)
        max_nesting(box_list, memo, idx + 1, temp)

# returns True if box1 fits inside box2
def does_fit (box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort()
        box_list.append (box)

    # print to make sure that the input was read in correctly
    #print (box_list)
    #print()

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    #print (box_list)
    #print()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes (box_list)

    # print the largest number of boxes that fit
    print (max_boxes)

    # print the number of sets of such boxes
    print (num_sets)

if __name__ == "__main__":
    main()
