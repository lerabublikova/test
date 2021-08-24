sec = []
n = int(input())
for i in range(n):
    sec.append([int(i) for i in input().split()])
sec = sorted(sec, key=lambda x: x[0])
i = 0
while i < len(sec) - 1:
    if sec[i + 1][0] <= sec[i][1]:
        sec[i] = [sec[i + 1][0], min(sec[i][1], sec[i + 1][1])]
        sec.remove(sec[i + 1])
    else:
        sec[i] = sec[i][0]
        i += 1
sec[-1] = sec[-1][0]
print(len(sec))
for dot in sec:
    print(dot, sep=' ')