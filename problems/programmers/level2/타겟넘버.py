def solution(numbers, target):
    def dfs(x, sums, y, z):
        nonlocal cnt, target
        if x == y:
            if sums == target:
                cnt += 1
            return 

        dfs(x+1, sums + numbers[x], y, z)
        dfs(x+1, sums - numbers[x], y, z)

    N = len(numbers)
    cnt = 0
    dfs(0, 0, N, target)
    return cnt