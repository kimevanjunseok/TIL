def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                break
        answer.append(j-i)
    answer.append(0)
    return answer