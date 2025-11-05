from queue import PriorityQueue
def dijkstra(maze, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    dist, prev = {start: 0}, {start: None}
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while not pq.empty():
        d, (x,y) = pq.get()
        if (x,y) == goal: break
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]!=1:
                nd = d+1
                if (nx,ny) not in dist or nd<dist[(nx,ny)]:
                    dist[(nx,ny)] = nd
                    prev[(nx,ny)] = (x,y)
                    pq.put((nd,(nx,ny)))
    # mark path
    cur = goal
    while cur and cur in prev:
        maze[cur[0]][cur[1]] = 2
        cur = prev[cur]
    maze[start[0]][start[1]] = 2
maze = [
 [0,0,1,0,0],
 [1,0,1,0,1],
 [0,0,0,0,0],
 [1,1,1,0,1],
 [0,0,0,0,0]
]
dijkstra(maze, (0,0), (4,4))
for r in maze: print(r)
