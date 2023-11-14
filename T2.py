
import math

memo = {'total':0}
def towers (n, source, spare, dest, movement):
    if (n == 1):
        print ('Move disk from', source, 'to', dest)
        memo['total'] += 1
    else:
        towers (n - 1, source, dest, spare, movement)
        print('Move disk from', source, 'to', dest)
        towers (n - 1, spare, source, dest, movement)
        towers (n - 1, spare, source, dest, movement)
        memo['total'] += 1

def towers2 (n, memo):
    if (n == 1):
        memo['total'] += 1
    elif (n == 2):
        memo['total'] += 3
    elif (n == 3):
        memo['total'] += 5
    else:
        k = round(n - math.sqrt(2 * n + 1) + 1)
        k = int(k)
        towers2(k, memo)
        memo['total'] += 1


def main():
    towers2 (28, memo)
    print(memo['total'])

main()