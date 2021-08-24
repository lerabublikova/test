# put your python code here
from random import randint
import sys


def swap(a, i, j):
    a_i = a[i]
    a[i] = a[j]
    a[j] = a_i

def bin_search(parts, n, dot):
    l = 0
    r = n - 1
    while r - l > 0:
        m = (r + l) // 2
        if dot > parts[m]:
            l = m + 1
        elif dot < parts[m]:
            r = m - 1
        else:
            while m + 1 < n and dot == parts[m + 1]:
                m += 1
            return m + 1
    if dot > parts[l]:
        return l + 1
    else:
        return l


def bin_search_strict(parts, n, dot):
    l = 0
    r = n - 1
    while r - l > 0:
        m = (r + l) // 2
        if dot > parts[m]:
            l = m + 1
        elif dot < parts[m]:
            r = m - 1
        else:
            while m - 1 >= 0 and dot == parts[m - 1]:
                m -= 1
            return m
    if dot > parts[l]:
        return l + 1
    else:
        return l


def quick_sort3_merge(parts):
    length = len(parts)
    if length > 1:
        more = []
        less = []
        equal = []
        k = randint(0, length - 1)
        swap(parts, 0, k)
        x = parts[0]
        for i in range(length):
            if parts[i] < x:
                less.append(parts[i])
            elif parts[i] == x:
                equal.append(parts[i])
            else:
                more.append(parts[i])
        return quick_sort3_merge(less) + equal + quick_sort3_merge(more)
    else:
        return parts


def quick_sort3(parts, l, r):
    while l < r - 1:
        k = randint(l, r - 1)
        swap(parts, l, k)
        i, j = l + 1, l
        x = parts[l]
        l_old = l
        while i < r:
            if parts[i] <= x:
                swap(parts, i, j + 1)
                j += 1
                if parts[i] == x:
                    swap(parts, l + 1, j)
                    l += 1
            i += 1
        for el in range(l_old, l + 1):
            swap(parts, el, j)
            j -= 1
        if j + 1 - l_old > r - (j + 1 + l - l_old):
            quick_sort3(parts, j + 1 + l - l_old, r)
            l = l_old
            r = j + 1
        else:
            quick_sort3(parts, l_old, j + 1)
            l = j + 1 + l - l_old


def main():
    n, m = (int(i) for i in sys.stdin.readline().split())
    left_parts = []
    right_parts = []
    for _ in range(n):
        parts = [int(i) for i in sys.stdin.readline().split()]
        left_parts.append(parts[0])
        right_parts.append(parts[1])
    left_parts = quick_sort3_merge(left_parts)
    right_parts = quick_sort3_merge(right_parts)
    for dot in [int(i) for i in sys.stdin.readline().split()]:
        print(bin_search(left_parts, n, dot) - bin_search_strict(right_parts, n, dot), end=' ')


if __name__ == "__main__":
    main()