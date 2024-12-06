# Part One

def loadMap(file):
    tempMap = list()
    for line in file:
        tempMap.append(list(line.strip()))
    return(tempMap)

# fhand = open('day6sample.txt')
fhand = open('day6.txt')

guardMap = loadMap(fhand)

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
print('Number of Iterations',l)
    


# Part Two

# reset map
guardMap = loadMap(fhand)

maxLoops = 100000