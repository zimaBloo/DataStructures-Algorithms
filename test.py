def permutations(k):
    if k == n:
        global count
        count += 1
        if count == 50:
            print("50th permutation:", numbers[:])
        if count == 80:
            print("80th permutation:", numbers[:])
        if count == 100:
            print("100th permutation:", numbers[:])
        return
    else:
        for i in range(1, n + 1):
            if not included[i]:
                included[i] = True
                numbers[k] = i
                permutations(k + 1)
                included[i] = False

# Define n as the number of digits for permutations
n = 5
numbers = [0] * n
included = [False] * (n + 1)  # We use 1-based indexing for included
count = 0

permutations(0)