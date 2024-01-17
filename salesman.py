#This page was useful when understanding and doing the task: https://www.geeksforgeeks.org/traveling-salesman-problem-using-branch-and-bound-2/

def salesman(city_map):
    #Initialize values
    optimalP = []
    best = float('infinity')
    nLength = len(city_map)

    def lowerBound(pathFollowing):
        left = 0

        allCities = set(range(nLength))

        visited = set(pathFollowing)
        unvisited = allCities - visited

        for i in unvisited:
            tempLength = len(unvisited)
            if 1 < tempLength:
                distances = []

                for nextC in unvisited - {i}:
                    distToNextCity = city_map[i][nextC]
                    distances.append(distToNextCity)
                    
                smallest = min(distances)


            else:

                firstEncounter = pathFollowing[0]
                distFirstEnc = city_map[i][firstEncounter]
                smallest = distFirstEnc


            left += smallest


        return left

    def visitNode(pathRn, costRn, optimalP, best):

        if nLength == len(pathRn):

            lastVis = pathRn[-1]
            startCit = pathRn[0]

            distanceTotal = city_map[lastVis][startCit]

            absoluteC = costRn + distanceTotal

            if absoluteC < best:
                optimalP = list(pathRn) #Learned to do thise here: https://www.w3schools.com/python/ref_func_list.asp

                best = absoluteC

            return optimalP, best

        for j in range(nLength):

            if j not in pathRn:

                recent = pathRn[-1]
                nextDist = city_map[recent][j]

                costNext = costRn + nextDist
                newPath = lowerBound([j] + pathRn)

                possBest = costNext + newPath


                if best > possBest:
                    optimalP, best = visitNode(pathRn + [j], costNext, optimalP, best)


        return optimalP, best




    optimalP, best = visitNode([0], 0, optimalP, best)


    returnal = optimalP + [0] #Need to return to first node, so [0] is added


    return returnal





if __name__ == "__main__":
    
    cost = 0

    city_map = [
    #     0   1   2   3   4
        [ 0, 12, 19, 16, 29],   # 0
        [12,  0, 27, 25,  5],   # 1
        [19, 27,  0,  8,  4],   # 2
        [16, 25,  8,  0, 14],   # 3
        [29,  5,  4, 14,  0]    # 4
        ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45