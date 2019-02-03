# My solution

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] in 'Kim':
            return f"김서방은 {i}에 있다"