def cal(x, works, n):
    sum_N = 0
    for i in range(len(works)):
        if works[i] > x:
            sum_N += works[i] - x
        else:
            break
    
    if sum_N > n:
        return "false"
    elif sum_N == n:
        return "true"
    else:
        return "continue"

def bin_search(start, end, works, n):
    save = 0
    while start <= end:
        mid = (start + end) // 2
        com = cal(mid, works, n)
        if com == "continue":
            end = mid - 1
            save = mid
        elif com == "true":
            return mid
        else:
            start = mid + 1
    return save

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        answer = 0

    else:
        works.sort(reverse=True)
        k = bin_search(0, max(works), works, n)
        if k:
            for i in range(len(works)):
                if works[i] > k:
                    n += -(works[i] - k)
                    works[i] = k
                else:
                    break

        for i in range(len(works)):
            if n:
                works[i] += -1
                n += -1
         
            answer += works[i] ** 2

    return answer

if __name__ == "__main__":
    n = [4, 1, 3]
    works = [[4, 3, 3], [2, 1, 2], [1, 1]]
    for i in range(len(n)):
        print(solution(n[i], works[i]))
