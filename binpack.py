#This source helped me grasp the idea of how this algorithm could be implemented: https://stackoverflow.com/questions/7392143/python-implementations-of-packing-algorithm

def binpack(items, S):
    allBins = []

    #Need to sort in reverse order first, otherewise list is same
    items = sorted(items)[::-1]


    for i in items:
        yesOrNo = False #Check if already appended

        for j in allBins:
            temp = sum(j)

            if S >= temp + i:

                j.append(i)
                yesOrNo = True

                break
        
        

        #New bin if not appended

        if yesOrNo == False:
            toAppendList = [i]
            allBins.append(toAppendList)


    return allBins



if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

# A possible output:
#   bin 1: [9]
#   bin 2: [3, 3, 4]
#   bin 3: [6, 3]
#   bin 4: [10]
#   bin 5: [6]
#   bin 6: [8]
#   bin 7: [6]