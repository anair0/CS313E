#  File: Intervals.py

#  Description: Takes in N intervals and merges overlapping intervals and sorts them by interval size

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 1/28/2022

#  Date Last Modified: 1/29/2022

import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):
    merged_tuples = []
    #Goes through each tuple in the list multiple times as it updates to ensure all mergers happen
    for i in range(len(tuples_list)):
        if(tuples_list[i] == ' '):
            continue
        #Accounts for if the interval has the same min and max number
        if(tuples_list[i][0] == tuples_list[i][1]):
            for k in range(len(tuples_list)):
                if(tuples_list[k] == ' '):
                    continue
                if(tuples_list[i][0] > tuples_list[k][0] and tuples_list[i][1] < tuples_list[k][1]):
                    tuples_list[i] = ' '
                    break
            continue
        for j in range(len(tuples_list)):
            if(tuples_list[j] == ' '):
                continue
            if(tuples_list[i] == tuples_list[j]):
                continue
            #Find the minimum out of the upper ends
            min_num = min(tuples_list[i][1],tuples_list[j][1])
            #Find the higher out of the lower ends
            max_num = max(tuples_list[i][0],tuples_list[j][0])
            overlap = min_num - max_num
            #Check that there is an overlap before merging
            if(overlap > 0):
                min_num = min(tuples_list[i][0],tuples_list[j][0])
                max_num = max(tuples_list[i][1],tuples_list[j][1])
                new_tuple = (min_num, max_num)
                tuples_list[i] = new_tuple
                tuples_list[j] = (' ')
            #These two elifs are to join intervals that only have one end matching
            elif(tuples_list[i][1] == tuples_list[j][0]):
                new_tuple = (tuples_list[i][0], tuples_list[j][1])
                tuples_list[i] = new_tuple
                tuples_list[j] = (' ')
            elif(tuples_list[j][1] == tuples_list[i][0]):
                new_tuple = (tuples_list[j][0], tuples_list[i][1])
                tuples_list[i] = new_tuple
                tuples_list[j] = (' ')
    #Removing the blank spaces
    for i in range(len(tuples_list)):
        if(tuples_list[i] != ' '):
            merged_tuples.append(tuples_list[i])
    #Sort the merged tuples by the lower number of the interval and output
    merged_tuples = sorted(merged_tuples)

    return merged_tuples

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size(tuples_list):
    for i in range(len(tuples_list)):
        for j in range(len(tuples_list)):
            if(tuples_list[i] == tuples_list[j]):
                continue
            #Finds interval size of two intervals being compared
            interval_size1 = tuples_list[i][1] - tuples_list[i][0]
            interval_size2 = tuples_list[j][1] - tuples_list[j][0]
            #Situates intervals in the list based on which interval is bigger
            if(interval_size1 == interval_size2):
                if(tuples_list[i][0] > tuples_list[j][0] and i < j):
                    temp = tuples_list[j]
                    tuples_list[j] = tuples_list[i]
                    tuples_list[i] = temp
                if (tuples_list[j][0] > tuples_list[i][0] and j < i):
                    temp = tuples_list[j]
                    tuples_list[j] = tuples_list[i]
                    tuples_list[i] = temp
            if(interval_size1 < interval_size2):
                temp = tuples_list[j]
                tuples_list[j] = tuples_list[i]
                tuples_list[i] = temp

    return tuples_list

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases
  assert merge_tuples([(1,2), (2,3)]) == [(1,3)]
  assert merge_tuples([(1,7), (6,6)]) == [(1,7)]
  assert merge_tuples([(1,2), (3,4)]) == [(1,2), (3,4)]
  assert merge_tuples([(1,3), (20,30), (3,7), (0,50)]) == [(0,50)]
  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases
  assert sort_by_interval_size([(2,3), (1,2)]) == [(1,2), (2,3)]

  return "all test cases passed"


def main():
  # read the input data and create a list of tuples
  tuples_list = []
  num_intervals = sys.stdin.readline()
  num_intervals = num_intervals.strip()
  num_intervals = int(num_intervals)

  for i in range(num_intervals):
      line = sys.stdin.readline()
      line = line.strip()
      space_idx = line.index(' ')
      num1 = int(line[0:space_idx])
      num2 = int(line[space_idx:len(line)])
      num_tuple = (num1, num2)
      tuples_list.append(num_tuple)

  # merge the list of tuples
  merged_tuples = merge_tuples(tuples_list)
  # print the merged list
  print(merged_tuples)
  # sort the list of tuples according to the size of the interval
  sorted_tuples = sort_by_interval_size(merged_tuples)
  # run your test cases
  test_cases()
  #Commented out the test cases printing due to it messing with gradescope
  #print(test_cases())


  # print the sorted list
  print(sorted_tuples)

if __name__ == "__main__":
  main()