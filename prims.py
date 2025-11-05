import heapq
def prims(graph, start):
    visited = set()
    pq = [(0, start, None)]
    mst, total = [], 0
    while pq:
        w, u, parent = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        total += w
        if parent:
            mst.append((parent, u, w))
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (weight, v, u))
    print("\nMinimum Spanning Tree (Prim):")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print("Total Distance:", total)

# ---------- User Input ----------
n = int(input("Enter number of departments: "))
graph = {}
for i in range(n):
    name = input(f"Enter name of department {i+1}: ")
    graph[name] = []

e = int(input("Enter number of links (edges): "))
for i in range(e):
    u = input("From: ")
    v = input("To: ")
    w = int(input("Distance: "))
    graph[u].append((v, w))
    graph[v].append((u, w))  # undirected

start = input("Enter starting department: ")
prims(graph, start)
