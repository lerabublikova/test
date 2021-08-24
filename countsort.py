def count_sort(a, n):
    b = [0 for i in range(10)]
    for i in a:
        b[i - 1] += 1
    for i in range(1, 10):
        b[i] += b[i - 1]
    sorted = [0 for _ in range(n)]
    for j in range(n - 1, -1, -1):
        sorted[b[a[j] - 1] - 1] = a[j]
        b[a[j] - 1] -= 1
    return sorted


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(count_sort(a, n))


if __name__ == "__main__":
    main()