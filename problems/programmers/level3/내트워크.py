def solution(n, computers):  
    def func(x):
        nonlocal n, computers, visited

        for i in range(n):
            if computers[x][i] == 1:
                if i not in visited:
                    visited.append(i)
                    func(i)
    result = 0
    visited = []

    for i in range(n):
        if i not in visited:
            visited.append(i)
            func(i)
            result += 1

    return result

if __name__ == "__main__":
    n = [3, 3]
    computers = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]
    for i in range(len(n)):
        print(solution(n[i], computers[i]))