import sys
from collections import deque
import heapq


def main():
    n, m = (map(int, sys.stdin.readline().split()))
    process = deque(map(int, sys.stdin.readline().split()))
    priorque  = []
    for i in range(n):
        priorque.append([0, i])
    heapq.heapify(priorque)
    for p in process:
        el = heapq.heappop(priorque)
        for i in reversed(el):
            print(i, end=' ')
        print()
        el[0] += p
        heapq.heappush(priorque, el)

if __name__ == "__main__":
    main()