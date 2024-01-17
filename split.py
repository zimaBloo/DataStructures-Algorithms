#Learned to traverse the list backwards here https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
#This website was very helpful and gave me some ideas about how to solve this problem with O(n) complexity https://www.geeksforgeeks.org/partition-array-into-two-subarrays-with-every-element-in-the-right-subarray-strictly-greater-than-every-element-in-left-subarray/

def split(T):
    n = len(T)
    howManySplits = 0
    
    highestValue = []
    for temp in range(n):
        highestValue.append(0)

    lowestValue = []
    for temp2 in range(n):
        lowestValue.append(0)

    highestValue[0] = T[0]
    for j in range(1, n):
        if T[j] > highestValue[j-1]:
            highestValue[j] = T[j]

        else:
            highestValue[j] = highestValue[j-1]
    
    lowestValue[n-1] = T[n-1]
    for l in range(n-2, -1, -1):
        if T[l] < lowestValue[l+1]:
            lowestValue[l] = T[l]

        else:
            lowestValue[l] = lowestValue[l+1]
    

    for m in range(0, n-1):
        if highestValue[m] < lowestValue[m+1]:

            howManySplits += 1
      
      
    return howManySplits

if __name__ == "__main__":
    print(split([1,2,3,4,5]))       # 4
    print(split([5,4,3,2,1]))       # 0
    print(split([2,1,2,5,7,6,9]))   # 3
    print(split([1,2,3,1]))         # 0