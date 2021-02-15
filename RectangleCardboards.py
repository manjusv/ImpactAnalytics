
def getRaiseDropPoints(input):
    # collect all x points from input
    xPoints = set()
    for i in range(n):
        xPoints.add(input[i][0])
        xPoints.add(input[i][1])

    # print inseted elements of the set
    for element in xPoints:
        print(element, end=' ')

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
                points[j] = possiblePoints

    print("points dict: {}".format(points))

    # Now we have max height for all the x values in points dict
    # start with some max height
    lastHeight = 1000

    for x in xPoints:
        random = points[x]
        found = False
        if(random['height'] == lastHeight and random['isEdge'] == False):
            continue

        if(random['height'] != lastHeight):
            print(f"{x} and {random['height']}")
            lastHeight = random['height']
            found = True

        if(found == False):
            print(f"{x} and {0}")
            lastHeight = 0


if __name__ == "__main__":
    n = 5
    input = [(1, 2, 8), (3, 6 ,4), (3, 6, 10), (4, 7, 6), (5, 8, 12)]
    getRaiseDropPoints(input)
        