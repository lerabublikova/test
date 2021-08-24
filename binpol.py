import sys
n = int(input())
a = list(map(float, input().split()))
l = -100
r = 100
y = 10
while abs(y) > pow(10, -6):
    m = (r + l)/2
    y = 0
    for i in range(n + 1):
        y += pow(m, i) * a[i]
    if y > 0:
        r = m
    else:
        l = m
print(m)

n = int(input())
a = list(map(float, input().split()))
l = -100
r = 100
y = 10
while abs(y) > pow(10, -7):
    m = (r + l)/2
    y = 0
    for i in range(n + 1):
        y += pow(m, i) * a[i]
    if y > 0:
        r = m
    else:
        l = m
print(m)