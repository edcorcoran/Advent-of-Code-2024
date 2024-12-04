# # Part One
# import re

# fhand = open('day3sample.txt')
# # fhand = open('day3.txt')

# file = fhand.read()

# commandList = re.findall(r'mul\(\d+,\d+\)', file)

# FinalSum = 0

# print(commandList)
# for command in commandList:
#     integerList = re.findall('\d+', command)
#     FinalSum += int(integerList[0])*int(integerList[1])

# print("Part One Final Sum", FinalSum)

# Part Two
import re

# fhand = open('day3sample.txt')
fhand = open('day3.txt')
# fhand = open('day3_subset.txt')

file = fhand.read()
# print(file)

# commandList = re.findall(r'mul\(\d+,\d+\)', file)
commandList = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', file)
# commandList = re.findall(r'mul\(\d+,\d\)|don\'t\(\)|do\(\)', file)

# print(commandList)

FinalSum = 0
enabled = True

for command in commandList:
    if command == 'don\'t()': 
        enabled = False
        continue
    if command == 'do()': 
        enabled = True
        continue
    integerList = re.findall('\d+', command)
    if enabled: 
        FinalSum += int(integerList[0])*int(integerList[1])

print("Part Two Final Sum", FinalSum)