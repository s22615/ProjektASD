import time

A = []
f = open(r"C:\Users\Sebastian\PycharmProjects\Algorytmy-Projekt\ReversedSortedNumbers.txt", "r", encoding="utf-8")
for line in f:
    A.append(int(line))


def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r-1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def QuickSort(A, p, r):
    if len(A) == 1:
        return A
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)


t1 = time.time()
QuickSort(A, 0, len(A) - 1)
t2 = time.time()
print(t2 - t1)
# for i in range(len(A)):
#     print(A[i],end=' ')
