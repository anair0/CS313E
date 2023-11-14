#  File: PirateMap.py

#  Description: Share a treasure islands map with your pirate friends

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120


import sys

class Island(object):
    """
    A class representing a single island
    You may add attributes to the Island class, but do not 
    modify any of the __str__, __eq__, __ne__, __lt__, __gt__, 
    __le__, or __ge__ functions
    """

    def __init__(self, label: str):
        self.label = label
        self.adj_islands = []
        self.visited = False
        # TODO: add any additional attributes here

    def __str__(self):
        adj_str = ""
        sorted_adj_islands = sorted(self.adj_islands)
        for i in range(len(sorted_adj_islands)):
            adj_str += sorted_adj_islands[i].label + " "
        return self.label + ": " + adj_str

    def __eq__(self, other):
        return ord(self.label) == ord(other.label)

    def __ne__(self, other):
        return ord(self.label) != ord(other.label)

    def __lt__(self, other):
        return ord(self.label) < ord(other.label)

    def __gt__(self, other):
        return ord(self.label) > ord(other.label)

    def __le__(self, other):
        return ord(self.label) <= ord(other.label)

    def __ge__(self, other):
        return ord(self.label) >= ord(other.label)
        

class PirateMap(object):
    """
    A class representing the pirate map
    Do not modify the __str__ function
    """
    def __init__(self):
        self.islands = {}

    def __str__(self):
        res = ""
        for k in sorted(self.islands.keys()):
            v = self.islands[k]
            res += v.__str__()
            res += "\n"
        return res
    
def share_pirate_map(island: Island) -> PirateMap:
    """
    Given a starting island, reconstruct the pirate map to share with
    your fellow pirates
    """
    # TODO: Your code here
    map = PirateMap()
    map.islands[island.label] = island
    map.islands[island.label].visited = True
    islands = set()
    islands.add(island.label)
    for i in range(len(island.adj_islands)):
        map.islands[island.adj_islands[i].label] = island.adj_islands[i]
        islands.add(island.adj_islands[i].label)
        for j in range(len(island.adj_islands[i].adj_islands)):
           map.islands[island.adj_islands[i].adj_islands[j].label] = island.adj_islands[i].adj_islands[j]
           islands.add(island.adj_islands[i].adj_islands[j].label)
    length = len(islands)
    islands = list(islands)
    Test = True
    for key in map.islands.keys():
        for i in range(len(map.islands[key].adj_islands)):
            if (map.islands[key].adj_islands[i].label not in islands):
                Test = False
    if Test == True:
        return map
    for i in range(length):
        p = islands[i]
        for j in range(len(map.islands[p].adj_islands)):
            map.islands[map.islands[p].adj_islands[j].label] = map.islands[p].adj_islands[j]
            if (map.islands[p].adj_islands[j].label not in islands):
                islands.append(map.islands[p].adj_islands[j].label)
                length += 1
            elif(map.islands[p].adj_islands[j].adj_islands[0].label not in islands or
            map.islands[p].adj_islands[j].adj_islands[0].label not in islands):
                islands.append(map.islands[p].adj_islands[j].adj_islands[0].label)
                length += 1
    while (len(islands) != len(map.islands)):
        for i in range(len(islands)):
            p = islands[i]
            for j in range(len(map.islands[p].adj_islands)):
                map.islands[map.islands[p].adj_islands[j].label] = map.islands[p].adj_islands[j]
                if (map.islands[p].adj_islands[j].label not in islands):
                    islands.append(map.islands[p].adj_islands[j].label)
                    length += 1
                elif (map.islands[p].adj_islands[j].adj_islands[0].label not in islands or
                      map.islands[p].adj_islands[j].adj_islands[0].label not in islands):
                    islands.append(map.islands[p].adj_islands[j].adj_islands[0].label)
                    length += 1


    """
    current = map.islands[island.label]
    while (True):
        for i in range(len(current.adj_islands)):
            if (current.adj_islands[i].label not in map.islands):
                map.islands[current.adj_islands[i].label] = current.adj_islands[i]
                islands.add(current.adj_islands[i].label)
                for j in range(len(current.adj_islands[i].adj_islands)):
                   islands.add(current.adj_islands[i].adj_islands[j].label)
        for i in range(len(current.adj_islands)):
            if (current.adj_islands[i].visited == False):
                current.adj_islands[i].visited = True
                current = current.adj_islands[i]
                break
        print(islands)
        print(map.islands)
        if (len(islands) == len(map.islands)):
            return map
    """

    return map

def main():
    """
    Modify this code below at your own risk
    """
    num_islands = int(sys.stdin.readline().strip())

    # Add islands to our map
    pirate_map = PirateMap()
    start_island_label = sys.stdin.readline().strip()

    for i in range(num_islands):
        line = sys.stdin.readline().strip()
        island = Island(line)
        pirate_map.islands[island.label] = island

    for i in range(num_islands):
        line = sys.stdin.readline().split()
        island = pirate_map.islands[line[0].strip()]

        adj_islands_labels = line[1:]
        for j in range(len(adj_islands_labels)):
            island.adj_islands.append(
                pirate_map.islands[adj_islands_labels[j]])
            
    shared_map = share_pirate_map(pirate_map.islands[start_island_label])
    print(shared_map)

if __name__ == "__main__":
    main()