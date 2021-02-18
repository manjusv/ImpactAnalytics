def getRaiseDropPoints(input, n):

    result = []
    # collect all x points from input
    xPoints = set()
    for i in range(n):
        xPoints.add(input[i][0])
        xPoints.add(input[i][1])

    xPoints = sorted(xPoints)
    # print inseted elements of the set
    # print(f"xPoints : {xPoints}")

    points = {}
    i = 0
    for i in range(n):
        for j in range(input[i][0], input[i][1] + 1):
            if(j in xPoints):
                # possiblePoints = PossiblePoints()
                possiblePoints = {}
                possiblePoints['height']= input[i][2]
                if(j == input[i][0] or j == input[i][1]):
                    possiblePoints['isEdge'] = True
                else:
                    possiblePoints['isEdge'] = False
                # print(f"for x={j}, dict:{possiblePoints}")
                if j not in points.keys():
                    points[j] = [possiblePoints]
                else:
                    points[j].append(possiblePoints)

    # print("points dict: {}".format(points))

    # Now we have max height for all the x values in points dict
    # start with some max height
    lastHeight = 1000

    for x in xPoints:
        random = points[x]
        random = sorted(random, reverse=True, key= lambda x: x['height'])
        found = False
        if(random[0]['height'] == lastHeight and random[0]['isEdge'] == False):
            continue

        for y in random:
            if(y['height'] != lastHeight):
                # print(f"{x} and {y['height']}")
                result.append((x, y['height']))
                lastHeight = y['height']
                found = True
                break

        if(found == False):
            # print(f"{x} and {0}")
            result.append((x, 0))
            lastHeight = 0
    return result


if __name__ == "__main__":
    input = [(1, 2, 8), (3, 6 ,4), (3, 6, 10), (4, 7, 6), (5, 8, 12)]
    # Output - [(1, 8), (2, 0), (3, 10), (5, 12), (8, 0)]
    
    # input = [(1,10,4),(1,8,6),(1,6,8)]
    # Output - [(1,8),(6,6),(8,4),(10,0)]

    # input = [(0,6,2),(5,10,8),(7,8,12)]
    # Output - [(0,2), (5,8),(7,12),(8,8) (10,0)]

    # input = [(1,5,10),(4,6,8),(10,15,10),(11,12,8)]
    # Output - [(1,10),(5,8),(6,0),(10,10),(15,0)]

    # input = [(0,6,2),(5,10,8),(7,8,12)]
    # Output = [(0, 2), (5, 8), (7, 12), (8, 8), (10, 0)]

    # input = [(1,8,8),(5,7,12)]
    # Output = [(1, 8), (5, 12), (7, 8), (8, 0)]

    # input = [(1,2,8),(2,6,10),(3,6,4),(5,7,6),(5,9,12)]
    # Output = [(1, 8), (2, 10), (5, 12), (9, 0)]
    n = len(input)
    res = getRaiseDropPoints(input, n)
    print(f"input: {input}")
    print(f"output: {res}")
        