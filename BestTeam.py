#  File: BestTeam.py

#  Description: Determine which subteam is best (highest average score).

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

from typing import Optional

class Node(object):
    """ An employee/node in the business hierarchy. """
    def __init__(
        self,
        val: int,
        left = None,
        right = None
    ) -> None:
        self.val = val
        self.lChild = left
        self.rChild = right

    def __str__(self) -> str:
        return f'({self.val})'

def parse_node_from_string(data: str) -> Optional[Node]:
    """ Parses node from string: (name:data).=> Node object."""

    if data == 'None':
        return None
    # Remove parantheses surrounding and split.
    cleaned = data.replace('(', '').replace(')', '')
    return Node(int(cleaned))

def deserialize(data: str) -> Optional[Node]:
    """ Deserializes the level order string into a tree, returns root node. """
    if len(data) == 0:
        return None
    
    level_order = data.split(', ')
    n = len(level_order)
    
    mapping = {i: parse_node_from_string(level_order[i]) for i in range(n) }
    # slow pointer for parent, fast pointer for child.
    slow = 0
    fast = 1
    
    # denotes where to place child (left or right).
    filled = 0
    
    # assign all children to a parent, stop when none left.
    while fast < len(level_order):
        if filled == 2:
            filled = 0
            slow += 1
        cur = mapping[slow]
        
        if cur is None:
            slow += 1
            continue

        if filled == 0:
            cur.lChild = mapping[fast]
        elif filled == 1:
            cur.rChild = mapping[fast]
        
        filled += 1
        fast += 1

    return mapping[0]


########################################## MODIFY CODE ABOVE AT YOUR OWN RISK ##########################################

def best_team(manager: Node) -> float:
    """ Determine which subteam is best (highest average score).

    Args:
        manager (Node): Root node of the business hierarchy.

    Returns:
        float: The average score of the best subteam.
    """
    average = float(100000)
    current = manager

    pass


if __name__ == '__main__':
    serialized = input().strip()
    root = deserialize(serialized)
    
    # round to hundredth decimal place.
    result = best_team(root)
    print(round(result, 2))

