# My solution

def solution(answers):
    frist = [1, 2, 3, 4, 5]*(len(answers) // 5 + 1)
    second = [2, 1, 2, 3, 2, 4, 2, 5]*(len(answers) // 8 + 1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answers) // 10 + 1)
    answer = []
    cnt_first, cnt_second, cnt_third = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == frist[i]:
            cnt_first += 1
        
        if answers[i] == second[i]:
            cnt_second += 1
        
        if answers[i] == third[i]:
            cnt_third += 1

    if cnt_first > cnt_second and cnt_first > cnt_third:
        answer = [1]
    elif cnt_second > cnt_first and cnt_second > cnt_third:
        answer = [2]
    elif cnt_third > cnt_first and cnt_third > cnt_second:
        answer = [3]
    elif cnt_first == cnt_second and cnt_first > cnt_third:
        answer = [1, 2]
    elif cnt_first == cnt_third and cnt_first > cnt_second:
        answer = [1, 3]
    elif cnt_second == cnt_third and cnt_second > cnt_first:
        answer = [2, 3]
    else:
         answer = [1,2,3]
    return answer

######################################################################

# Other

def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    score = [0, 0, 0]
    answer = []

    for idx, ans in enumerate(answers):
        if ans == first[idx%len(first)]:
            score[0] += 1
        if ans == second[idx%len(second)]:
            score[1] += 1
        if ans == third[idx%len(third)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
    return answer

