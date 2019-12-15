g = input()
g = g.split(",")

g = [int(i) for i in g]

for i in range (0,len(g)):
    if (i%4) == 0:
        if g[i] == 1:
            g[g[i+3]] = g[g[i+1]] + g[g[i+2]]
            continue
        elif g[i] == 2:
            g[g[i+3]] = g[g[i+1]] * g[g[i+2]]
            continue
        elif g[i] == 99:
            print (g)
            break

print (g)

