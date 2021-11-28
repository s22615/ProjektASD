import time

A = []
f = open(r"C:\Users\Sebastian\PycharmProjects\Algorytmy-Projekt\ReversedSortedNumbers.txt", "r", encoding="utf-8")
for line in f:
    A.append(int(line))

def Bubblesort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

t1 = time.time()
Bubblesort(A)
t2 = time.time()
print(t2-t1)
# for i in range(len(A)):
#     print(A[i], end=' ')
