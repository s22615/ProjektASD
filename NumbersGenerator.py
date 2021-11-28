import random

A = []

def generate(n):
    for i in range(n):
        r = random.randint(0,1000)
        A.append(r)

generate(1000)
f = open(r"C:\Users\Sebastian\PycharmProjects\Algorytmy-Projekt\RandomNumbers.txt", "w", encoding="utf-8")
for i in range(len(A)):
    f.write(str(A[i]) + "\n" )
f.close()
f = open(r"C:\Users\Sebastian\PycharmProjects\Algorytmy-Projekt\SortedNumbers.txt", "w", encoding="utf-8")
A.sort()
for i in range(len(A)):
    f.write(str(A[i]) + "\n" )
f.close()
f = open(r"C:\Users\Sebastian\PycharmProjects\Algorytmy-Projekt\ReversedSortedNumbers.txt", "w", encoding="utf-8")
A.reverse()
for i in range(len(A)):
    f.write(str(A[i]) + "\n" )
f.close()
