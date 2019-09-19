def solution(progresses, speeds):
    save = []
    for i in range(len(progresses)):
        for j in range(1, 101):
            if progresses[i] + speeds[i] * j >= 100:
                save.append(j)
                break

    answer = []
    save.append(101)
    comp = 0
    cnt = 0

    for i in range(len(save)):
        if comp < save[i]:
            if comp:
                answer.append(cnt)

            comp = save[i]
            cnt = 1
            
        else:
            cnt += 1

    return answer