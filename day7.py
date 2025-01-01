import itertools
import copy
# filename = 'day7sample.txt'
filename = 'day7.txt'

# Part One

fhand = open(filename)
testValues = list()
valueList = list()

for line in fhand:
    testValues.append(int(line.strip().split(':')[0]))
    lineVals = line.strip().split(':')[1].split()
    lineVals = [int(x) for x in lineVals]
    valueList.append(lineVals)
fhand.close()

def processEquation(vals,ops):
    total = vals.pop(0)
    for op in ops:
        if op == '+': total = total + vals.pop(0) 
        if op == '*': total = total * vals.pop(0) 
        if op == '|': total = int(str(total) + str(vals.pop(0)))
    return total

totalCalibrationList = list() # add to this list if it's valid
for i, val in enumerate(testValues):
    operands = valueList[i]
    operatorsSet = list(itertools.product('+*',repeat=len(operands)-1))
    for operators in operatorsSet:
        if val == processEquation(copy.deepcopy(operands),operators): 
            totalCalibrationList.append(val)
            break

print('Part One Answer:', sum(totalCalibrationList))

# Part Two: 

totalCalibrationList = list() # add to this list if it's valid
for i, val in enumerate(testValues):
    operands = valueList[i]
    operatorsSet = list(itertools.product('+*|',repeat=len(operands)-1))
    for operators in operatorsSet:
        if val == processEquation(copy.deepcopy(operands),operators): 
            totalCalibrationList.append(val)
            break

print('Part Two Answer:', sum(totalCalibrationList))