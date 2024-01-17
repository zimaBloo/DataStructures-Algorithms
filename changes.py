def changes(A):
    allChanges = 0
    n = len(A)

    for i in range(1, n):
        if A[i] == A[i-1]:

            previous = A[i-1]
            
            if i+1 < n:
                next = A[i+1]

            A[i] = previous + 1
            if A[i] == next:
                A[i] += 1

            allChanges += 1

    return allChanges

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2