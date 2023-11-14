#  File: Poly.py

#  Description: Represent polynomials as linked lists and add/multiply them

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 4/8/2022

#  Date Last Modified: 4/8/2022

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        if (self.is_empty()):
            self.first = Link(coeff, exp)
            return
        current = self.first
        if (exp > current.exp):
            newLink = Link(coeff, exp)
            newLink.next = self.first
            self.first = newLink
            return
        while (current.next != None):
            if (exp > current.next.exp):
                newLink = Link(coeff, exp)
                newLink.next = current.next
                current.next = newLink
                return
            current = current.next
        self.insert_last(coeff, exp)

    # add an item at the end of a list
    def insert_last(self, coeff, exp):
        newLink = Link(coeff, exp)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if (self.first == None):
            return True
        else:
            return False

    # get number of links
    def get_num_links(self):
        if (self.is_empty() == True):
            return 0
        count = 0
        current = self.first
        while (current.next != None):
            count += 1
            current = current.next
        count += 1
        return count

    def internal_add (self):
        current = self.first
        exp_list = []
        while (current.next != None):
            if (current.exp not in exp_list):
                exp_list.append(current.exp)
            current = current.next
        if (current.exp not in exp_list):
            exp_list.append(current.exp)
        current = self.first
        temp = LinkedList()
        length = self.get_num_links()
        for i in exp_list:
            coeff = 0
            for j in range(length):
                if (current.exp == i):
                    coeff = coeff + current.coeff
                current = current.next
            temp.insert_in_order(coeff, i)
            current = self.first
        return temp

    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        sum = LinkedList()
        if (self.is_empty() == True):
            return p
        if (p.is_empty() == True):
            return self
        q = self.internal_add()
        p2 = p.internal_add()
        q_current = q.first
        p_current = p2.first
        q_length = q.get_num_links()
        p_length = p2.get_num_links()
        while (p_length != 0 and q_length != 0):
            if (q_current.exp == p_current.exp):
                coeff = q_current.coeff + p_current.coeff
                if (coeff != 0):
                    sum.insert_in_order(coeff, q_current.exp)
                q_current = q_current.next
                p_current = p_current.next
                p_length -= 1
                q_length -= 1
                continue
            if (q_current.exp > p_current.exp):
                sum.insert_in_order(q_current.coeff, q_current.exp)
                q_current = q_current.next
                q_length -= 1
                continue
            if (p_current.exp > q_current.exp):
                sum.insert_in_order(p_current.coeff, p_current.exp)
                p_current = p_current.next
                p_length -= 1
        if (p_length == 0 and q_length != 0):
            while (q_current.next != None):
                sum.insert_in_order(q_current.coeff, q_current.exp)
                q_current = q_current.next
            sum.insert_in_order(q_current.coeff, q_current.exp)
        if (p_length != 0 and q_length == 0):
            while (p_current.next != None):
                sum.insert_in_order(p_current.coeff, p_current.exp)
                p_current = p_current.next
            sum.insert_in_order(p_current.coeff, p_current.exp)
        return sum

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        product = LinkedList()
        q_length = self.get_num_links()
        p_length = p.get_num_links()
        current = self.first
        p_current = p.first
        for i in range(q_length):
            temp = LinkedList()
            for i in range(p_length):
                coeff = current.coeff * p_current.coeff
                exp = current.exp + p_current.exp
                temp.insert_in_order(coeff, exp)
                p_current = p_current.next
            product = product.add(temp)
            current = current.next
            p_current = p.first
        product = product.internal_add()
        return product

    # create a string representation of the polynomial
    def __str__ (self):
        if (self.is_empty()):
            return ''
        if (self.get_num_links() == 1):
            return str(self.first)
        current = self.first
        string = ''
        string = string + str(current) + ' + '
        current = current.next
        while (current.next != None):
            string = string + str(current) + ' + '
            current = current.next
        string = string + str(current)
        return string

def main():
    # read data from file poly.in from stdin
    num = sys.stdin.readline()
    num = num.strip()
    num = int(num)
    p = LinkedList()
    q = LinkedList()
    # create polynomial p
    for i in range(num):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        line[0] = int(line[0])
        line[1] = int(line[1])
        p.insert_in_order(line[0], line[1])
    blank = sys.stdin.readline()
    num = sys.stdin.readline()
    num = num.strip()
    num = int(num)
    # create polynomial q
    for i in range(num):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        line[0] = int(line[0])
        line[1] = int(line[1])
        q.insert_in_order(line[0], line[1])

    # get sum of p and q and print sum
    sum = q.add(p)
    print(sum)
    # get product of p and q and print product
    product = q.mult(p)
    print(product)
if __name__ == "__main__":
    main()