from collections import defaultdict
from itertools import permutations
import random

n = 8

grid = [[0 for i in range(n)] for j in range(n)]



def check():

    for i in range(n):
        if any([grid[i].count(k) > 1for k in range(1, n+1)]): #or countVis(grid[i]) < rows[i]: #or
            return False

        s = []
        for j in range(n):
            s.append(grid[j][i])
        if any([s.count(k) > 1 for k in range(1, n+1)]): #or countVis(s) < cols[i]:
            return False
    return True


def isEmpty():
    for i in grid:
        for j in i:
            if j==0:
                return True
    return False
got = False
valid = 0
case = None
def solve(x, y):
    global valid,got,case
    if got: return
    if y==n:
        if check() and not isEmpty():
            valid += 1

            ans = []
            for m in grid:
                ans.append(m[:])
            if valid==50000:
                got = True
                case = ans
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

def countVis(seq):
    large = 0
    vis = len(seq)
    for i in seq:
        if large > i:
            vis -= 1
        else:
            large = i
    return vis


def compVals(board):
    rows = []
    cols = []
    for i in range(len(board)):
        rows.append(countVis(board[i]))
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        cols.append(countVis(col))
    return rows, cols

solve(0,0)

chosen = [i for i in case]

#chosen = [[1,3,2,4],[4,2,1,3],[3,1,4,2],[2,4,3,1]]
for m in chosen:
    print(*m)
a,b = compVals(chosen)
print()
print(*a)
print(*b)
print(chosen)
