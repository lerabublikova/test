import math

n = 255255 * 257257
a = int(pow(2, math.floor(math.log(n, 2)))) + 1
b = n - a

print(a)
print(b)

b_c = b // 2
a_c = a + b // 2

#a_c = a // 2
#b_c = b + a // 2
count = 1
while a_c != a:
    if a_c % 2:
        b_c //= 2
        a_c += b_c
    else:
        a_c //= 2
        b_c += a_c
    count += 1

print(count)