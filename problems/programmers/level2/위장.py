def solution(clothes):        
    answer = dict()
    for i in range(len(clothes)):
        if clothes[i][1] not in answer:
            answer[clothes[i][1]] = 1
        else:
            answer[clothes[i][1]] += 1
    L = []
    for value in answer.values():
        L.append(value)
    
    sums = 1
    for i in range(len(L)):
        sums *= (L[i] + 1)
    return sums-1