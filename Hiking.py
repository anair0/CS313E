#  File: Hiking.py

#  Description: Help Jeff determine if he can finish the Appalachian Trail hike

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  def push (self, item):
    self.stack.insert (0, item )

  def pop (self):
    return self.stack.pop(0)

  def peek (self):
    return self.stack[0]

  def isEmpty (self):
    return (len(self.stack) == 0)

  def size (self):
    return (len(self.stack))

def hike(hike_string: str, capacity: int) -> bool:
    backpack = Stack()
    for i in range(len(hike_string)):
        if (hike_string[i] == '.'):
            continue
        if (hike_string[i] == 'b' or hike_string[i] == 'f' or hike_string[i] == 'c'):
            if (backpack.size() < capacity):
                backpack.push(hike_string[i])
                continue
            else:
                continue
        if (hike_string[i] == 'p'):
            if (backpack.isEmpty()):
                return False
            if (backpack.peek() == 'b'):
                backpack.pop()
                continue
            else:
                return False
        if (hike_string[i] == 'm'):
            if (backpack.isEmpty()):
                return False
            if (backpack.peek() == 'c'):
                backpack.pop()
                continue
            else:
                return False
        if (hike_string[i] == 's'):
            if (backpack.isEmpty()):
                return False
            if (backpack.peek() == 'f'):
                backpack.pop()
                continue
            else:
                return False

    return backpack.isEmpty()


# You do not need to modify anything below this line
def main():
    first_line = sys.stdin.readline().split()
    N, W = int(first_line[0]), int(first_line[1])

    for _ in range(N):
        hike_string = sys.stdin.readline().strip()
        print(hike(hike_string, W))

if __name__ == "__main__":
    main()