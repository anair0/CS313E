#  File: PowerLines.py

#  Description: Determines how many power lines must be built to connect everyone to power

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
          (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
          new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

# Input: houses is a Graph of the neighborhood
#        by default, house 0 is always connected to the power plant
# Output: The minimum number of power lines that must be built to connect
#         all houses to power
def needed_lines(houses: Graph) -> int:
    needed = 0
    housenum = len(houses.Vertices)
    length = housenum
    homes = []
    for i in range(housenum):
        homes.append(i)
    homes.remove(0)
    houses.Vertices[0].visited = True
    houses.get_adj_unvisited_vertex(0)
    adj = set()
    for i in range(len(houses.adjMat[0])):
        if (houses.adjMat[0][i] == 1):
            adj.add(i)
            homes.remove(i)
    for k in range(len(houses.Vertices)):
        for i in range(k, len(houses.adjMat[0])):
            if (houses.adjMat[k][i] == 1):
                adj.add(i)

                homes.remove(i)
    needed = len(homes)
    pass


# DO NOT MODIFY THIS METHOD
def main():
    houses = Graph()
    num, n = map(int, input().split())
    for house in range(num):
        # add vertex
        houses.add_vertex(house)

    # read in the adjacency matrix
    for _ in range(n):
        start, finish = map(int, input().split())
        houses.add_undirected_edge(start, finish)

    # get the result from your call to needed_lines()
    min = needed_lines(houses)

    # print the result to standard output
    print(min)


if __name__ == "__main__":
    main()
