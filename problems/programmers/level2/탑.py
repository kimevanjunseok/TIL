def solution(heights):
    answer = [0] * len(heights)
    for i in range(len(heights)-1, 0, -1):
        x = heights[i]
        for j in range(i-1, -1, -1):
            if heights[j] > x:
                answer[i] = j+1
                break
    return answer