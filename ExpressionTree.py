#  File: ExpressionTree.py

#  Description: Create expression tree and solve the expression

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 4/11/2022

#  Date Last Modified: 4/11/2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']
# These are global string variables that act as memos for the recursive
# pre and post order functions
pre_order = ''
post_order = ''

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild
    def __str__(self):
        if(self.data == None):
            return ''
        return str(self.data)


class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        exp = expr.split()
        current = Node()
        self.root = current
        stack = Stack()
        for i in exp:
            if (i == '('):
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
                continue
            elif (i in operators):
                current.data = i
                stack.push(current)
                current.rChild = Node()
                current = current.rChild
                continue
            elif (i == ')'):
                if (stack.is_empty() == False):
                    current = stack.pop()
            else:
                current.data = i
                current = stack.pop()
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        #Creates post order notation version of tree in a list
        expr = self.post_order(aNode)
        expr = expr.split()
        for i in expr:
            if (i == ' '):
                expr.remove(i)
        operations = 0
        #Finds number of operations done in the equation
        for k in expr:
            if (k in operators):
                operations += 1
        result = 0
        i = 0
        # Finds all the operations and uses dynamic programming to update the list as operations are done
        while (operations != 0):
            if (expr[i + 2] in operators):
                num1 = float(expr.pop(i))
                num2 = float(expr.pop(i))
                operator = expr.pop(i)
                if (operator == '+'):
                    result += num1 + num2
                elif (operator == '-'):
                    result += num1 - num2
                elif (operator == '*'):
                    result += num1 * num2
                elif (operator == '/'):
                    result += num1 / num2
                elif (operator == '//'):
                    result += num1 // num2
                elif (operator == '%'):
                    result += num1 % num2
                elif (operator == '**'):
                    result += num1 ** num2
                operations -= 1
                expr.insert(i, result)
                result = 0
                i = 0
            else:
                i += 1
        #At the end only one number remains in the list which is the answer
        global post_order
        post_order = ''
        answer = expr[0]
        return answer



    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if (aNode != None):
            global pre_order
            pre_order += aNode.data + ' '
            self.pre_order(aNode.lChild)
            self.pre_order(aNode.rChild)
        return pre_order

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if (aNode != None):
            global post_order
            self.post_order(aNode.lChild)
            self.post_order(aNode.rChild)
            post_order += aNode.data + ' '
        return post_order

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()