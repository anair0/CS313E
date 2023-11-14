#  File: TestLinkedList.py

#  Description: Creating a linked list class with helper functions

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 4/3/2022

#  Date Last Modified: 4/4/2022

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        count = 0
        current = self.first
        while (current.next != None):
            count += 1
            current = current.next
        count += 1
        return count

    # add an item at the beginning of the list
    def insert_first(self, data):
        if (self.is_empty()):
            newLink = Link(data)
            newLink.next = None
            self.first = newLink
            return
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    # add an item at the end of a list
    def insert_last(self, data):
        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        current = self.first
        if (current.data > data):
            newLink = Link(data)
            newLink.next = self.first
            self.first = newLink
            return
        while (current.next != None):
            if (current.next.data > data):
                newLink = Link(data)
                newLink.next = current.next
                current.next = newLink
                return
            current = current.next
        self.insert_last(data)

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        if (self.is_empty()):
            return None
        current = self.first
        while (current.next != None):
            if (current.data == data):
                return data
            current = current.next
        if (current.data == data):
            return data
        return None

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        if (self.is_empty()):
            return None
        current = self.first
        while (current.next != None):
            if (current.data == data):
                return data
            elif (current.data > data):
                return None
            current = current.next
        if (current.data == data):
            return data
        return None

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        if (self.is_empty()):
            return None
        current = self.first
        if (current.data == data):
            self.first = current.next
            return data
        while (current.next != None):
            if (current.next.data == data):
                current.next = current.next.next
                return data
            current = current.next
        return None

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        if (self.is_empty()):
            return ''
        current = self.first
        count = 0
        string = ''
        while (current.next != None):
            if (count < 10):
                string = string + str(current.data) + '  '
            else:
                string = string + '\n' + str(current.data) + '  '
                count = 1
            current = current.next
            count += 1
        if (count < 10):
            string = string + str(current.data) + '  '
        else:
            string = string + '\n' + str(current.data) + '  '
        return string

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        current = self.first
        new_list = LinkedList()
        while (current.next != None):
            new_list.insert_last(current.data)
            current = current.next
        new_list.insert_last(current.data)
        return new_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        current = self.first
        length = self.get_num_links()
        nums = []
        new_list = LinkedList()
        for i in range(length):
            if (i == length - 1):
                nums.append(current.data)
                break
            nums.append(current.data)
            current = current.next
        nums.sort()
        for i in nums:
            new_list.insert_first(i)
        return new_list
        pass

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        current = self.first
        length = self.get_num_links()
        nums = []
        new_list = LinkedList()
        for i in range(length):
            if (i == length - 1):
                nums.append(current.data)
                break
            nums.append(current.data)
            current = current.next
        nums.sort()
        for i in nums:
            new_list.insert_last(i)
        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        while (current.next != None):
            if (current.data > current.next.data):
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if (self.first == None):
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        current1 = self.first
        current2 = other.first
        new_list = LinkedList()
        while (current1.next != None):
            current1 = current1.next
        if (current1.data < current2.data):
            current1 = self.first
            while(current1.next != None):
                new_list.insert_last(current1.data)
                current1 = current1.next
            new_list.insert_last(current1.data)
            while (current2.next != None):
                new_list.insert_last(current2.data)
                current2 = current2.next
            new_list.insert_last(current2.data)
            return new_list
        current1 = self.first
        while (current1.next != None or current2.next != None):
            if (current1.data < current2.data):
                new_list.insert_last(current1.data)
                current1 = current1.next
            else:
                new_list.insert_last(current2.data)
                current2 = current2.next
        if (current1.data < current2.data):
            new_list.insert_last(current1.data)
            new_list.insert_last(current2.data)
        else:
            new_list.insert_last(current2.data)
            new_list.insert_last(current1.data)
        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current1 = self.first
        current2 = other.first
        if (self.get_num_links() != other.get_num_links()):
            return False
        while (current1.next != None and current2.next != None):
            if (current1.data != current2.data):
                return False
            current1 = current1.next
            current2 = current2.next
        if (current1.data != current2.data):
            return False
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        occurrences = []
        new_list = LinkedList()
        current = self.first
        while (current.next != None):
            if (current.data not in occurrences):
                new_list.insert_last(current.data)
                occurrences.append(current.data)
            current = current.next
        if (current.data not in occurrences):
            new_list.insert_last(current.data)
        return new_list

def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    test = LinkedList()
    for i in range(10):
        test.insert_first(i)
    print(test)

    # Test method insert_last()
    test = LinkedList()
    for i in range(10):
        test.insert_last(i)
    print(test)

    # Test method insert_in_order()

    # Test method get_num_links()
    print(test.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    b = LinkedList()
    c = LinkedList()
    c.insert_first(12)
    c.insert_first(7)
    c.insert_first(19)
    print(b.find_unordered(7))
    print(c.find_unordered(7))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    d = LinkedList()
    e = LinkedList()
    e.insert_first(1)
    e.insert_first(2)
    e.insert_first(3)
    print(d.find_unordered(7))
    print(e.find_unordered(3))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print(d.delete_link(2))
    print(e.delete_link(2))

    # Test method copy_list()
    f = e.copy_list()
    print(f)

    # Test method reverse_list()
    print(f.reverse_list())

    # Test method sort_list()
    print(f.sort_list())

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print(f.is_sorted())
    print(c.is_sorted())

    # Test method is_empty()
    print(test.is_empty())
    a = LinkedList()
    print(a.is_empty())

    # Test method merge_list()
    t = LinkedList()
    t.insert_first(4)
    t.insert_first(5)
    t.insert_first(6)
    s = LinkedList()
    s.insert_first(1)
    s.insert_first(2)
    s.insert_first(3)
    print(s.merge_list(t))

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(s.is_equal(f))
    print(s.is_equal(s))

    # Test remove_duplicates()
    s.insert_last(3)
    print(s.remove_duplicates())

if __name__ == "__main__":
    main()
