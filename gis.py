# put your python code here
import sys


def bin_search(lst, element, i, prev):
    left = 0
    right = len(lst)
    if element <= lst[right - 1]:
        lst.append(element)
        prev.append([right + 1, i, element])
    else:
        while right > left:
            m = (right + left) // 2
            if lst[m] >= element:
                left = m + 1
            else:
                right = m
        lst[left] = element
        prev.append([left + 1, i, element])


def max_seq(a, n):
    max_elements = [a[0]]
    prev = [[1, 0, a[0]]]
    for i in range(1, n):
        bin_search(max_elements, a[i], i, prev)
    count = len(max_elements)
    res = []
    for i in range(1, n + 1):
        if prev[-i][0] == count:
            count -= 1
            res.append(prev[-i][1] + 1)
    return len(max_elements), res


def main():
    n = int(sys.stdin.readline())
    a = [int(i) for i in sys.stdin.readline().split()]
    k, b = max_seq(a, n)
    print(k)
    for i in range(k):
        print(b.pop(), end=' ')


if __name__ == "__main__":
    main()