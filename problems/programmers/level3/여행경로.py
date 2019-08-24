def DFS(L, tickets, n):
    visited.append(L)
    tickets.remove(L)
    if not tickets:
        result.append(["" for _ in range(n + 1)])
        result[-1][0] = visited[0][0]
        for i in range(len(visited)):
            result[-1][i+1] = visited[i][1]

    else:
        for i in range(len(tickets)):
            if (L[1] == tickets[i][0]):
                DFS(tickets[i], [t[:] for t in tickets], n) 

    visited.pop()

def solution(tickets):
    n = len(tickets)
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            DFS(tickets[i], [t[:] for t in tickets], n)

    result.sort()
    return result[0]

visited = []
result = []

if __name__ == "__main__":
    # tickets = [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]]
    tickets =  [[ "ICN", "BOO" ], [ "ICN", "COO" ], [ "COO", "DOO" ], [ "DOO", "COO" ], [ "BOO", "DOO" ],[ "DOO", "BOO" ], [ "BOO", "ICN" ], [ "COO", "BOO" ]]
    print(solution(tickets))
   