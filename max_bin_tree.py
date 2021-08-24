import sys


def shiftup(tree, element, len_tree):
    k = len_tree - 1
    while bool(k):
        if tree[(k - 1) // 2] < element:
            tree[k] = tree[(k - 1) // 2]
            tree[(k - 1) // 2] = element
            k = (k - 1) // 2
        else:
            break


def shiftdown(tree, len_tree, k=0):
    while 2 * k + 1 < len_tree:
        max_index = min(len_tree - 1, 2 * (k + 1))
        max_val = max(tree[2 * (k + 1) - 1], tree[max_index])
        if tree[k] < max_val:
            if tree[2 * (k + 1) - 1] > tree[max_index]:
                tree[2 * (k + 1) - 1] = tree[k]
                tree[k] = max_val
                k = 2 * (k + 1) - 1
            else:
                tree[max_index] = tree[k]
                tree[k] = max_val
                k = max_index
        else:
            break


def line_creater():
    line = []
    length = 0
    for _ in range(int(sys.stdin.readline())):
        s = sys.stdin.readline()
        if s.startswith("Insert"):
            s = int(s[7:])
            line.append(s)
            length += 1
            shiftup(line, s, length)
        else:
            print(line[0])
            length -= 1
            if length > 1:
                line[0] = line.pop()
                shiftdown(line, length)
            else:
                line.pop()


if __name__ == "__main__":
    line_creater()
