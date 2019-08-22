def solution(N, stages):
    answer = []
    number = len(stages)
    for i in range(1, N+1):
        if number:
            user = stages.count(i)
            answer.append([i, user / number])
        else:
            answer.append([i, 0])
        number -= user

    answer.sort(key=lambda answer: answer[1], reverse=True)
    result = []
    for i in answer:
        result.append(i[0])
    return result

if __name__ == "__main__":
    N = [5, 4]
    stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4,4,4,4,4]]
    for i in range(len(N)):
        print(solution(N[i], stages[i]))