# My soloution

def solution(n, lost, reserve):
    answer = [1]*(n+2)
    answer[n+1] = 0
    answer[0] = 0
    cnt = 0

    for i in lost:
        answer[i] += -1
    for i in reserve:
        answer[i] += 1
    for i in range(2, n-1):
        if answer[i] == 0:
            if answer[i-1] == 2:
                answer[i] += 1
                answer[i-1] += -1
            elif answer[i+1] == 2:
                answer[i] += 1
                answer[i+1] += -1
    for i in answer:
        if i >= 1:
            cnt += 1

    return cnt

###############################################

# Other

def solution(n, lost, reserve):
    reserve_list = [i for i in reserve if i not in lost]
    lost_list = [i for i in lost if i not in reserve]

    for i in reserve_list:
        front = i - 1
        back = i + 1
        if front in lost_list:
            lost_list.remove(front)
        elif back in lost_list:
            lost_list.remove(back)
            
    return n - len(lost_list)
