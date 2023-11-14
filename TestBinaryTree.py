#  File: TestBinaryTree.py

#  Description: Creating multiple helper functions for the Tree class

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 4/15/2022

#  Date Last Modified: 4/15/2022

import sys

class Node (object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild
    def __str__(self):
        if(self.data == None):
            return ''
        return str(self.data)

class Tree (object):
    def __init__(self):
        self.root = None
        self.preorder = ''

    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lChild
                else:
                    current = current.rChild

            if (data < parent.data):
                parent.lChild = new_node
            else:
                parent.rChild = new_node

    # takes in a list of numbers to create a tree
    # returns a tree
    def create_tree (self, nodes):
        tree = Tree()
        for i in nodes:
            tree.insert(i)
        return tree

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        if (self.num_nodes() != pNode.num_nodes()):
            return False
        tree1 = self.pre_order(self.root).split()
        tree2 = pNode.pre_order(pNode.root).split()
        for i in range(len(tree1)):
            if (tree1[i] != tree2[i]):
                return False
        return True

    # this function should generate the preorder notation of the tree
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if (aNode != None):
            self.preorder += str(aNode.data) + ' '
            self.pre_order(aNode.lChild)
            self.pre_order(aNode.rChild)
        return self.preorder

    # Returns a list of nodes at a given level from left to right
    def get_level (self, level):
        if (self.is_empty()):
            node = Node()
            node.data = ''
            return [node]
        if (level == 0):
            return [self.root]
        if (level > self.get_height()):
            return [None]
        else:
            nodes = []
            self.get_level_helper(self.root, level, 0, nodes)
            return nodes

    # Finds a certain level in a tree and prints the nodes in that level
    def get_level_helper (self, node, level, iterator, list):
        if (node == None):
            return
        if (level == iterator):
            list.append(node)
        else:
            self.get_level_helper(node.lChild, level, iterator + 1, list)
            self.get_level_helper(node.rChild, level, iterator + 1, list)

    # Returns the height of the tree
    def get_height (self):
        if (self.is_empty()):
            return -1
        else:
            return self.update_height(self.root)

    # Finds the height of the tree
    def update_height (self, node):
        if (node == None):
            return -1
        else:
            return max(1 + self.update_height(node.lChild), 1 + self.update_height(node.rChild))

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        if (self.is_empty()):
            return 0
        else:
            return self.num_nodes_helper(self.root)

    # Recursively finds the number of nodes in the tree
    def num_nodes_helper (self, node):
        if (node == None):
            return 0
        else:
            return  1 + self.num_nodes_helper(node.lChild) + self.num_nodes_helper(node.rChild)

    # Returns true if the tree is empty
    def is_empty (self):
        if (self.root == None):
            return True
        else:
            return False

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints

    tree1 = Tree().create_tree(tree1_input)
    tree2 = Tree().create_tree(tree2_input)
    tree3 = Tree().create_tree(tree3_input)
    tree4 = Tree()
    # Test your method is_similar()
    print(tree1.is_similar(tree2))
    print(tree1.is_similar(tree3))
    # Print the various levels of two of the trees that are different
    print(tree1.get_level(1))
    print(tree4.get_level(0))
    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())
    # Get the total number of nodes a binary search tree
    print(tree1.num_nodes())
if __name__ == "__main__":
    main()
