import sys


def is_in_list(key, lst):
    right = lst[0]
    left = 1
    while right - left > 0:
        index = (right + left) // 2
        if lst[index] == key:
            return index
        elif lst[index] < key:
            left = index + 1
        else:
            right = index - 1
    return -1


def main():
    a = [int(i) for i in sys.stdin.readline().split()]
    b = [int(i) for i in sys.stdin.readline().split()]
    for i in range(1, b[0] + 1):
        print(is_in_list(b[i], a), end=' ')


if __name__ == '__main__':
    main()