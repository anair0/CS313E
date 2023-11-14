#  File: WinStreak.py

#  Description: Determines the teams with the longest win streak

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue if empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)

    def __str__(self):
        s = ''
        for i in range(len(self.queue)):
            s += self.queue[i] + ' '
        return s[:-1]


# Input: players is a list of people who are playing the game
#        winners is an ordered string of the winning teams
# Output: A list of the team(s) with the longest win streak in chronological order
#         The player who has been on the team the longest should be listed first
#         Each team is represented by a string structure as follows "Player1 Player2"
def longest_win_streak(players, winners):
    red = Queue()
    blue = Queue()

    red.enqueue(players[0])
    blue.enqueue(players[1])
    red.enqueue(players[2])
    blue.enqueue(players[3])

    reserve = Queue()
    for i in range(4, len(players)):
        reserve.enqueue(players[i])

    r_count = 0
    b_count = 0
    max_count = 0
    for i in range(len(winners)):
        if (winners[i] == 'R'):
            if (i != 0):
                if (winners[i - 1] == 'R'):
                    r_count += 1
                else:
                    r_count = 1
            else:
                r_count = 1
        if (winners[i] == 'B'):
            if (i != 0):
                if (winners[i - 1] == 'B'):
                    b_count += 1
                else:
                    b_count = 1
            else:
                b_count = 1
        if (r_count > max_count):
            max_count = r_count
        elif (b_count > max_count):
            max_count = b_count
    win_streaks = []
    current_rwins = 0
    current_bwins = 0
    for i in range(len(winners)):
        if (winners[i] == 'R'):
            current_bwins = 0
            reserve.enqueue(blue.dequeue())
            blue.enqueue(reserve.dequeue())
            current_rwins += 1
            if (current_rwins == max_count):
                copy = red.__str__()
                win_streaks.append(copy)
        if (winners[i] == 'B'):
            current_rwins = 0
            reserve.enqueue(red.dequeue())
            red.enqueue(reserve.dequeue())
            current_bwins += 1
            if (current_bwins == max_count):
                copy = blue.__str__()
                win_streaks.append(copy)
    return win_streaks


# DO NOT MODIFY THIS METHOD
def main():
    # read number of players
    n = int(input())

    players = list(map(str, input().split()))
    # read data from standard input
    winners = input()

    # get the result from your call to flip_matrix()
    teams = longest_win_streak(players, winners)

    # print the result to standard output
    for team in teams:
        print(team)


if __name__ == "__main__":
    main()
