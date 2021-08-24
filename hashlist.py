import sys
from collections import deque


def hashcode(text, l, m, x=263, p=1000000007):
    samp_code = 0
    cur_x = 1
    for i in range(l):
        samp_code = (samp_code + (ord(text[i]) * cur_x) % p) % p
        cur_x = (cur_x * x) % p
    return samp_code % m


def main():
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    hash_table = [deque() for _ in range(m)]
    for i in range(n):
        #print(hash_table)
        text = sys.stdin.readline().strip().split()
        if text[0] in ['add', 'find', 'del']:
            string = text[1]
            l = len(string)
            number = hashcode(string, l, m)
            if text[0] == 'add':
                if string not in hash_table[number]:
                    hash_table[number].appendleft(string)
            elif text[0] == 'find':
                state = False
                for s in hash_table[number]:
                    if s == string:
                        state = True
                        print('yes')
                        break
                if not state:
                    print('no')
            else:
                if string not in hash_table[number]:
                    continue
                else:
                    hash_table[number].remove(string)
        if text[0] == 'check':
            i = int(text[1])
            if not hash_table[i]:
                print('')
            else:
                for s in hash_table[i]:
                    print(s, end=' ')
                print()


if __name__ == "__main__":
    main()
