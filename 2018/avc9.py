playercount = 430
last_marble = 7158800

from blist import blist

#playercount = 10
#last_marble = 1618

arr = blist([0,2,1])
dictionary = {}
current_index = 1

playernumber = 3


for marble in range(3,last_marble+1):
    #print (marble)
    if playernumber == playercount+1:
        playernumber = 1
    #print (playernumber)
    if marble%23 == 0:
        #print (current_index)
        if current_index == 7:
            current_index = 0
        elif current_index > 7:
            current_index = current_index - 7
        else:
            subtract_amount = current_index
            subtract_amount = 7 - subtract_amount
            current_index = (len(arr)) - subtract_amount
        val = arr[current_index]
        arr.pop(current_index)
        #print (current_index, val)
        if playernumber in dictionary:
            dictionary[playernumber] += val + marble
            #print (playernumber)
        else:
            dictionary[playernumber] = marble + val
            # print (playernumber)
    else:
        if current_index+2 == len(arr):
            current_index = len(arr)
            arr.append(marble)
        elif current_index+2 == len(arr)+1:
            current_index = 1
            arr.insert(current_index,marble)
        else:
            current_index += 2
            arr.insert(current_index,marble)
    playernumber += 1

# print (len(arr))
# print (arr)

maximum = max(dictionary.values())
print (maximum)
