import re


initialstr = "#.#.#....##...##...##...#.##.#.###...#.##...#....#.#...#.##.........#.#...#..##.#.....#..#.###"
patternstr = """####.#
..#...
#.#...
.##...
##....
#.##.#
##.#..
##..#.
.###..
.#.##.
.#..##
......
###..#
#..##.
##.##.
#.....
...###
....#.
#.#.##
###.#.
.#####
.#...#
#.###.
..###.
.#.#.#
.##.#.
#..#.#
...#..
#...##
..##..
######
..#.##"""
initialstr = list(initialstr)

for i in range(0,5,1):
    initialstr.insert(0, ".")

for i in range(0,1000,1):
    initialstr.append(".")

tempnewstr = ""

for element in initialstr:
    tempnewstr += element
initialstr = tempnewstr

patternstr = patternstr.split("\n")

#print patternstr

for _ in range(0,900,1):
    tempstr = list(initialstr)
    c = 0
    for b in tempstr:
        tempstr[c] = "."
        c+=1
    for pattern in patternstr:
        a = pattern[5]
        pattern = pattern[0:5]
        matcharr = [i for i in range(len(initialstr)) if initialstr.startswith(pattern, i)]
        if matcharr:
            for index in matcharr:
                tempstr[index+2] = a
    newstr = ''
    for element in tempstr:
        newstr += element
    initialstr = newstr
    print initialstr

sum = 0
numtags =0
counter = -5
for char in initialstr:
    if char == "#":
        sum += counter
        numtags += 1
    counter +=1

print sum
print numtags

ans = (50000000000-900) * 20 + sum

print ans