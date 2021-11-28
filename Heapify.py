import time

A = []
f = open(r"C:\Users\Sebastian\PycharmProjects\Algorytmy-Projekt\ReversedSortedNumbers.txt", "r", encoding="utf-8")
for line in f:
    A.append(int(line))

def Max_Heapify(A,n,i):
    l = 2*i+1
    r = 2*i+2
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        Max_Heapify(A,n,largest)

def Build_Max_Heapify(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        Max_Heapify(A,n,i)

def HeapSort(A):
    n = len(A)
    Build_Max_Heapify(A)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        Max_Heapify(A,i,0)

t1 = time.time()
HeapSort(A)
t2 = time.time()
print(t2-t1)
# for i in range(len(A)):
#     print(A[i],end=' ')