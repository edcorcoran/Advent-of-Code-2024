# Part One
# fhand = open('day2sample.txt')
fhand = open('day2.txt')

reports = list()


for line in fhand:
   levels = line.split()
   levels = [int(x) for x in levels]
   reports.append(levels)

monotonic = bool()
gradual = bool()
SafeCount = 0

for levels in reports:
    if levels == sorted(levels):
        monotonic = True
    elif levels == sorted(levels, reverse=True):
        monotonic = True
    else:
        monotonic = False 
    gradual = True
    for i in range(len(levels)):
        if i == 0: continue
        if abs(levels[i] - levels[i-1]) < 1:
            gradual = False
        if abs(levels[i] - levels[i-1]) > 3:
            gradual = False
    if monotonic and gradual:
        SafeCount += 1
    # print(levels, "Monotonic:", monotonic, "Gradual", gradual)
    # input()

print(SafeCount, "Safe Reports")

# Part Two
# fhand = open('day2sample.txt')
fhand = open('day2.txt')

reports = list()


for line in fhand:
   levels = line.split()
   levels = [int(x) for x in levels]
   reports.append(levels)

def SafetyCheck(levels): 
    monotonic = bool()
    gradual = bool()
    if levels == sorted(levels):
        monotonic = True
    elif levels == sorted(levels, reverse=True):
        monotonic = True
    else:
        monotonic = False 
    gradual = True
    for i in range(len(levels)):
        if i == 0: continue
        if abs(levels[i] - levels[i-1]) < 1:
            gradual = False
        if abs(levels[i] - levels[i-1]) > 3:
            gradual = False
    if monotonic and gradual:
        return(True)
    else: return(False)


SafeCount = 0

for levels in reports:
    # Check the normal way
    if SafetyCheck(levels):
        SafeCount += 1
        continue
    
    # Iterate through all subsets of levels that exclude one entry
    for index, level in enumerate(levels):
        levelsSubset = list(levels)
        del levelsSubset[index]
        if SafetyCheck(levelsSubset):
            SafeCount += 1
            break

print(SafeCount, "Safe Reports with Dampener")