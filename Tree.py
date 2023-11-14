# File: Sugar.py

# Description: Help Alex identify if a graph is a tree.

# Student Name: Arjun Nair

# Student EID: asn922

# Course Name: CS 313E

# Unique Number: 51120

import sys

# Feel free to define any helper functions, if necessary!

# Input: n - total number of vertices in graph, edges - set of all edge connections between vertices
# Output: true/false if graph is valid tree
def isTree(n, edges):
    cycle_list = []
    for i in range(len(edges)):
        cycle_list.append(edges[i][0])
        if (edges[i][1] in cycle_list):
            return False
    vertex_dict = {}
    for i in range(n):
        vertex_dict[i] = 0
    for i in range(len(edges)):
        if (edges[i][1] in vertex_dict):
            vertex_dict[edges[i][1]] += 1
            if (vertex_dict[edges[i][1]] > 1):
                return False
    return True

# TAKE CAUTION TO EDIT BELOW
def main():
    n = int(sys.stdin.readline().strip())
    allEdges = []
    for line in sys.stdin:
        edge = list(map(int, line.split(" ")))
        allEdges.append(edge)
    print(isTree(n, allEdges))

if __name__ == "__main__":
    main()
