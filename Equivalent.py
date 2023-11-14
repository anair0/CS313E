import sys


# Return True if a and b are equivalent, False otherwise.
def equivalent(a: str, b: str) -> bool:
    if (a == b):
        return True
    alen = len(a)
    blen = len(b)
    a1 = a[0:alen//2]
    a2 = a[alen//2:]
    b1 = b[0:blen//2]
    b2 = b[blen//2:]

    if (equivalent_helper(a1, b1) and equivalent_helper(a2, b2)):
        return True
    elif (equivalent_helper(a1, b2) and equivalent_helper(a2, b1)):
        return True
    else:
        return False

def equivalent_helper(a1, b1):
    if (a1 == b1):
        return True
    if (len(a1) == 1 and a1 != b1):
        return False
    else:
        a1_1 = a1[0:len(a1) // 2]
        a1_2 = a1[len(a1) // 2:]
        b1_1 = b1[0:len(b1) // 2]
        b1_2 = b1[len(b1) // 2:]
        return (equivalent_helper(a1_1, b1_1) and equivalent_helper(a1_2, b1_2)) or \
               (equivalent_helper(a1_1, b1_2) and equivalent_helper(a1_2, b1_1))


# DO NOT CHANGE ANYTHING BELOW THIS LINE

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    print(equivalent(a, b))


if __name__ == "__main__":
    main()
