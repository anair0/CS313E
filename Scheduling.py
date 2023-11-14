import sys


# Input: `alice` and `bob` are the lists representing the respective schedules
#   for each student. Each availability schedule is represented as a list of tuples.
# Output: Return a single list of tuples representing the intervals
#   where both students are available.
def available(alice, bob):
    times = []
    for i in range(len(alice)):
        for j in range(len(bob)):
            if(bob[j][0] <= alice[i][0] and bob[j][1] >= alice[i][1]):
                lo = max(bob[j][0], alice[i][0])
                hi = min(bob[j][1], alice[i][1])
                times.append((lo, hi))
                continue
            elif(alice[i][0] <= bob[j][0] and alice[i][1] >= bob[j][1]):
                lo = max(bob[j][0], alice[i][0])
                hi = min(bob[j][1], alice[i][1])
                times.append((lo, hi))
                continue
            elif(alice[i][1] > bob[j][0]):
                if(alice[i][0] <= bob[j][0] and alice[i][1] <= bob[j][1]):
                    lo = max(bob[j][0], alice[i][0])
                    hi = min(bob[j][1], alice[i][1])
                    times.append((lo, hi))
                    continue
            elif (alice[i][0] < bob[j][1]):
                if(bob[j][0] <= alice[i][0] and bob[j][1] <= alice[i][1]):
                    lo = max(bob[j][0], alice[i][0])
                    hi = min(bob[j][1], alice[i][1])
                    times.append((lo, hi))
                    continue
            if((alice[i][1] >= bob[j][1]) and (bob[j][1] >= alice[i][0])):
                lo = max(bob[j][0], alice[i][0])
                hi = min(bob[j][1], alice[i][1])
                if(lo == hi):
                    continue
                times.append((lo, hi))
                continue
            elif (alice[i][1] <= bob[j][1] and bob[j][0] <= alice[i][1]):
                lo = max(bob[j][0], alice[i][0])
                hi = min(bob[j][1], alice[i][1])
                if (lo == hi):
                    continue
                times.append((lo, hi))
                continue
            elif (alice[i][1] >= bob[j][0] and bob[j][0] >= alice[i][0]):
                lo = max(bob[j][0], alice[i][0])
                hi = min(bob[j][1], alice[i][1])
                if (lo == hi):
                    continue
                times.append((lo, hi))
                continue
            elif (alice[i][0] <= bob[j][1] and bob[j][0] <= alice[i][0]):
                lo = max(bob[j][0], alice[i][0])
                hi = min(bob[j][1], alice[i][1])
                if (lo == hi):
                    continue
                times.append((lo, hi))
                continue
    return times


# DO NOT MODIFY ANYTHING BELOW THIS LINE
def main():
    a_lines = int(sys.stdin.readline())
    alice = []
    for _ in range(a_lines):
        line = sys.stdin.readline().strip().split(" ")
        alice.append((int(line[0]), int(line[1])))

    b_lines = int(sys.stdin.readline())
    bob = []
    for _ in range(b_lines):
        line = sys.stdin.readline().strip().split(" ")
        bob.append((int(line[0]), int(line[1])))

    print(available(alice, bob))


if __name__ == "__main__":
    main()
