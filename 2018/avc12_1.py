from avc12helper import initialstr,patternstr
import re

patternlist = patternstr.split('\n')


initialstr = str(initialstr)

for _ in range(1,21,1):
    newstr = initialstr
    newstr = list(newstr)
    for pattern in patternlist:
        pattern = str(pattern)
        check = [m.start() for m in re.finditer(pattern, initialstr)]
        if check:
            for occurence in check:
                print (newstr)
                newstr[occurence+2] = "#"
    initialstr = ''.join(str(e)for e in newstr)

print (initialstr)