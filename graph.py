HIGH = 99999
class Graph:
    def __init__(self):
        self.g = []          # adjacency matrix
        self.n = 0
        self.v_array = []    # visited array
        self.dept = []       # department names
    def initialize(self):
        self.n = int(input("\nEnter total departments: "))
        print("\nEnter department names:")
        for i in range(self.n):
            name = input()
            self.dept.append(name)
        self.g = [[0] * self.n for _ in range(self.n)]
        print("\nEnter distance between departments (0 if no direct path):")
        # adjacency matrix input for undirected graph
        for i in range(self.n):
            for j in range(i, self.n):
                if i == j:
                    self.g[i][j] = 0
                else:
                    dist = int(input(f"Distance between {self.dept[i]} and {self.dept[j]}: "))
                    if dist == 0:
                        self.g[i][j] = HIGH
                        self.g[j][i] = HIGH
                    else:
                        self.g[i][j] = dist
                        self.g[j][i] = dist
    # display adjacency matrix
    def display(self):
        print("   ", end="\t")
        for i in range(self.n):
            print(self.dept[i], end="\t")
        print()
        for i in range(self.n):
            print(self.dept[i], end="\t")
            for j in range(self.n):
                print(self.g[i][j], end="\t")
            print()
    def prims(self):
        cost = 0
        self.v_array = [False] * self.n
        self.v_array[0] = True
        print("\nPrim's MST -> EDGE : Weight")
        n_edges = 0
        while n_edges < self.n - 1:
            minimum = HIGH
            u = v = 0
            for i in range(self.n):
                if self.v_array[i]:
                    for j in range(self.n):
                        if not self.v_array[j] and self.g[i][j] and self.g[i][j] < minimum:
                            minimum = self.g[i][j]
                            u, v = i, j
            print(f"Edge: {self.dept[u]} - {self.dept[v]} with weight {self.g[u][v]}")
            cost += self.g[u][v]
            self.v_array[v] = True
            n_edges += 1
        print("\nCost of minimum spanning tree using Prim's:", cost)
    # ---------- Kruskal’s Algorithm ----------
    # find set of an element i
    def find(self, parent, i):
        while parent[i] != i:
            i = parent[i]
        return i
    # do union of two subsets
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def kruskals(self):
        edges = []
        # extract edges from adjacency matrix
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.g[i][j] != 0 and self.g[i][j] != HIGH:
                    edges.append((self.g[i][j], i, j))
                    print(f"Edge: {self.dept[i]} - {self.dept[j]} with weight {self.g[i][j]}")
        # sort edges by weight
        edges.sort()
        # Make disjoint sets
        parent = [i for i in range(self.n)]
        rank = [0] * self.n
        print("\nDisjoint sets initialized.")
        print("Parent array:", parent)
        print("Rank array:", rank)
        mst_edges = []
        cost = 0
        # iterate through sorted edges
        for w, u, v in edges:
            x = self.find(parent, u)
            y = self.find(parent, v)
            print(f"Processing edge {self.dept[u]} - {self.dept[v]} with weight {w}")
            if x != y:
                mst_edges.append((u, v, w))
                cost += w
                self.union(parent, rank, x, y)
                print("added to MST")
            else:
                print("creates a cycle and is skipped")
        print("\nKruskal's MST -> EDGE : Weight")
        for u, v, w in mst_edges:
            print(f"{self.dept[u]} - {self.dept[v]} : {w}")
        print("\nCost of minimum spanning tree using Kruskal's:", cost)
if __name__ == "__main__":
    g = Graph()
    g.initialize()
    g.display()
    g.prims()
    g.kruskals()
