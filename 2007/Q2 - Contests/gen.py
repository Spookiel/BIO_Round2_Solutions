import random
MAXGRAPHSIZE = 5000
CHANCE = 50
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

    with open("contests.in", "r") as fin:
        nnodes = int(fin.readline())


    degs = [0] * (nnodes+1)
    with open("contests.out", "r") as fout:
        n = int(fout.readline())
        for i in range(n):
            s, e = list(map(int, fout.readline().split()))
            degs[s] += 1
            degs[e] += 1
    return all([i % 2 == 1 for i in degs[1:nodes + 1]])





def check():
    f = find(1)
    for i in range(2, nodes+1):
        if find(i)!=f:
            return False
    return True

def generate():
    edges = set()
    while not check():
        # Draw a random edge between two components
        while True:
            start, end = random.randint(1, nodes), random.randint(1, nodes)
            if start!=end and (find(start)!=find(end) or  random.randint(0,100) > CHANCE) and (start, end) not in edges:
                break
        unite(start, end)
        edges.add((start, end))
        edges.add((end, start))
    print(nodes, len(edges)//2)
    with open("contests.in", "w+") as fin:
        fin.write(f"{nodes}\n")
        while edges:
            s,e = edges.pop()
            edges.remove((e, s))
            fin.write(f"{s} {e}\n")
        fin.write("-1 -1\n")
nodes = random.choice([i for i in range(2, MAXGRAPHSIZE, 2)])
initialise(nodes)


if input("GEN NEW: (y/n)") in "yesYes":
    generate()

isCorrect = checkSol()



print(isCorrect)











