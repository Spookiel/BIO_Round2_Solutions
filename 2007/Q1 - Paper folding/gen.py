from random import randint
import sys
import time


sys.setrecursionlimit(10000)

f = randint(2, 5000)
c = randint(1, 2**f-2)




def solve(folds, pos, inv):
    #print(folds, pos, inv)
    if folds==2:
        forw = "DDU"
        if not inv:
            return forw[pos-1]
        return "DUU"[pos-1]
    a = (2**folds)//2
    #print(a, folds, pos, inv)
    if pos==(2**folds)//2:
        return "D" if inv==0 else "U"

    if pos < a:
        return solve(folds-1, pos, 0)
    else:
        return solve(folds-1, pos-a, 1)

with open("paper.in", "w+") as fin:
    fin.write(f"{f} {c}")

start = time.time()
with open("paper.out", "w+")  as fout:
    fout.write(f"{solve(f, c, 0)} {solve(f, c+1, 0)} {solve(f, c+2, 0)}")
print(time.time()-start)



#DDUDDUUDDDUUDUUDDDUDDUUUDDUUDUUDDDUDDUUDDDUUDUUUDDUDDUUUDDUUDUU
#DDUDDUUDDDUUDUUDDDUDDUUUDDUUDUUDDDUDDUUDDDUUDUUUDDUDDUUUDDUUDUU