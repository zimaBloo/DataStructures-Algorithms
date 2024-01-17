def jumps(n, a, b):
    list = []
    
    for i in range(n + 1):
        list.append(0)

    for j in range(0, n + 1):
        if j == 0:
            list[j] = 1

        temp = 0
        if j - a != 0 or j - a == 0:
            temp = list[j - a]
            list[j] = list[j] + temp

        temp2 = 0
        
        if j - b != 0 or j - b == 0:
            temp2 = list[j - b]
            list[j] = list[j] + temp2

    return list[n]


if __name__ == "__main__":
    print(jumps(4, 1, 2))  # 5
    print(jumps(8, 2, 3))  # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937