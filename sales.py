def sales(cars, customers):
    cars.sort()
    customers.sort()
    sales = 0
    i = 0
    j = 0
    while i < len(cars):
        while j < len(customers):
            if customers[j] >= cars[i]:
                cars.pop(i)
                customers.pop(j)

                sales += 1
                break
            j += 1
        else:
            i += 1

    return sales

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5