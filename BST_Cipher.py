#  File: BST_Cipher.py

#  Description: A binary search tree encryption and decryption scheme

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 4/16/2022

#  Date Last Modified: 4/18/2022

import sys

class Node (object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    def __str__(self):
        if (self.data == None):
            return ''
        return str(self.data)

class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        encrypt_lst = []
        for i in range(len(encrypt_str)):
            if ((ord(encrypt_str[i]) >= 97 and ord(encrypt_str[i]) <= 122) or ord(encrypt_str[i]) == 32):
                encrypt_lst.append(encrypt_str[i])
        for i in range(len(encrypt_lst)):
            self.insert(encrypt_lst[i])

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        new_node = Node(ch)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (ord(ch) < ord(current.data)):
                    current = current.lChild
                elif (ord(ch) == ord(current.data)):
                    return
                else:
                    current = current.rChild

            if (ord(ch) < ord(parent.data)):
                parent.lChild = new_node
            elif (ord(ch) == ord(parent.data)):
                return
            else:
                parent.rChild = new_node

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        str = ''
        if (self.root == None):
            return
        if (self.root.data == ch):
            str = '*'
            return str
        else:
            current = self.root
            while (current != None):
                if (ch < current.data):
                    current = current.lChild
                    str = str + '<'
                elif (ch == current.data):
                    return str
                else:
                    current = current.rChild
                    str = str + '>'
            return ''

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        st_lst = []
        for i in range (len(st)):
            st_lst.append(st[i])
        current = self.root
        if (st_lst[0] == '*'):
            return self.root.data
        for i in range (len(st_lst)):
            if (st_lst[i] == '<'):
                if (current != None):
                    current = current.lChild
                    continue
                else:
                    return ''
            if (st_lst[i] == '>'):
                if (current != None):
                    current = current.rChild
                else:
                    return ''
        if (current.data != None):
            return current.data
        else:
            return ''

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        st = st.lower()
        ch_lst = []
        for i in range(len(st)):
            if ((ord(st[i]) >= 97 and ord(st[i]) <= 122) or ord(st[i]) == 32):
                ch_lst.append(st[i])
        encrypted = ''
        for i in range (len(ch_lst)):
            if (i == len(ch_lst) - 1):
                encrypted = encrypted + self.search(ch_lst[i])
                break
            encrypted = encrypted + self.search(ch_lst[i]) + '!'
        return encrypted

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        ch_lst = []
        for i in range (len(st)):
            ch_lst.append(st[i])
        decrypted = ''
        directions = ''
        for i in range (len(ch_lst)):
            if (ch_lst[i] == '!'):
                decrypted = decrypted + self.traverse(directions)
                directions = ''
            elif (i == len(ch_lst) - 1):
                directions = directions + ch_lst[i]
                decrypted = decrypted + self.traverse(directions)
                break
            else:
                directions = directions + ch_lst[i]
        return decrypted

def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()