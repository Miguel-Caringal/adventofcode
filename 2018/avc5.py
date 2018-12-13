from avc5helper import inputstring
from string import ascii_lowercase

def findlen (inputstring):
    matchFound = True
    key = False

    while (matchFound == True):
        matchFound = False
        newstr = ""
        for i in range(0,(len(inputstring)),1):
            if i != len(inputstring)-1:
                if key == True:
                    key = False
                    continue
                if inputstring[i].islower():
                    if inputstring[i+1] == inputstring[i].upper():
                        matchFound = True
                        key = True
                    else:
                        newstr += inputstring[i]
                else:
                    if inputstring[i+1] == inputstring[i].lower():
                        matchFound = True
                        key = True
                    else:
                        newstr += inputstring[i]
            else:
                if key != True:
                    newstr+= inputstring[i]
        inputstring = newstr

    return len(inputstring)

currentmin = 50000

for letter in ascii_lowercase:
    uppercase = letter.upper()
    tempstring = inputstring
    tempstring = tempstring.replace(letter,"")
    tempstring = tempstring.replace(uppercase, "")
    print len(tempstring)
    tempmin = findlen(tempstring)
    if tempmin < currentmin:
        currentmin = tempmin

print(currentmin)
