def solution(priorities, location):
    q = []
    for idx, i in enumerate(priorities):
        q.append([idx, i])

    cnt = 9
    answer = 0
    
    while q:
        judge = False

        while not judge:
            for i in range(len(q)):
                if q[i][1] == cnt:
                    judge = True
                    break

            if not judge:
                cnt += -1

        x, y = q.pop(0)

        if y == cnt:
            answer += 1
            if x == location:
                break
        else:
            q.append([x, y])

    return answer

if __name__ == "__main__":
    priorities = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1], [1, 1, 1, 1, 1]]
    location = [2, 0, 3]
    for i in range(len(priorities)):
        print(solution(priorities[i], location[i]))
