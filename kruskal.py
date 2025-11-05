# Kruskal's Algorithm (User Input)

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot, yroot = find(parent, x), find(parent, y)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

def kruskal(edges, nodes):
    edges.sort(key=lambda x: x[2])
    parent = {n: n for n in nodes}
    rank = {n: 0 for n in nodes}
    mst = []
    total = 0

    for u, v, w in edges:
        x, y = find(parent, u), find(parent, v)
        if x != y:
            mst.append((u, v, w))
            total += w
            union(parent, rank, x, y)

    print("\nMinimum Spanning Tree (Kruskal):")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print("Total Distance:", total)

# ---------- User Input ----------
n = int(input("Enter number of departments: "))
nodes = []
for i in range(n):
    nodes.append(input(f"Enter name of department {i+1}: "))

e = int(input("Enter number of links (edges): "))
edges = []
for i in range(e):
    u = input("From: ")
    v = input("To: ")
    w = int(input("Distance: "))
    edges.append((u, v, w))

kruskal(edges, nodes)
