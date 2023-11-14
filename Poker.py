#  File: Poker.py

#  Description: Simulation of 5 card draw poker game

#  Student's Name: Arjun Nair

#  Student's UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/9/2022

#  Date Last Modified: 2/14/2022

import sys, random

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck (object):
    # constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        for i in range (num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card (rank, suit)
                    self.deck.append (card)

    # shuffle the deck
    def shuffle (self):
        random.shuffle (self.deck)

    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
    # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range (num_players):
            hand = []
            for j in range (self.numCards_in_Hand):
                hand.append (self.deck.deal())
            self.players_hands.append (hand)

    # simulate the play of poker
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse=True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)
        print('')

        # determine the type of each hand and print
        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand
        for i in range(len(self.players_hands)):
            points = 0
            type = ''
            while (points == 0):
                points, type = Poker().is_royal(self.players_hands[i])
                if(points != 0):
                    break
                points, type = Poker().is_straight_flush(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_four_kind(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_full_house(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_flush(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_straight(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_three_kind(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_two_pair(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_one_pair(self.players_hands[i])
                if (points != 0):
                    break
                points, type = Poker().is_high_card(self.players_hands[i])
            hand_points.append(points)
            hand_type.append(type)

        for i in range(len(hand_type)):
            print('Player ' + str(i + 1) + ': ' + hand_type[i])
        print('')

        # determine winner and see if there is a tie and print
        winner = 0
        for i in range(len(hand_points)):
            if(winner < hand_points[i]):
                winner = hand_points[i]
        is_Tie = False
        tie_count = 0
        tie_list = []
        for i in range(len(hand_type)):
            if(hand_type[hand_points.index(winner)] == hand_type[i]):
                tie_count += 1
                tie_list.append([hand_points[i],i])
        tie_list = sorted(tie_list, reverse=True)
        if(tie_count > 1):
            is_Tie = True
        if(is_Tie == False):
            print('Player ' + str(hand_points.index(winner) + 1) + ' wins.')
        if(is_Tie == True):
            for i in range(len(tie_list)):
                print('Player ' + str(tie_list[i][1] + 1) + ' ties.')


    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'

    # determine if a hand is a straight flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_straight_flush (self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

        if (not rank_order):
            return 0, ''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

    # determine if a hand is a four of a kind
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_four_kind (self, hand):
        same_rank = False
        for i in range(len(hand) - 3):
            if (hand[i].rank == hand[i + 1].rank):
                if (hand[i].rank == hand[i + 2].rank):
                    if(hand[i].rank == hand[i + 3].rank):
                        same_rank = True
                        break

        if (not same_rank):
            return 0, ''

        points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Four of a Kind'

    # determine if a hand is a full house
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_full_house (self, hand):
        same_rank = True
        triple = [hand[0].rank, hand[1].rank, hand[2].rank]
        double = [hand[3].rank, hand[4].rank]
        for i in range(len(hand) - 3):
            same_rank = same_rank and (hand[i].rank == hand[i + 1].rank)
        if(hand[3].rank != hand[4].rank):
            same_rank = False
            triple = [hand[2].rank, hand[3].rank, hand[4].rank]
            double = [hand[0].rank, hand[1].rank]
        if(same_rank):
            points = 7 * 15 ** 5 + (triple[0]) * 15 ** 4 + (triple[1]) * 15 ** 3
            points = points + (triple[2]) * 15 ** 2 + (double[0]) * 15 ** 1
            points = points + (double[1])
            return points, 'Full House'
        same_rank = True
        for i in range(len(hand) - 3):
            i = i + 2
            same_rank = same_rank and (hand[i].rank == hand[i + 1].rank)
        if(hand[0].rank != hand[1].rank):
            same_rank = False

        if (not same_rank):
            return 0, ''

        points = 7 * 15 ** 5 + (triple[0]) * 15 ** 4 + (triple[1]) * 15 ** 3
        points = points + (triple[2]) * 15 ** 2 + (double[0]) * 15 ** 1
        points = points + (double[1])

        return points, 'Full House'

    # determine if a hand is a flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_flush (self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'

    # determine if a hand is a straight
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_straight (self, hand):
        num_order = True
        for i in range(len(hand) - 1):
            num_order = num_order and (hand[i].rank == hand[i + 1].rank + 1)

        if (not num_order):
            return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    # determine if a hand is a three of a kind
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_three_kind (self, hand):
        three_kind = False
        three = []
        rest = []
        for i in range(len(hand) - 2):
            if(hand[i].rank == hand[i + 1].rank):
                if(hand[i].rank == hand[i + 2].rank):
                    three_kind = True
                    three.append(hand[i].rank)
                    three.append(hand[i + 1].rank)
                    three.append(hand[i + 2].rank)
                    break

        if (not three_kind):
            return 0, ''

        for i in range(len(hand)):
            if (hand[i].rank not in three):
                rest.append(hand[i].rank)

        points = 4 * 15 ** 5 + (three[0]) * 15 ** 4 + (three[1]) * 15 ** 3
        points = points + (three[2]) * 15 ** 2 + (rest[0]) * 15 ** 1
        points = points + (rest[1])

        return points, 'Three of a Kind'

    # determine if a hand is a two pair
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_two_pair (self, hand):
        two_pair = False
        num_pairs = 0
        pairs = []
        rest = []
        for i in range(len(hand) - 1):
            if(hand[i].rank == hand[i + 1].rank):
                num_pairs += 1
                pairs.append(hand[i].rank)
                pairs.append(hand[i + 1].rank)
                if (num_pairs == 2):
                    two_pair = True
                    break
        if (not two_pair):
            return 0, ''

        for i in range(len(hand)):
            if(hand[i].rank not in pairs):
                rest.append(hand[i].rank)

        points = 3 * 15 ** 5 + (pairs[0]) * 15 ** 4 + (pairs[1]) * 15 ** 3
        points = points + (pairs[2]) * 15 ** 2 + (pairs[3]) * 15 ** 1
        points = points + (rest[0])

        return points, 'Two Pair'

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair (self, hand):
        one_pair = False
        pairs = []
        rest = []
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                pairs.append(hand[i].rank)
                pairs.append(hand[i + 1].rank)
                for j in range(len(hand)):
                    if(hand[j].rank != hand[i].rank):
                        rest.append(hand[j].rank)
                one_pair = True
                break

        if (not one_pair):
            return 0, ''

        points = 2 * 15 ** 5 + (pairs[0]) * 15 ** 4 + (pairs[1]) * 15 ** 3
        points = points + (rest[0]) * 15 ** 2 + (rest[1]) * 15 ** 1
        points = points + (rest[2])

        return points, 'One Pair'

    # determine the highest card in the hand
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_high_card (self,hand):
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'High Card'

def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int (line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker (num_players)

    # play the game
    game.play()

if __name__ == "__main__":
    main()
        
