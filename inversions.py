import sys
import math
from collections import deque


def mergesort(q):
    inversions = 0
    len_q = len(q)
    while len_q > 1:
        len_q -= 1
        print(q)
        a1 = q.popleft()
        a2 = q.popleft()
        sum = deque()
        len_a1 = len(a1)
        len_a2 = len(a2)
        i, j = 0, 0
        while i < len_a1 and j < len_a2:
            if a1[0] <= a2[0]:
                sum.append(a1.popleft())
                i += 1
            else:
                sum.append(a2.popleft())
                j += 1
                inversions += len_a1 - i
        if i >= len_a1:
            sum += a2
        else:
            sum += a1
        print(sum)
        q.append(sum)
    return inversions


def main():
    n = int(sys.stdin.readline())
    m = int(math.log(n, 2)) + 1
    q = deque([deque([int(i)]) for i in sys.stdin.readline().split()])
    q = deque([deque([0]) for _ in range(2 ** m - n)]) + q
    print(mergesort(q))


if __name__ == "__main__":
    main()