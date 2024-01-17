def pairs(s):
    distanceSum = 0
    positionsOf1 = []
    totalSum = [0]

    for i in range(len(s)):
        if s[i] == "1":
            positionsOf1.append(i)
        i += 1

    for j in range(len(positionsOf1)):
        temp = totalSum[j] + positionsOf1[j]
        totalSum.append(temp)

    for j in range(len(positionsOf1)):
        futurePositions = len(positionsOf1) - (j+1)
        
        lastOne = totalSum[len(totalSum)-1]
        distanceSum += lastOne - totalSum[j+1] - positionsOf1[j] * futurePositions

    return distanceSum

if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71