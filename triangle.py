def triangle(a, b, c):
    sides = []
    sides.append(a)
    sides.append(b)
    sides.append(c)

    TFtriangle = False

    longestSide = max(sides)
    sumOfOtherSides = sum(sides) - longestSide

    if (sumOfOtherSides > longestSide):
        TFtriangle = True

    return TFtriangle


if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True