import time

A = []
f = open(r"C:\Users\Sebastian\PycharmProjects\Algorytmy-Projekt\ReversedSortedNumbers.txt", "r", encoding="utf-8")
for line in f:
    A.append(int(line))


def InsertionSort(A):
    for i in range(1, len(A)):
        n = A[i]
        j = i - 1
        while j >= 0 and A[j] > n:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = n

t1 = time.time()
InsertionSort(A)
t2 = time.time()
print(t2-t1)
# for i in range(len(A)):
#     print(A[i], end=' ')
