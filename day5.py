# Part One

# fhand = open('day5sample.txt')
fhand = open('day5.txt')

rules = list()
updates = list()

for line in fhand:
    if line.find('|') > 0:
        rule = tuple(line.strip().split('|'))
        rule = [int(x) for x in rule]
        rules.append(rule)
    if line.find(',') > 0:
        update = line.strip().split(',')
        update = [int(x) for x in update]
        updates.append(update)

def midValue(a):
    return(a[int(len(a)/2)])

middlePageSum = 0
incorrectUpdates = list()

for update in updates:
    errorCount = 0
    for i, page in enumerate(update):
        priorPages = update[0:i]
        pageMustBeBefore = [rule[1] for rule in rules if rule[0] == page]
        for priorPage in priorPages:
            if priorPage in pageMustBeBefore: errorCount +=1
    if errorCount == 0: middlePageSum += midValue(update)
    else: incorrectUpdates.append(update)

print("Part One Answer:", middlePageSum)

# Part Two

correctedUpdates = list()

for update in incorrectUpdates:
    sorter = list()
    for page in update:
        pageMustBeBefore2 = [rule[1] for rule in rules if rule[0] == page and rule[1] in update]
        sorter.append((page, len(pageMustBeBefore2)))
    sorter.sort(key=lambda tup: tup[1], reverse=True)
    sortedUpdate = [x[0] for x in sorter]
    correctedUpdates.append(sortedUpdate)

middlePageSum = 0
for update in correctedUpdates:
    middlePageSum += midValue(update)

print("Part Two Answer:", middlePageSum)