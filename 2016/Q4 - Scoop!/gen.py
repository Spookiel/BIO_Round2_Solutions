import random
import os
import subprocess
MAXGRAPHSIZE = 50000
CHANCE = 100
parent = [0]*(MAXGRAPHSIZE+1)
# Needs to generate a connected graph, with an even number of nodes
# Using a DSU, add edges to the graph sequentially checking for connnectivity at each edge added
# Keeping track of edges added so no duplicate edges are added
# Additionally there is a 40% chance of two components being joined instead of just randomly drawing edges
# Therefore if you change CHANCE to 100, it will create a tree

def initialise(SIZE):
    for i in range(1, SIZE+1):
        parent[i] = i


def find(x):
    if(parent[x]==x):
        return x

    parent[x] = find(parent[x])
    return parent[x]

def unite(a, b):
    c,d = find(a), find(b)
    if(c!=d):
        parent[d] = c


def checkSol():
    pass





def check(nodes):
    f = find(1)
    for i in range(2, nodes+1):
        if find(i)!=f:
            return False
    return True

def generate():
    nodes = random.choice([i for i in range(2, MAXGRAPHSIZE, 2)])
    initialise(nodes)

    edges = set()
    while not check(nodes):
        # Draw a random edge between two components
        while True:
            start, end = random.randint(1, nodes), random.randint(1, nodes)
            if start!=end and (find(start)!=find(end) or  random.randint(0,100) > CHANCE) and (start, end) not in edges:
                break
        unite(start, end)
        edges.add((start, end))
        edges.add((end, start))
    got = len(edges)//2
    print(f"GENERATED {nodes} with {got} edges")
    with open("scoop.in", "w+") as fin:
        fin.write(f"{nodes} {random.randint(1, nodes)}\n")
        while edges:
            s,e = edges.pop()
            edges.remove((e, s))
            fin.write(f"{s} {e}\n")
        #fin.write("-1 -1\n")
    return nodes, got

import time
def stress(fname, NUMTESTS=1000):
    for i in range(NUMTESTS):
        nodes,edges = generate()
        start = time.time()
        subprocess.check_call(os.getcwd()+"/"+fname, stdout=None)
        if not checkSol(nodes):
            print("FAILED")
            break
        print("COMPLETED IN", round(time.time()-start,5), nodes, edges)
    print("-----------------")
    print(f"Completed {NUMTESTS} tests successfully")

def checkOne():
    if input("GEN NEW: (y/n)") in "yesYes":
        generate()


checkOne()
#stress("scoop", 100)










