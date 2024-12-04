# Part One
fhand = open('day2sample.txt')
# fhand = open('day2.txt')

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
fhand = open('day2sample.txt')
# fhand = open('day2.txt')

reports = list()


for line in fhand:
   levels = line.split()
   levels = [int(x) for x in levels]
   reports.append(levels)

SafeCount = 0

for levels in reports:
    ErrorCount = 0
    PrevLevel = 0
    CurrLevel = 0
    IncreasingFlag = False
    DecreasingFlag = False
    for index, level in enumerate(levels):
            if index == 0:
                CurrLevel = level
            elif index == 1:
                PrevLevel = CurrLevel
                CurrLevel = level
                if CurrLevel == PrevLevel: ErrorCount += 1
                if CurrLevel > PrevLevel: IncreasingFlag = True
                if CurrLevel < PrevLevel: DecreasingFlag = True
                if abs(CurrLevel - PrevLevel) > 3: ErrorCount += 1
            else:
                PrevLevel = CurrLevel
                CurrLevel = level
                if IncreasingFlag and CurrLevel <= PrevLevel: 
                    ErrorCount += 1
                    continue
                if DecreasingFlag and CurrLevel >= PrevLevel: 
                    ErrorCount += 1
                    continue
                if abs(CurrLevel - PrevLevel) > 3: 
                    ErrorCount += 1
                    continue 
    if ErrorCount <= 1:
        SafeCount += 1
       

print(SafeCount, "Safe Reports with Dampener")