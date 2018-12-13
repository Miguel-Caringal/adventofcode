import numpy as np

grid_serial_number = 5791

arr = []

# j is x
# i is y

for i in range(1,301,1):
    temp = []
    for j in range(1,301,1):
        rackid = j + 10
        powerlevel = rackid * i
        powerlevel = powerlevel + grid_serial_number
        powerlevel = powerlevel * rackid
        powerlevel = str(powerlevel)
        if len(powerlevel) >=3:
            powerlevel = powerlevel[len(powerlevel)-3]
        else:
            powerlevel = 0
        powerlevel = int(powerlevel)
        powerlevel = powerlevel - 5
        if i == 1 and j == 1:
            print powerlevel
        temp.append(powerlevel)

    arr.append(temp)

maxsum = 0
coords = (0,0)
biglen = 0

# part 1
"""
for x in range(0,300,1):
    for y in range(0,300,1):
        if x <= 297 and y <= 297:
            sum = 0
            sum += arr[y][x]
            sum += arr[y+1][x]
            sum += arr[y+2][x]
            sum += arr[y][x+1]
            sum += arr[y][x+2]
            sum += arr[y+1][x+1]
            sum += arr[y+2][x+2]
            sum += arr[y+2][x+1]
            sum += arr[y+1][x+2]
            if maxsum < sum:
                maxsum = sum
                coords = (x+1,y+1)
"""

"""
for y in range(0,300,1):
    for x in range(0,300,1):
        print (xcoord)
            xcoord = x
            ycoord = y
            while xcoord != 299 or ycoord != 299:
                sum = 0
                for curry in range(x,xcoord+1,1):
                    for currx in range(x,xcoord+1,1):
                        sum += arr[currx][curry]
                        if maxsum < sum:
                            coords = (y+1,x+1)
                            maxsum = sum
                            biglen = xcoord - x
                xcoord +=1
                ycoord +=1

"""

print (coords)

#print arr[22,62]

print np.matrix(arr)

#12,283