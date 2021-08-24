import sys

def popheap(heap, n):
    swap(0, n - 1, heap)
    h = heap.pop()
    n -= 1
    shiftdown(0, n, heap)
    return h, n

def addheap(el, heap, n):
    heap.append(el)
    n += 1
    shiftdown(n // 2 - 1, n, heap)
    return n


def swap(i, minindex, heap):
    s = heap[i]
    heap[i] = heap[minindex]
    heap[minindex] = s


def shiftdown(i, n, heap):
    minindex = i
    if 2 * i + 1 < n and heap[2 * i + 1] < heap[minindex]:
        minindex = 2 * i + 1
    if 2 * i + 2 < n and heap[2 * i + 2] < heap[minindex]:
        minindex = 2 * i + 2
    if minindex != i:
        swap(i, minindex, heap)
        shiftdown(minindex, n, heap)


def build_heap(heap, n):
    for i in range(n // 2 - 1, -1, -1):
        shiftdown(i, n, heap)
    return heap


n = int(input())
heap = list(map(int, input().split()))
heap = build_heap(heap, n)
fee = 0
while len(heap) > 1:
    h1, n = popheap(heap, n)
    h2, n = popheap(heap, n)
    h = h1 + h2
    fee += h * 0.05
    n = addheap(h, heap, n)
print(fee)
