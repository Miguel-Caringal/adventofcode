import numpy as np
from collections import defaultdict

d = defaultdict(list)
with open('C:\\day3.txt') as f:
   content = f.readlines()
content = [x.strip() for x in content]

twod = []

for _ in range(0,1000,1):
    list = []
    for _ in range (0,1000,1):
        list2 = 0
        list.append(list2)
    twod.append(list)

setofoverlap = set()

def getnum(id):
    str = ""
    for char in id:
        if char.isdigit():
            str+=char
    return str

#Part 1
"""
for entry in content:
    left,right = entry.split(":")
    width,height = right.split("x")
    id,important = left.split ("@")
    xcoord,ycoord = important.split(",")
    width = int(width)
    height = int(height)
    xcoord = int(xcoord)
    ycoord = int(ycoord)
    id = getnum(id)
    key = True
    for currentxcord in range(xcoord+1,xcoord+width+1,1):
        for currentycoord in range(ycoord+1,ycoord+height+1,1):
            #print (currentxcord,currentycoord)
            if twod [currentycoord][currentxcord] == 0:
                twod[currentycoord][currentxcord] = id
            elif twod[currentycoord][currentxcord] != 0:
                key = False
                twod[currentycoord][currentxcord] = id
                setofoverlap.add((currentxcord,currentycoord))
            if not (currentycoord, currentxcord) in d:
                d[(currentycoord, currentxcord)] = [id]
            else:
                d[(currentycoord, currentxcord)].append(id)

print len(setofoverlap)
"""

# Part 2
"""
for entry in content:
    left,right = entry.split(":")
    width,height = right.split("x")
    id,important = left.split ("@")
    xcoord,ycoord = important.split(",")
    width = int(width)
    height = int(height)
    xcoord = int(xcoord)
    ycoord = int(ycoord)
    id = getnum(id)
    key = True
    for currentxcord in range(xcoord+1,xcoord+width+1,1):
        for currentycoord in range(ycoord+1,ycoord+height+1,1):
            if (currentycoord,currentxcord) in d:
                if id in d[currentycoord,currentxcord] and len(d[currentycoord,currentxcord]) > 1:
                    key = False
    if key == True:
        print id
"""