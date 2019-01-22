# My solution

def solution(arr):
    answer = [arr[0]]
    point = 0
    for i in range(1, len(arr)):
        if answer[point] != arr[i]:
            answer.append(arr[i])
            point += 1
    return answer

########################################

# Other

def solution(arr):
    L = []
    for i in arr:
        if L[-1:] == [i]: 
            continue
        L.append(i)
    return L

