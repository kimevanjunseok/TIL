#My solution

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

#############################################

# Other
# collection를 주면 리스트 안의 값을 딕셔너리로 반환

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return "".join(answer.keys())

print(solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))

# collection 공부