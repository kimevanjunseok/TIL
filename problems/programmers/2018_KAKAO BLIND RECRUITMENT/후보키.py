def comb(L, act, x, y, relation, answer):
    if y == 0:
        func([act[t] for t in range(len(act))], relation, answer)

    elif x < y:
        return

    else:
        act[y-1] = L[x-1]
        comb(L, act, x-1, y-1, relation, answer)
        comb(L, act, x-1, y, relation, answer)

def func(act, relation, answer):
    save = []
    for i in range(len(relation)):
        mid_save = []
        for j in act:
            mid_save.append(relation[i][j])
        if mid_save not in save:
            save.append(mid_save)
        else:
            return

    if not answer:
        answer.append(act)
    else:
        for i in answer:
            n = len(i)
            cnt = 0
            for j in i:
                if j in act:
                    cnt += 1
            if n == cnt:
                return
        
        answer.append(act)

def solution(relation):
    answer = []
    n = len(relation[0])
    num_list = list(range(n))
    for i in range(1, n+1):
        act = [0 for _ in range(i)]
        comb(num_list, act, n, i, relation, answer)

    return len(answer)

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
    solution(relation)