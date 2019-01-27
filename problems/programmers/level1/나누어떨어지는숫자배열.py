# My solution

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer

###################################################33

# Other

def solution(arr, divisor):
    arr = sorted([x for x in arr if x % divisor == 0])
    return arr if len(arr) != 0 else [-1]