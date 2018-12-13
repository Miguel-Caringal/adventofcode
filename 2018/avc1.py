with open('C:\\day1.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

arr2 = []
sum = 0
key = False
while (key == False):
    for index in content:
        index = int(index)
        sum = sum + index
        if sum in arr2:
            print sum
            exit()
        else:
            arr2.append(sum)
