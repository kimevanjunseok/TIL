def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_list = list(skill)
        judge = 0
        for j in i:
            if j != skill_list[0] and j in skill_list:
                judge = 1
                break
            elif j == skill_list[0]:
                skill_list.pop(0)
                if not skill_list:
                    break
        if judge == 0:
            answer += 1
    return answer