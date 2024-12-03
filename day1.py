# Part One
# fhand = open('day1sample.txt')
fhand = open('day1.txt')
list1 = list()
list2 = list()

for line in fhand:
   words = line.split()
   list1.append(int(words[0]))
   list2.append(int(words[1]))

list1.sort()
list2.sort()

totalDistance = 0

for i in range(len(list1)):
    totalDistance += abs(list1[i] - list2[i])

print("Total Distance", totalDistance)

#Part Two

# fhand = open('day1sample.txt')
fhand = open('day1.txt')
list1 = list()
list2 = list()

for line in fhand:
   words = line.split()
   list1.append(int(words[0]))
   list2.append(int(words[1]))

list1.sort()
list2.sort()

SimilarityScore = 0
CurrCount = 0

for i in list1:
   for j in list2:
      if i == j:
        CurrCount += 1
   SimilarityScore += i * CurrCount
   CurrCount = 0
    

print("Similarity Score", SimilarityScore)