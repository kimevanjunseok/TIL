def enter(uid, nickname):
    answer.append("님이 들어왔습니다.")
    backup.append(uid)
    userinfo[uid] = nickname

def leave(uid):
    answer.append("님이 나갔습니다.")
    backup.append(uid)

def change(uid, nickname):
    userinfo[uid] = nickname

answer = []
backup = []
userinfo = dict()

def solution(record):
    for rec in record:
        info = rec.split()
        if info[0] == "Enter":
            enter(info[1], info[2])
        elif info[0] == "Leave":
            leave(info[1])
        elif info[0] == "Change":
            change(info[1], info[2])
    
    result = []
    for i in range(len(answer)):
        result.append(userinfo[backup[i]] + answer[i])

    return result

if __name__ == "__main__":
    input_list = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"] 
    print(solution(input_list))
