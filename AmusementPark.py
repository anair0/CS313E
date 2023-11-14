class Link (object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList (object):
    def __init__(self):
        self.first = None

    def insertFirst(self, data):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    def insertLast(self, data):
        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink

    def findLink(self, data):
        current = self.first
        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    def deleteLink(self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

# **DO NOT MODIFY ANYTHING ABOVE THIS LINE.**


# Return a linked list with the heights of the children after arranging them
#   based on whether or not they meet the roller coaster height requirement, h.
# You must use the Link and LinkedList classes to complete this question.
# You are **NOT ALLOWED** to use built-in data structures such as lists, sets, dicts,
#   or tuples to store the heights.
def arrangeChildren(heights: LinkedList, h: int) -> LinkedList:
    current = Link(heights.first.data, heights.first.next)
    length = 0
    while (current.next != None):
        length += 1
        current = current.next
    length += 1
    current = Link(heights.first.data, heights.first.next)
    for i in range(length):
        if (int(current.data) >= h):
            new_Link = Link(current.data)
            delete = current.data
            heights.deleteLink(delete)
            heights.insertFirst(new_Link.data)
            current = current.next
        else:
            new_Link = Link(current.data)
            delete = current.data
            heights.deleteLink(delete)
            heights.insertLast(new_Link.data)
            current = current.next
    return heights

# main() is not needed, we will import your code and run it directly
