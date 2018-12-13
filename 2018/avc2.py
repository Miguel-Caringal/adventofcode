with open('C:\\day2.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

"""
#Part 1
twosum = 0
threesum = 0
for index in content:
    d = {}
    checkertwo = False
    checkerthree = False
    for char in index:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    for key in d:
        if d[key] == 2 and checkertwo is False:
            twosum +=1
            checkertwo = True
        if d[key] == 3 and checkerthree is False:
            threesum +=1
            checkerthree = True

print (twosum*threesum)
"""

"""
#Part 2
for currentid in content:
    for pointingat in content:
        counter = 0
        checkersum = 0
        csarray = []
        for char in currentid:
            if currentid[counter] != pointingat[counter]:
                checkersum+=1
                csarray.append(counter)
            counter +=1
        if checkersum == 1:
            print (csarray[0])
            print (currentid)
"""
