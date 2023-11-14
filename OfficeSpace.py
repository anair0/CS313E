#  File: OfficeSpace.py

#  Description: System for determining the implications of employee requests for cubicles in a space

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/10/22

#  Date Last Modified: 2/11/22

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    #Gets the bottom left and top right vertice coordinates of the rectangle
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    #Finds length and width of the rectangle for area
    length = x2 - x1
    width = y2 - y1

    return length * width

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    #Gets the bottom left and top right vertice coordinates of the rectangles
    x1 = int(rect1[0])
    y1 = int(rect1[1])
    x2 = int(rect1[2])
    y2 = int(rect1[3])
    x3 = int(rect2[0])
    y3 = int(rect2[1])
    x4 = int(rect2[2])
    y4 = int(rect2[3])
    if(x4 <= x1 or x3 >= x2 or y3 >= y2 or y4 <= y1):
        return (0, 0, 0, 0)
    #o = overlap rectangle coordinates and finds overlap based on bottom left/top right vertices of rect
    ox1 = max(x1, x3)
    oy1 = max(y1, y3)
    ox2 = min(x4, x2)
    oy2 = min(y2, y4)

    return (ox1, oy1, ox2, oy2)

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
#         space in the office
def unallocated_space (bldg):
    #Checks each row and column of the building to see which spaces are unoccupied denoted by 0
    unallocated = 0
    for row in bldg:
        for col in row:
            if(col == 0):
                unallocated += 1

    return unallocated

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
#         space in the office
def contested_space (bldg):
    contested = 0
    #Checks each row and column of the building 2D list to see which spaces are contested
    for row in bldg:
        for col in row:
            if(col != 0 and col != 1):
                contested += 1

    return contested

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    #Checks the 2D bldg list for any occupied space and if it is uncontested then it counts up
    uncontested = 0
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    width = x2 - x1
    height = y2 - y1
    for j in range(height):
        for k in range(width):
            if (bldg[y1 + j][x1 + k] == 1):
                uncontested += 1

    return uncontested

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    width = office[2]
    height = office[3]
    #Creates a 2d list for the building space
    bldg = [[0 for i in range(width)] for j in range(height)]
    #Uses the coordinates of the employees to map where they are
    for i in range(len(cubicles)):
        x1 = cubicles[i][0]
        y1 = cubicles[i][1]
        x2 = cubicles[i][2]
        y2 = cubicles[i][3]
        width = x2 - x1
        height = y2 - y1
        #Puts a 1 if it is occupied and a 2 if it is contested
        for j in range(height):
            for k in range(width):
                if(bldg[y1 + j][x1 + k] == 0):
                    bldg[y1 + j][x1 + k] = 1
                else:
                    bldg[y1 + j][x1 + k] = 2
    return bldg

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
    assert area ((0, 0, 1, 1)) == 1
    # write your own test cases
    assert overlap ((0, 0, 2, 2), (3, 3, 4, 4)) == (0, 0, 0, 0)
    assert overlap ((0, 0, 5, 5), (3, 3, 8, 8)) == (3, 3, 5, 5)
    assert unallocated_space([[0, 0, 1], [1, 1, 1]]) == 2
    assert unallocated_space([]) == 0
    assert contested_space([[1, 1, 1, 1], [2, 2, 2, 2]]) == 4
    assert contested_space([]) == 0
    assert uncontested_space([[1, 0, 0], [0, 0, 0], [0, 0, 0]], (0, 0, 1, 1)) == 1
    return "all test cases passed"

def main():
    # read the data
    space = sys.stdin.readline()
    space = space.strip()
    space = space.split()
    width = int(space[0])
    height = int(space[1])
    office = (0, 0, width, height)
    total_area = area(office)
    num_employee = sys.stdin.readline()
    num_employee = num_employee.strip()
    num_employee = int(num_employee)
    employees = []
    cubicles = [[0 for i in range(4)] for j in range(num_employee)]
    for i in range(num_employee):
        info = sys.stdin.readline()
        info = info.strip()
        info = info.split()
        info[1] = int(info[1])
        info[2] = int(info[2])
        info[3] = int(info[3])
        info[4] = int(info[4])
        employees.append(info[0])
        cubicles[i] = info[1:5]
    bldg = request_space(office, cubicles)
    # run your test cases

    #print (test_cases())


    # print the following results after computation

    # compute the total office space
    print('Total ' + str(total_area))
    # compute the total unallocated space
    print('Unallocated ' + str(unallocated_space(bldg)))
    # compute the total contested space
    print('Contested ' + str(contested_space(bldg)))
    # compute the uncontested space that each employee gets
    for i in range(len(employees)):
        name = employees[i]
        employee_space = (cubicles[i][0], cubicles[i][1], cubicles[i][2], cubicles[i][3])
        uncontested = uncontested_space(bldg, employee_space)
        print(str(name), str(uncontested))
if __name__ == "__main__":
    main()