# Part One

import copy

def loadMap(filename):
    fhand = open(filename)
    tempMap = list()
    for line in fhand:
        tempMap.append(list(line.strip()))
    fhand.close()
    return(tempMap)

# filename = 'day6sample.txt'
filename = 'day6.txt'

guardMap = loadMap(filename)

row_max = len(guardMap)-1 # minus one to handle start at zero
col_max = len(guardMap[0])-1

guardState = ''
guardPath = [[0] * (col_max+1) for i in range(row_max+1)]

# find starting point
for i, row in enumerate(guardMap):
    for j, col in enumerate(row):
        if col in ['^','v', '>','<']:
            guardState = col
            guardPosition = (i,j)

#move guard
i = guardPosition[0]
j = guardPosition[1]
l = 0
while True:
    match guardState:
        case '^':
            if i == 0:
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                break
            elif guardMap[i-1][j] == '.':
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                guardMap[i-1][j] = guardState
                i = i-1
            elif guardMap[i-1][j] == '#':
                guardMap[i][j] = '>'
                guardState = '>'
        case 'v':
            if i == row_max:
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                break
            elif guardMap[i+1][j] == '.':
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                guardMap[i+1][j] = guardState
                i = i+1
            elif guardMap[i+1][j] == '#':
                guardMap[i][j] = '<'
                guardState = '<'
        case '>':
            if j == col_max:
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                break
            elif guardMap[i][j+1] == '.':
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                guardMap[i][j+1] = guardState
                j = j+1
            elif guardMap[i][j+1] == '#':
                guardMap[i][j] = 'v'
                guardState = 'v'
        case '<':
            if j == 0:
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                break
            elif guardMap[i][j-1] == '.':
                guardPath[i][j] = 1
                guardMap[i][j] = '.'
                guardMap[i][j-1] = guardState
                j = j-1
            elif guardMap[i][j-1] == '#':
                guardMap[i][j] = '^'
                guardState = '^'
    # print("After iteration",l)
    l = l+1
    # for row in guardMap: print(row)

TotalCells=0
for row in guardPath:
    TotalCells += sum(row)

print('Part One Answer',TotalCells)
# print('Number of Iterations',l)
    


# Part Two

# reset map
guardMap = loadMap(filename)
maxLoops = 100000
positionCount = 0


def testGuardMap(testMap):
    # find starting point
    for i, row in enumerate(testMap):
        for j, col in enumerate(row):
            if col in ['^','v', '>','<']:
                testState = col
                testPosition = (i,j)
    #move guard
    i = testPosition[0]
    j = testPosition[1]
    l = 0
    while True:
        if l > maxLoops: return(True)
        match testState:
            case '^':
                if i == 0:
                    testMap[i][j] = '.'
                    return(False)
                elif testMap[i-1][j] == '.':
                    testMap[i][j] = '.'
                    testMap[i-1][j] = testState
                    i = i-1
                elif testMap[i-1][j] == '#':
                    testMap[i][j] = '>'
                    testState = '>'
            case 'v':
                if i == row_max:
                    testMap[i][j] = '.'
                    return(False)
                elif testMap[i+1][j] == '.':
                    testMap[i][j] = '.'
                    testMap[i+1][j] = testState
                    i = i+1
                elif testMap[i+1][j] == '#':
                    testMap[i][j] = '<'
                    testState = '<'
            case '>':
                if j == col_max:
                    testMap[i][j] = '.'
                    return(False)
                elif testMap[i][j+1] == '.':
                    testMap[i][j] = '.'
                    testMap[i][j+1] = testState
                    j = j+1
                elif testMap[i][j+1] == '#':
                    testMap[i][j] = 'v'
                    testState = 'v'
            case '<':
                if j == 0:
                    testMap[i][j] = '.'
                    return(False)
                elif testMap[i][j-1] == '.':
                    testMap[i][j] = '.'
                    testMap[i][j-1] = testState
                    j = j-1
                elif testMap[i][j-1] == '#':
                    testMap[i][j] = '^'
                    testState = '^'
        l = l+1



# put a # in each cell and see what happens.
for i, row in enumerate(guardMap):
    for j, col in enumerate(row):
        if col == '.':
            copyMap = copy.deepcopy(guardMap)
            copyMap[i][j] = '#'
            # test if stuck
            positionCount += testGuardMap(copyMap)
            # reset the map
            # guardMap[i][j] = '.'
            #problem appears to be that I'm changing guardMap in memory and then reloading it while also iterating on it.
            # maybe make a copy or something? 
            # guardMap = loadMap(filename)

print("Part Two Answer",positionCount)