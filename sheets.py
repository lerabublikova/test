import sys


def find(i, parent):
    while parent[i - 1][0] != i:
        i = parent[i - 1][0]
    return parent[i - 1][0]


def union(i, j, parent, sizes):
    i = find(i, parent)
    j = find(j, parent)
    if i != j:
        sizes[j - 1] += sizes[i - 1]
        sizes[i - 1] = 0
        parent[i - 1][0] = j
        return sizes[j - 1]
    else:
        return 0


def main():
    n, m = tuple(map(int, sys.stdin.readline().split()))
    sizes = list(map(int, sys.stdin.readline().split()))
    max_size = max(sizes)
    parent = [[0 for j in range(2)] for i in range(n)]
    for i in range(n):
        parent[i][0] = i + 1
    for i in range(m):
        print(sizes)
        i, j = tuple(map(int, sys.stdin.readline().split()))
        united_size = union(i, j, parent, sizes)
        print(sizes)
        max_size = max(max_size, united_size)
        print(parent)
        print(max_size)
        # print(parent)


if __name__ == "__main__":
    main()