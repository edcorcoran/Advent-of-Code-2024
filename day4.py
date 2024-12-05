# Part One

# fhand = open('day4sample.txt')
fhand = open('day4.txt')

puzzle = list()

for line in fhand:
   puzzle.append(list(line.strip()))

row_max = len(puzzle)-1 # minus one to handle start at zero
col_max = len(puzzle[0])-1
search_string = ('X','M','A','S')
depth_max = len(search_string)-1
wordcount = 0

def WordSearch(i, j, depth, direction):
    if depth == depth_max and puzzle[i][j] == search_string[-1]:
        return(True)
    elif depth == depth_max: return(False)
    if direction == 'up':
        if puzzle[i][j] == search_string[depth] and i > 0:
            return(WordSearch(i-1,j,depth+1,'up'))
        else: return(False)
    if direction == 'down':
        if puzzle[i][j] == search_string[depth] and i < row_max:
            return(WordSearch(i+1,j,depth+1,'down'))
        else: return(False)
    if direction == 'left':
        if puzzle[i][j] == search_string[depth] and j > 0:
            return(WordSearch(i,j-1,depth+1,'left'))
        else: return(False)
    if direction == 'right':
        if puzzle[i][j] == search_string[depth] and j < col_max:
            return(WordSearch(i,j+1,depth+1,'right'))
        else: return(False)
    if direction == 'upleft':
        if puzzle[i][j] == search_string[depth] and i > 0 and j < col_max:
            return(WordSearch(i-1,j-1,depth+1,'upleft'))
        else: return(False)
    if direction == 'upright':
        if puzzle[i][j] == search_string[depth] and i > 0 and j < col_max:
            return(WordSearch(i-1,j+1,depth+1,'upright'))
        else: return(False)
    if direction == 'downleft':
        if puzzle[i][j] == search_string[depth] and i < row_max and j > 0:
            return(WordSearch(i+1,j-1,depth+1,'downleft'))
        else: return(False)
    if direction == 'downright':
        if puzzle[i][j] == search_string[depth] and i < row_max and j < col_max:
            return(WordSearch(i+1,j+1,depth+1,'downright'))
        else: return(False)


for i, row in enumerate(puzzle):
    for j, cell in enumerate(row):
        if cell == search_string[0]: 
            if i > 0: wordcount += WordSearch(i-1,j,1,'up')
            if i < row_max: wordcount += WordSearch(i+1,j,1,'down')
            if j > 0: wordcount += WordSearch(i,j-1,1,'left')
            if j < col_max: wordcount += WordSearch(i,j+1,1,'right')
            if i > 0 and j > 0: wordcount += WordSearch(i-1,j-1,1,'upleft')
            if i > 0 and j < col_max: wordcount += WordSearch(i-1,j+1,1,'upright')
            if i < row_max and j > 0: wordcount += WordSearch(i+1,j-1,1,'downleft')
            if i < row_max and j < col_max: wordcount += WordSearch(i+1,j+1,1,'downright')

print('Part One Word Count', wordcount)

# Part Two

# fhand = open('day4sample.txt')
fhand = open('day4.txt')

puzzle = list()

for line in fhand:
   puzzle.append(list(line.strip()))

row_max = len(puzzle)-1 # minus one to handle start at zero
col_max = len(puzzle[0])-1
wordcount = 0

for i, row in enumerate(puzzle):
    for j, cell in enumerate(row):
        if cell == 'A': 
            mascount = 0
            if i > 0 and j > 0 and i < row_max and j < col_max: #not too close to an edge 
                upleft = puzzle[i-1][j-1]
                downright = puzzle[i+1][j+1]
                if upleft == 'S' and downright == 'M': mascount += 1
                if upleft == 'M' and downright == 'S': mascount += 1
            
            if i > 0 and j < col_max and i < row_max and j > 0: #not too close to an edge 
                upright = puzzle[i-1][j+1]
                downleft = puzzle[i+1][j-1]
                if upright == 'S' and downleft == 'M': mascount += 1
                if upright == 'M' and downleft == 'S': mascount += 1
            
            if mascount == 2: wordcount += 1
            

print('Part Two Word Count', wordcount)