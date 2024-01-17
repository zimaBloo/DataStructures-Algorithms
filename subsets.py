#Looping through all possible subsets was done with bit manipulation, learned here: https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/
#Checking i-th bit was learned here https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset

def subsets(N):
    listSubs = []
    maxSubs = 1 << N

    for i in range(1, maxSubs):
        subset = []

        for j in range(0, N):
            if ((1 << j) & i):  #The second source helped me solve and implement this
                subset.append(j+1)
        listSubs.append(subset)

    return listSubs


if __name__ == "__main__":
    print(subsets(1))   # [[1]]
    print(subsets(2))   # [[1], [2], [1, 2]]
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]