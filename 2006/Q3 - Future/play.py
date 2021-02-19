
import sys
from collections import defaultdict

from itertools import permutations


def countVis(seq):
    large = 0
    vis = len(seq)
    for i in seq:
        if large > i:
            vis -= 1
        else:
            large = i
    return vis


g = defaultdict(set)
for perm in permutations(range(1,5)):
    #print(perm, countVis(perm))
    g[countVis(perm)].add(perm)


rows,cols = ([1, 2, 2, 4, 2, 4], [1, 2, 2, 4, 4, 4])

n = len(rows)


grid = [[0 for i in range(n)] for j in range(n)]

for i in range(len(rows)):
    if rows[i]==1:
        grid[i][0] = n
    if cols[i]==1:
        grid[0][i] = n

#grid[0][3] = 5
#grid[1][0] = 5



def check():

    for i in range(n):
        if any([grid[i].count(k) > 1 for k in range(1, n+1)]): #or countVis(grid[i]) < rows[i]: #or
            return False
        if minVis(grid[i]) > rows[i] or maxVis(grid[i]) < rows[i]:
            #print(minVis(grid[i]), maxVis(grid[i]), grid[i], rows[i])
            return False
        s = []
        for j in range(n):
            s.append(grid[j][i])
        if any([s.count(k) > 1 for k in range(1, n+1)]): #or countVis(s) < cols[i]:
            return False
        if minVis(s) > cols[i] or maxVis(s) < cols[i]:
            #print(minVis(grid[i]), maxVis(grid[i]), grid[i], rows[i])
            return False
    return True

def checkFinal():
    for i in range(n):
        if countVis(grid[i]) != rows[i]:
            return False
        s = []
        for j in range(n):
            s.append(grid[j][i])
        if countVis(s) != cols[i]:
            return False
    return True

def maxVis(seq):
    seq2 = seq[:]
    left = [i for i in range(1, len(seq)+1) if i not in seq]

    c = 0
    for i in range(len(seq2)):
        if seq2[i]==0:
            seq2[i] = left[c]
            c += 1

    return countVis(seq2)

def minVis(seq):
    seq2 = seq[:]
    left = [i for i in range(1, len(seq)+1) if i not in seq][::-1]

    c = 0
    for i in range(len(seq2)):
        if seq2[i]==0:
            seq2[i] = left[c]
            c += 1

    return countVis(seq2)


valid = 0
def solve(x, y):
    global valid
    if y==n:
        if checkFinal():
            print("FOUND")
            valid += 1
            #input("FINSIHED: ")
            for m in grid:
                print(*m)
            print(time.time()-start)
            sys.exit(0)
        return

    if grid[y][x]!=0:
        if x==n-1:
            solve(0, y+1)
        else:
            solve(x+1, y)

    for val in range(1, n+1):
        grid[y][x] = val
        if check():
            #print(val, "AT", x, y, "IS VALID")
            if x==n-1:
                solve(0, y+1)
            else:
                solve(x+1, y)
            #print(val, "AT", x, y, "IS NOT VALID")
        grid[y][x] = 0
import time
start = time.time()
solve(0,0)
print(valid)

