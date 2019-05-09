def solution(nums):
    def combi(x, y):
        nonlocal cnt
        if y == 0:
            if sum(T) in sosuList:
                cnt += 1
        elif x < y:
            return
        else:
            T[y - 1] = nums[x - 1]
            combi(x - 1, y - 1)
            combi(x - 1, y)

    def sosu(x):
        T = [True] * (x + 1)
        N = int((x + 1) ** 0.5)
        for i in range(2, N + 1):
            if T[i]:
                for j in range(i + i, x + 1, i):
                    T[j] = False
        return [i for i in range(2, x + 1) if T[i]]

    sosuList = sosu(sum(nums))
    T = [0] * 3
    cnt = 0
    combi(len(nums), 3)

    return cnt