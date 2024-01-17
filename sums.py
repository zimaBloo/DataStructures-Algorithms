def sums(items):

    total = sum(items)

    list = []
    list.append(1)
    upperLimit = total + 1

    for i in range(upperLimit):
        list.append(0)


    for j in items:

        tempList = []
        for _ in list:
            tempList.append(_)

        for k in range(j, upperLimit):
            if list[k - j] != 0:
                tempList[k] = 1

        list = tempList



    answer = sum(list) - 1 #Exclude sum 0

    return answer


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121