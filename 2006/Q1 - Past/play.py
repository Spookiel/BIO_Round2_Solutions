
n = 6
from functools import lru_cache

#@lru_cache(maxsize=None)
def solve(pos, omax, umax, lmax,last,vis=0,cur=""):
    print(pos, omax, umax, lmax, vis, cur)
    input()
    if pos==n:
        if vis==0:
            print(pos, omax, umax, lmax, vis,lmin,cur)
            return 1
        return 0

    tot = 0
    for i in range(umax):
        tot += solve(pos+1, omax, umax-1, lmax,lmax-i-1, vis, cur+str(lmax-i-1))

    for j in range(omax):
        tot += solve(pos+1, n-(j+1), lmax+j, lmax+j+1,lmax+j+1,vis, cur+str(lmax+j+1))
    return tot



cur = [0]*n
print(cur)
def countVis(seq):
    large = 0
    vis = len(seq)
    for i in seq:
        if large > i:
            vis -= 1
        else:
            large = i
    return vis,large

def getLeft(seq):
    return [i for i in range(1, len(seq)+1) if i not in seq]


from math import factorial
tot = 0

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
def brute(pos,targ):
    global tot
    l = getLeft(cur)
    c,large = countVis(cur)
    if minVis(cur)[0] > targ or maxVis(cur)[0] < targ:
        return

    if all([i < large for i in l]):

         if countVis(cur[:pos])[0]==targ:
            #print(cur, l, cur[:pos], countVis(cur[:pos]))
            tot += factorial(len(l))
         return
    else:
        if cur[pos]!=0:
            brute(pos+1, targ)
            return


        for i in l:
            cur[pos] = i
            brute(pos+1, targ)
            cur[pos] = 0


#brute(0,8)
print(solve(0,n,0,0,4))