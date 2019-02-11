def DFS(V):
    global G, visited, n
    visited[V] = 1
    print(V, end=" ")
    for w in range(n):
        if G[V][w] == 1 and visited[w] == 0:
            DFS(w)

n = 8
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

G = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for i in range(n)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(n):
    print("{} {}".format(i, G[i]))

DFS(1)



