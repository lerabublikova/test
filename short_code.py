import collections
import re


def count_dict_maker(string):
    c = collections.Counter()
    for letter in string:
        c[letter] += 1
    return dict(c)


def code_btree_add(a, b, dictionary):
    binary = 0
    for i in [a, b]:
        for j in i:
            if j in dictionary:
                dictionary[j] = str(binary) + dictionary[j]
            else:
                dictionary[j] = str(binary)
        binary = 1


s = input()
letters = count_dict_maker(s)
print(letters)
cipher = dict()
code_length = 0
quantity = len(letters)
while len(letters) != 1:
    sym1, f1 = min(letters.items(), key=lambda x: x[1])
    letters.pop(sym1)
    sym2, f2 = min(letters.items(), key=lambda x: x[1])
    letters.pop(sym2)
    f_sum = f1 + f2
    letters[sym1 + sym2] = f_sum
    code_length += f_sum
    code_btree_add(sym1, sym2, cipher)
print(quantity, code_length)
for key, value in cipher.items():
    print(key + ': ' + value)
print(cipher)
for sym in s:
    print(cipher[sym], end='')

s = int(re.sub(r'Insert\s(/1)', r'(/1)', s))